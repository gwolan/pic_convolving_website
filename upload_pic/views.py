from django.shortcuts import render
from django.contrib import messages
from .src.ChooseEffectRadioForm import radio_list
from .src.UploadImageForm import UploadImageForm
from .src.Config import EffectType
from .src.Config import supported_types
from .src.FileRemover import FileRemover
from .src.ImageData import ImageData
from .src.ImageValidator import ImageValidator
import subprocess
import pic_convolving_website.settings


file_remover = FileRemover()


def get_homepage_context():
    return {'title': 'Witaj!',
            'upload_image_form': UploadImageForm(),
            'effects_radio_list': radio_list,
            'supported_types': supported_types, }


def get_result_context(image_url, effect_type):
    return {'title': 'Wynik',
            'image_url': image_url,
            'effect_type': effect_type, }


def upload_pic(request):
    if request.method == 'POST':
        image_data = ImageData(request.FILES['image_field'])
        image_validator = ImageValidator(image_data.image_path)
        chosen_option = request.POST['pref-effect']

        if image_validator.is_image_valid():
            # process_result = subprocess.run([pic_convolving_website.settings.MEDIA_ROOT + str("\\bin.exe"), "-p", image_data.image_path, "-f", image_validator.image.format.lower(), "-e", chosen_option])
            context = get_result_context(image_data.image_url, EffectType.__members__[chosen_option].value[0])
        else:
            messages.error(request, f'Wystąpił błąd: ' + image_validator.error)
            context = get_homepage_context()
        file_remover.paths.put(image_data.image_path)
    else:
        context = get_homepage_context()

    return render(request, 'upload_pic/homepage.html', context)
