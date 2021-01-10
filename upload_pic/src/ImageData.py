from django.core.files.storage import FileSystemStorage


class ImageData:
    file_storage = FileSystemStorage()

    def __init__(self, uploaded_image):
        self.image_name = self.file_storage.save(uploaded_image.name, uploaded_image)
        self.image_url = self.file_storage.url(self.image_name)
        self.image_path = self.file_storage.path(self.image_name)
        self.image_size = uploaded_image.size
