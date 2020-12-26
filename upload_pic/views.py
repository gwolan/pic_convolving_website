from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .src.ChooseEffectRadioForm import radio_list
from .src.UploadImageForm import UploadImageForm
from .src.EffectType import EffectType
from .src.FileRemover import FileRemover


file_remover = FileRemover()


def upload_pic(request):
    if request.method == 'POST':
        file_storage = FileSystemStorage()
        chosen_option = request.POST['pref-effect']
        uploaded_image = request.FILES['image_field']

        file_name = file_storage.save(uploaded_image.name, uploaded_image)
        file_url = file_storage.url(file_name)
        file_path = file_storage.path(file_name)

        # modify file

        context = {
            'title': 'Wynik',
            'image_url': file_url,
            'effect_type': EffectType.__members__[chosen_option].value[0],
        }
        file_remover.paths.put(file_path)
    else:
        context = {
            'title': 'Witaj!',
            'upload_image_form': UploadImageForm(),
            'effects_radio_list': radio_list,
        }

    return render(request, 'upload_pic/homepage.html', context)
