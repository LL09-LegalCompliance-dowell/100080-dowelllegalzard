import os
import re

import requests
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from github import Github
from github import GithubIntegration
from github_webhook.send_email import send_email, EMAIL_FROM_WEBSITE
import json


def search_license(search_term):
    response = requests.get(f'https://100080.pythonanywhere.com/api/licenses/?search_term={search_term}&action_type=search')
    license_data = response.json()['data'][0]
    print("Event ID", license_data['eventId'])
    return license_data['eventId']


def check_compatibility(event1, event2):
    api_url = "https://100080.pythonanywhere.com/api/licenses/"
    json_payload = {
    "action_type": "check-compatibility",
    "license_event_id_one": event1,
    "license_event_id_two": event2,
    }
    response = requests.post(api_url, json=json_payload)
    is_compatible = response.json()['is_compatible']
    percentage_of_compatibility = response.json()['percentage_of_compatibility']
    print("is_compatible: ", is_compatible)
    print("percentage_of_compatibility: ", percentage_of_compatibility)
    return is_compatible

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
        # print("Payload: ", payload)
        sender_email = ""
        try:
            sender_email = payload["check_suite"]["head_commit"]["author"]["email"]
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")        
        else:
            sender_email = payload["head_commit"]["author"]["email"]
        finally:
            print("Division operation completed.")

        # repository details
        repo_license_key = payload['repository']['license']
        owner = payload['repository']['owner']['login']
        repo_name = payload['repository']['name']

        # Read the bot certificate
        app_id = settings.LEGALZARD_BOT_APP_ID
        print("App_ID:", app_id)
        print("Bot Key path", settings.LEGALZARD_BOT_KEY_PATH)
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
        print("Github integration done!")
        # Get a git connection as our bot
        # Here is where we are getting the permission to talk as our bot and not
        # as a Python webservice
        github_auth = git_integration.get_access_token(git_integration.get_installation(owner, repo_name).id).token
        git_connection = Github(login_or_token=github_auth)
        repo = git_connection.get_repo(f"{owner}/{repo_name}")
        # print("Repo details", repo)
        
        #getting a list of all the repo collaborators and then formatting by adding `@` before each name
        #to simulate mentions. This will ensure each member gets notified via email
        print("Github Auth: ", github_auth)
        collaborators = []
        members = repo.get_collaborators()
        for c in members:
            collaborators.append(c)

        collaborators = add_prefix(remove_prefix(collaborators))
        # print("Collaborators: ", collaborators)
        
        repo_license_id = payload['repository']['license']
        # Send email to user telling them to add their primary licnese
        if not repo_license_id:
            print(sender_email)
            print(collaborators)
            subject="Dowell UX Living Lab Legalzard Github Bot Alert"
            email_content="You need to First Add a License to your Repository Before we can check Compatibility!"
            issue= f"{collaborators} Attention! You need to First Add a License to your Repository Before we can check Compatibility!"        
            try:
                repo.create_issue(title="No License Found", body=issue)
                print("issue created. Trying to send email...")
                if sender_email:
                    send_email('Repository Owner', sender_email, subject, email_content)
            except Exception as e:
                print(f"Error: An unexpected error occurred - {e}")
            return HttpResponse('OK', status=200)

        # get repo dependencies
        sbom_request = requests.get(f'https://api.github.com/repos/{owner}/{repo_name}/dependency-graph/sbom',
                                    headers={'Authorization': f'Bearer {github_auth}',
                                            'X-GitHub-Api-Version': '2022-11-28'})
        # print("SBOM Request: ", sbom_request.json())
        if sbom_request.status_code != 200:
            return HttpResponse('OK', status=200)

        sbom = sbom_request.json()
        packages = sbom.get('sbom').get('packages', [])
        package_license_ids = set()
        print("packages", packages)

        for p in packages:
            p_license = p.get('licenseConcluded', None)
            if p_license is None:
                continue
            # separate combined licenses
            for l in re.sub(r'\([^()]*\)', '', p_license).split(" "):
                if l not in ["AND", "OR"]:
                    package_license_ids.add(l)

        # print("package_license_ids", package_license_ids)
        # Empty set guard clause
        if len(package_license_ids) == 0:
            subject="Dowell UX Living Lab Legalzard Github Bot Alert"
            email_content="Your repository does not seem to have additional licenses. You may no have used additional libraries or you have a missing package.json file or requirements.txt file!"
            send_email('Repository Owner', sender_email, subject, email_content)
            return HttpResponse('OK', status=200)

        repo_license_event_id = search_license(repo_license_key)
        #  initialize issues
        incompatible_licenses = ""
        truth = False
        # run comparison with package licenses
        for license_id in package_license_ids:
            try:
                # get license
                license_event_id = search_license(license_id)
                compatibility = check_compatibility(repo_license_event_id, license_event_id)
                # skip compatible licenses
                if compatibility:
                    print("Is compatible")
                    continue
                # log incompatible licenses
                incompatible_licenses += f"{license_event_id}\n"
            except Exception as e:
                print(e)
                pass

        if len(incompatible_licenses) > 0:
            #format the table
            table_rows = [f"<tr><td>Licence Detail</td><td>{i}</td></tr>" for i in incompatible_licenses]
            table_html = "<table>" + "".join(table_rows) + "</table>"
            truth = True

        # prepare and write issue
        issue= ""
        if truth == True:
            f"{collaborators} Legalzard found licenses in your dependencies that are incompatible with your repository license\n\n {incompatible_licenses}" 
        else:
            f"{collaborators} Legalzard found no license compatibility issues in your dependencies"
        
        repo.create_issue(title="Incompatible Licenses", body=issue)
        
        html_p = "<p>Legalzard found no licence in your repo</p>"
        #set email payload and send email
        subject = "Legalzard Bot Alert: Incompatible Licenses"
        email_content = table_html if truth == True else html_p
        send_email('Dowell UX Living Legalzard Bot Alert!', sender_email, subject, email_content)

        return HttpResponse('OK', status=200)

    #except KeyError as e:
    #    print(f"KeyError encountered: {e}")
    #    return HttpResponse('OK', status=422)
    except Exception as e:
        print("Error Handling User Request", e)
        return HttpResponse('Internal Server Error', status=500)
