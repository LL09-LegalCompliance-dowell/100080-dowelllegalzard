import os
import re

import requests
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from doWellOpensourceLicenseCompatibility import doWellOpensourceLicenseCompatibility
from github import Github
from github import GithubIntegration


@csrf_exempt
def legalzard_webhook(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed', status=400)

    # get github payload
    payload = request.body.decode()

    # get license information
    repo_license_id = payload.get('repository').get('license')
    if not repo_license_id:
        return HttpResponse('OK', status=200)

    # repository details
    owner = payload['repository']['owner']['login']
    repo_name = payload['repository']['name']

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
    # get repo dependencies
    sbom_request = requests.get(f'https://api.github.com/repos/{owner}/{repo_name}/dependency-graph/sbom',
                                headers={'Authorization': f'Bearer {github_auth}',
                                         'X-GitHub-Api-Version': '2022-11-28'})
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
        return HttpResponse('OK', status=200)
    # Get spdx license data
    spdx_request = requests.get("https://spdx.org/licenses/licenses.json")
    if spdx_request.status_code != 200:
        return HttpResponse('OK', status=200)

    licenses = spdx_request.json().get('licenses')
    # use the compatibility library
    legalzard_api = doWellOpensourceLicenseCompatibility(api_key=settings.LEGALZARD_API_KEY)
    repo_license = legalzard_api.search(repo_license_id).get("data")[0]
    repo_license_event_id = repo_license.get("eventId")

    #  initialize issues
    incompatible_licenses = ""
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
            pass
    # prepare and write issue
    issue = f"Legalzard found licenses in your dependencies that are incompatible with your repository license\n\n {incompatible_licenses}"
    repo.create_issue(title="Incompatible Licenses", body=issue)
    return HttpResponse('OK', status=200)