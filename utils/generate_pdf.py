# Referencem link: https://pypi.org/project/pyhtml2pdf/
from pyhtml2pdf import converter
from storage.path import get_storage_path
from django.conf import settings
import os



def generate(
    html_file_abs_path_or_url:str,
    pdf_file_name:str,
    generate_from_web:bool = False
    ):

    """
        Generate PDF document using html document on the host machine
        or html document from specific url
    """
    
    # path = os.path.abspath('index.html')

    try:

        if generate_from_web:
            converter.convert(
                html_file_abs_path_or_url, 
                f'{get_storage_path(settings.DEBUG)}/media/documents/{pdf_file_name}.pdf')
        else:

            converter.convert(
                f'file:///{html_file_abs_path_or_url}', 
                f'{get_storage_path(settings.DEBUG)}/media/documents/{pdf_file_name}.pdf')


        return True
    except Exception as err:
        print(str(err))
        return False