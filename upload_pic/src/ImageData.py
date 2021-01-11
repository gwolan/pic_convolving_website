from django.core.files.storage import FileSystemStorage
from .Config import MAX_FILE_SIZE_BYTES


class ImageData:
    file_storage = FileSystemStorage()

    def __init__(self, uploaded_image):
        if uploaded_image.size < MAX_FILE_SIZE_BYTES:
            self.is_file_saved = True
            self.image_name = self.file_storage.save(uploaded_image.name, uploaded_image)
            self.image_url = self.file_storage.url(self.image_name)
            self.image_path = self.file_storage.path(self.image_name)
        else:
            self.image_path = str("")
            self.is_file_saved = False

        self.image_size = uploaded_image.size
