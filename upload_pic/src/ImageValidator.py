import sys
from PIL.Image import open
from PIL.Image import UnidentifiedImageError


class ImageValidator:
    image_open = False
    error = None
    supported_types = ['jpeg', 'png']

    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def get_error_msg(self, exception):
        text, path, blank = str(exception).split('\'')

        if sys.platform == 'win32':
            file_name = path.split('\\')[-1]
        else:
            file_name = path.split('/')[-1]
        return text + '\'' + file_name + '\''

    def open_image(self):
        try:
            self.image = open(fp=self.image_path, mode='r')
            self.image_open = True
        except FileNotFoundError as fnfe:
            self.image_open = False
            self.error = 'ImageValidator exception FileNotFoundError: ' + self.get_error_msg(fnfe)
        except UnidentifiedImageError as uie:
            self.image_open = False
            self.error = 'ImageValidator exception UnidentifiedImageError: ' + self.get_error_msg(uie)
        except TypeError as te:
            self.image_open = False
            self.error = 'ImageValidator exception TypeError: ' + self.get_error_msg(te)
        except ValueError as ve:
            self.image_open = False
            self.error = 'ImageValidator exception ValueError: ' + self.get_error_msg(ve)
        except Exception as e:
            self.image_open = False
            self.error = 'ImageValidator exception UnknownException: ' + self.get_error_msg(e)

    def close_image(self):
        if self.image_open:
            self.image.close()

    def is_image_valid(self):
        self.open_image()

        if self.image_open:
            for supported_type in self.supported_types:
                if supported_type == self.image.format.lower():
                    self.close_image()
                    return True
            self.error = 'Format \'' + self.image.format.lower() + '\' nie jest wspierany.'
            self.close_image()
        return False