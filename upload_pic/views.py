from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .src.ChooseEffectRadioForm import radio_list
from .src.UploadImageForm import UploadImageForm
from .src.EffectType import EffectType


def upload_pic(request):
    if request.method == 'POST':
        file_storage = FileSystemStorage()
        chosen_option = request.POST['pref-effect']
        uploaded_image = request.FILES['image_field']

        file_name = file_storage.save(uploaded_image.name, uploaded_image)

        # modify file

        context = {
            'title': 'Wynik',
            'image_url': file_storage.url(file_name),
            'effect_type': EffectType.__members__[chosen_option].value[0],
        }
    else:
        context = {
            'title': 'Witaj!',
            'upload_image_form': UploadImageForm(),
            'effects_radio_list': radio_list,
        }

    return render(request, 'upload_pic/homepage.html', context)
