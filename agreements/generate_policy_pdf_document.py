import os
import datetime
from .convert_html_to_pdf import generate_pdf
from django.conf import settings
from django.template.loader import get_template


def create_pdf_document(context, policy_template_name):
    new_filename = ""
    try:
        template = get_template(f'software-policy/{policy_template_name}')
        html=template.render(context)

        # Get storage path
        root_path = os.path.join(settings.MEDIA_ROOT, 'documents/')

        # get new filename
        datetime_format=datetime.datetime.now().strftime("%m%d%Y%H%M%S")
        new_filename=f'{context["_id"].replace("-", "_").upper()}_{datetime_format}.PDF'
        file_path = f'{root_path}{new_filename}'

        # Generate pdf document]
        generate_pdf(html,f'{root_path}{new_filename}')


        #PERMIT READ FILE
        try:
            os.chmod(file_path, 0o777)
        except Exception as e:
            print(str(e))
        #END PERMIT READ FILE

    except Exception as e:
        print("error message")
        print(str(e))
    return new_filename






if __name__ == "__main__":
    context = {
        "software_product_license_name": "Apache v2.0",
        "software_product": "Friends Packet",
        "software_product_license_name_uc": "Packet 400",
        "liability_remedy_amount": "2000.00",
        "state_law_applies": "India",
        "license_jurisdiction_city": "Mubai",
        "license_jurisdiction_state": "India",
        "license_representative_name": "Charu",
        "license_representative_address": "784 state road",
        "license_representative_city": "Mubai",
        "license_representative_state": "India",
        "license_representative_zipcode": "00245",
        "license_representative_phone": "02154555555",
        "license_representative_email": "sample@sample.com"
        }

    create_pdf_document(context, "enduserlicensingagreement.html")


    