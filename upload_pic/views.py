import subprocess, os
from django.shortcuts import render
from django.contrib import messages
from .src.ChooseEffectRadioForm import radio_list
from .src.UploadImageForm import UploadImageForm
from .src.Config import EffectType
from .src.Config import supported_types
from .src.Config import MAX_FILE_SIZE_MB
from .src.Config import engine_error_codes
from .src.FileQueueSupervisor import FileQueueSupervisor
from .src.FileToRemove import FileToRemove
from .src.ImageData import ImageData
from .src.ImageValidator import ImageValidator
import pic_convolving_website.settings as settings


file_queue_supervisor = FileQueueSupervisor()


def get_homepage_context():
    return {'title': 'Witaj!',
            'upload_image_form': UploadImageForm(),
            'effects_radio_list': radio_list,
            'supported_types': supported_types,
            'max_file_upload': MAX_FILE_SIZE_MB,}


def get_result_context(image_url, effect_type):
    return {'title': 'Wynik',
            'image_url': image_url,
            'effect_type': effect_type, }


def modify_image(request, image_validator, image_data, chosen_option):
    if image_validator.is_image_valid():
        process_result = subprocess.run(
            [os.path.join(settings.BASE_DIR, settings.config["EXECUTABLE_PATH"]), "-p", image_data.image_path,
                                                                                  "-f", image_validator.image.format.lower(),
                                                                                  "-e", chosen_option])

        file_queue_supervisor.files_queue.put(FileToRemove(image_data.image_path))
        if process_result.returncode == 0:
            return get_result_context(image_data.image_url, EffectType.__members__[chosen_option].value[0])
        else:
            messages.error(request, f'Wystąpił błąd: ' + engine_error_codes.get(process_result.returncode, "Nieznany błąd serwera"))
            return get_homepage_context()

    if image_data.is_file_saved:
        file_queue_supervisor.files_queue.put(FileToRemove(image_data.image_path))

    messages.error(request, f'Wystąpił błąd: ' + image_validator.error)
    return get_homepage_context()


def upload_pic(request):
    if request.method == 'POST':
        image_data = ImageData(request.FILES['image_field'])
        image_validator = ImageValidator(image_data)
        chosen_option = request.POST['pref-effect'] if request.POST['pref-effect'] != 'tga' else 'jpeg'

        context = modify_image(request, image_validator, image_data, chosen_option)
    else:
        context = get_homepage_context()

    return render(request, 'upload_pic/homepage.html', context)
