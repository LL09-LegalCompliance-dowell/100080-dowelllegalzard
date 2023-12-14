import os
import re

import requests
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from doWellOpensourceLicenseCompatibility import doWellOpensourceLicenseCompatibility
from github import Github
from github import GithubIntegration
from github_webhook.send_email import send_email, EMAIL_FROM_WEBSITE
import json

def remove_prefix(users):
    cleaned_users = []
    for user in users:
        login = user.login.replace('NamedUser(login="', '')
        cleaned_users.append(login)
    return cleaned_users

def add_prefix(names):
    prefixed_names = []
    for name in names:
        prefixed_names.append('@' + name)
    return ' '.join(prefixed_names)

@csrf_exempt
def legalzard_webhook(request):
    # Only post method is allowed from the github bot
    if request.method != 'POST':
        return HttpResponse('Method not allowed', status=400)    
    try:
        # get github payload
        payload = json.loads(request.body.decode('utf-8'))
        # get license information
        sender_email = payload["check_suite"]["head_commit"]["author"]["email"] or 'test@gmail.com'
        
        repo_license_id = payload['repository']['license']
        # Send email to user telling them to add their primary licnese
        if not repo_license_id:
            print(sender_email)
            subject="Dowell UX Living Lab Legalzard Github Bot Alert"
            email_content="You need to First Add a License to your Repository Before we can check Compatibility!"
            send_email('Repository Owner', sender_email, subject, email_content)
            return HttpResponse('OK', status=200)
        # print("License", repo_license_id)
        # repository details
        owner = payload['repository']['owner']['login']
        repo_name = payload['repository']['name']
        print("Owner: ", owner)
        print("Repo: ", repo_name)

        # Read the bot certificate
        app_id = settings.LEGALZARD_BOT_APP_ID
        with open(
                os.path.normpath(os.path.expanduser(settings.LEGALZARD_BOT_KEY_PATH)),
                'r'
        ) as cert_file:
            app_key = cert_file.read()
        # Create an GitHub integration instance
        git_integration = GithubIntegration(
            app_id,
            app_key,
        )

        # Get a git connection as our bot
        # Here is where we are getting the permission to talk as our bot and not
        # as a Python webservice
        github_auth = git_integration.get_access_token(git_integration.get_installation(owner, repo_name).id).token
        git_connection = Github(login_or_token=github_auth)
        repo = git_connection.get_repo(f"{owner}/{repo_name}")

        #getting a list of all the repo collaborators and then formatting by adding `@` before each name
        #to simulate mentions. This will ensure each member gets notified via email
        print("Github Auth: ", github_auth)
        members = repo.get_collaborators()
        for c in members:
            collaborators.append(c)

        collaborators = add_prefix(remove_prefix(collaborators))
        print("Collaborators: ", collaborators)


        # get repo dependencies
        sbom_request = requests.get(f'https://api.github.com/repos/{owner}/{repo_name}/dependency-graph/sbom',
                                    headers={'Authorization': f'Bearer {github_auth}',
                                            'X-GitHub-Api-Version': '2022-11-28'})
        print("SBOM Request: ", sbom_request.json())
        if sbom_request.status_code != 200:
            return HttpResponse('OK', status=200)

        sbom = sbom_request.json()
        packages = sbom.get('sbom').get('packages', [])
        package_license_ids = set()

        for p in packages:
            p_license = p.get('licenseConcluded', None)
            if p_license is None:
                continue
            # separate combined licenses
            for l in re.sub(r'\([^()]*\)', '', p_license).split(" "):
                if l not in ["AND", "OR"]:
                    package_license_ids.add(l)
        
        # Empty set guard clause
        if len(package_license_ids) == 0:
            subject="Dowell UX Living Lab Legalzard Github Bot Alert"
            email_content="Your repository does not seem to have additional licenses. You may no have used additional libraries or you have a missing package.json file or requirements.txt file!"
            send_email('Repository Owner', sender_email, subject, email_content)
            return HttpResponse('OK', status=200)
        
        # Get spdx license data
        spdx_request = requests.get("https://spdx.org/licenses/licenses.json")
        if spdx_request.status_code != 200:
            return HttpResponse('OK', status=200)

        licenses = spdx_request.json().get('licenses')
        print("Licenses: ", licenses)
        # use the compatibility library
        legalzard_api = doWellOpensourceLicenseCompatibility(api_key=settings.LEGALZARD_API_KEY)
        repo_license = legalzard_api.search(repo_license_id['key']).get("data")[0]
        repo_license_event_id = repo_license.get("eventId")

        #  initialize issues
        incompatible_licenses = ""
        truth = False
        # run comparison with package licenses
        for l_id in package_license_ids:
            try:
                # get license
                l_name = next(lnc for lnc in licenses if lnc["licenseId"] == l_id)["name"]
                # prepare comparison data
                _pkg_license = legalzard_api.search(l_name).get("data")[0]
                _pkg_license_event_id = _pkg_license.get("eventId")
                compatibility = legalzard_api.check_compatibility({
                    "license_event_id_one": repo_license_event_id,
                    "license_event_id_two": _pkg_license_event_id,
                })["is_compatible"]
                # skip compatible licenses
                if compatibility:
                    continue
                # log incompatible licenses
                incompatible_licenses += f"{l_name}\n"
            except Exception as e:
                print(e)
                pass

        if len(incompatible_licenses) > 0:
            #format the table
            table_rows = [f"<tr><td>Licence Detail</td><td>{i}</td></tr>" for i in incompatible_licenses]
            table_html = "<table>" + "".join(table_rows) + "</table>"
            truth = True

        # prepare and write issue
        issue= f"{collaborators} Legalzard found licenses in your dependencies that are incompatible with your repository license\n\n {incompatible_licenses}" if truth == True else f"{collaborators} Legalzard found no license compatibility issues in your dependencies"
        repo.create_issue(title="Incompatible Licenses", body=issue)
        html_p = "<p>Legalzard found no licence in your repo</p>"

        #set email payload and send email
        subject = "Legalzard Bot Alert: Incompatible Licenses"
        email_content = table_html if truth == True else html_p
        send_email('Dowell UX Living Legalzard Bot Alert!', sender_email, subject, email_content)

        return HttpResponse('OK', status=200)
    
    except KeyError:
        return HttpResponse('OK', status=422)
    except Exception as e:
        print("Error Handling User Request", e)
        return HttpResponse('Internal Server Error', status=500)
