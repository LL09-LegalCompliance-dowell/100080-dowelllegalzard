import os
from string import Template
from DowellLicenseProject.settings import BASE_DIR

agreement_compliance_templates = {
    "software-license-policy": "software-license-agreement.html",
    "eula": "end-user-licensing-agreement.html",
    "mou": "memorandum-of-understanding.html",
    "website-terms-of-use": "website-terms-of-use.html",
    "website-privacy-policy": "website-privacy-policy.html",
    "website-security-policy": "website-security-policy.html",
    "non-compete-agreement": "non-compete-agreement.html",
    "cookie-policy": "cookie-policy.html",
    "return-and-refund": "return-and-refund.html",
    "app-disclaimer": "app-disclaimer.html",
    "app-privacy-policy": "app-privacy-policy.html"
}


def read_template(filename:str) -> Template:
    content=""

    # Get obsolute path
    file_path = os.path.join(BASE_DIR, f"templates/agreement-compliance/{filename}")

    # load content
    with open(file_path, 'r') as template_file:
        content = template_file.read()
        
    return Template(content)


def get_compliance_template_name(agreement_compliance_type:str) -> str:
    return agreement_compliance_templates[agreement_compliance_type]