import os
import datetime
from django.conf import settings
from utils.general import read_template, get_compliance_template_name


def create_pdf_document(context:dict):
    new_filename = ""
    try:
        # wkhtmltopdf package install Reference
        # https://computingforgeeks.com/install-wkhtmltopdf-on-ubuntu-debian-linux/

        # Get storage path
        # /home/100080/100080-dowelllegalzard/vol/web
        root_path = os.path.join(settings.MEDIA_ROOT, 'documents/')


        # get new filename
        datetime_format=datetime.datetime.now().strftime("%m%d%Y%H%M%S")
        new_filename=f'{context["_id"].replace("-", "_").upper()}_{datetime_format}.PDF'
        file_path = f'{root_path}{new_filename}'


        # load commpliance template from the filesystem
        # content = read_template(get_compliance_template_name(context['agreement_compliance_type']))

        # replace placeholders in the template with actual values
        # content = content.substitute(**context)
        # return html context

        # html temporary file
        # html_file_name = f'{context["_id"].replace("-", "_").upper()}_{datetime_format}.html'
        # html_tmp_path = os.path.join('/tmp/', html_file_name)

        # create html tmp file
        # with open(html_tmp_path, "w") as html_tmp_file:
        #     html_tmp_file.write(content)

        #     #PERMIT READ FILE
        #     try:
        #         os.chmod(html_tmp_path, 0o777)
        #     except Exception as e:
        #         print(str(e))
            #END PERMIT READ FILE



        # Define path to wkhtmltopdf
        # path_to_wkhtmltopdf = "/usr/local/bin/wkhtmltopdf"


        # Point pdfkit configuration to wkhtmltopdf.exe
        # config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

        # Convert HTML file to PDF
        # pdfkit.from_file(html_tmp_path, output_path=file_path, configuration=config)


        template_name = f"agreement-compliance/{get_compliance_template_name(context['agreement']['agreement_compliance_type'])}"
        from django.template.loader import get_template
        template =get_template(template_name)
        html=template.render(context)

        from utils.render_html_to_pdf import generate_pdf
        return generate_pdf(sourceHtml=html, outputFilename=file_path)



        # # PERMIT READ FILE
        # try:
        #     os.chmod(file_path, 0o777)
        # except Exception as e:
        #     print(str(e))
        # # END PERMIT READ FILE

    except Exception as e:
        print("error message")
        print(str(e))
    return new_filename



    