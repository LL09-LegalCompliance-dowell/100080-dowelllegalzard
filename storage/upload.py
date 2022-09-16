from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import uuid
from PIL import Image


def optimise_upload_img(file_path, extension):
    try:
        img_extension_list = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff']

        extension = extension.lower().replace(".", "")
        if extension in img_extension_list:
            img = Image.open(file_path)
            # Reduce the size of the image
            img.save(file_path, optimize=True, quality=65)

        # PERMIT READ FILE
        try:
            os.chmod(file_path, 0o777)
        except Exception as e:
            print(str(e))
        # END PERMIT READ FILE

    except Exception as e:
        print(str(e))
        return False

    else:
        return True


def upload_img(file):
    """Save image and optimize the size of the image
       return (filename, actual_filename, file_extension, file_path)
    """
    file_path = ""
    actual_filename = ""
    new_filename = ""
    file_extension = ""
    try:
        # Get file extension
        file_extension = file.name.split(".")[1].lower()
        # Get storage path
        root_path = os.path.join(settings.MEDIA_ROOT, 'images/')

        actual_filename = file.name

        # Build file path
        root_path = root_path.replace("\\", "/")
        new_filename = f'img_{uuid.uuid4()}.{file_extension}'
        file_path = f"{root_path}{new_filename}"

        # Save file
        fs = FileSystemStorage(location=root_path)
        fs.save(new_filename, file)

        # PERMIT READ FILE
        try:
            os.chmod(file_path, 0o777)
        except Exception as e:
            print(str(e))
        # END PERMIT READ FILE

        # Optimize the size of the image
        optimise_upload_img(file_path, file_extension)

    except Exception as e:
        print(str(e))
        return {}

    else:
        return {
            "file_data": {
                "filename": new_filename,
                "actual_filename": actual_filename,
                "file_extension": file_extension,
                "file_path": file_path
            }
        }
