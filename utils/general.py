import os
from string import Template
from DowellLicenseProject.settings import BASE_DIR


def read_template(filename:str) -> Template:
    content=""

    # Get obsolute path
    file_path = os.path.join(BASE_DIR, f"templates/agreement-compliance/{filename}")

    # load content
    with open(file_path, 'r') as template_file:
        content = template_file.read()
        
    return Template(content)


def get_compliance_template_name(agreement_compliance_type:str) -> str:

    if agreement_compliance_type == "software-license-policy":
        return "software-license-agreement.html"

    elif agreement_compliance_type == "eula":
        return "end-user-licensing-agreement.html"

    elif agreement_compliance_type == "mou":
        return "memorandum-of-understanding.html"

    elif agreement_compliance_type == "website-terms-of-use":
        return "website-terms-of-use.html"