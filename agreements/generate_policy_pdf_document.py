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
        new_filename=f'{context["_id"].replace("-", "_").upper()}_{datetime_format}"_.PDF'
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
            print(str(e))

    return new_filename        


    