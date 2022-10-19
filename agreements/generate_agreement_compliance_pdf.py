import os
import datetime
from django.conf import settings
import pdfkit
from utils.general import read_template, get_compliance_template_name

def create_pdf_document(context:dict):
    new_filename = ""
    try:
        # Get storage path
        # /home/100080/100080-dowelllegalzard/vol/web
        root_path = os.path.join(settings.MEDIA_ROOT, 'documents/')


        # get new filename
        datetime_format=datetime.datetime.now().strftime("%m%d%Y%H%M%S")
        new_filename=f'{context["_id"].replace("-", "_").upper()}_{datetime_format}.PDF'
        file_path = f'{root_path}{new_filename}'


        # load commpliance template from the filesystem
        content = read_template(get_compliance_template_name(context['agreement_compliance_type']))

        # replace placeholders in the template with actual values
        content = content.substitute(**context)
        # return html context

        # html temporary file
        html_file_name = f'{context["_id"].replace("-", "_").upper()}_{datetime_format}.html'
        html_tmp_path = os.path.join('/tmp/', html_file_name)

        # create html tmp file
        with open(html_tmp_path, "w") as html_tmp_file:
            html_tmp_file.write(content)

            #PERMIT READ FILE
            try:
                os.chmod(html_tmp_path, 0o777)
            except Exception as e:
                print(str(e))
            #END PERMIT READ FILE



        #Define path to wkhtmltopdf.exe
        path_to_wkhtmltopdf = "/usr/local/bin/wkhtmltopdf"


        #Point pdfkit configuration to wkhtmltopdf.exe
        config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

        #Convert HTML file to PDF
        pdfkit.from_file(html_tmp_path, output_path=file_path, configuration=config)



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


    