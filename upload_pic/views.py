from django.shortcuts import render, redirect
from .src.ChooseEffectRadioForm import radio_list
from .src.UploadImageForm import UploadImageForm


def upload_pic(request):
    context = {
        'title': 'Witaj!',
        'upload_image_form': UploadImageForm(),
        'effects_radio_list': radio_list,
    }

    if request.method == 'POST':
        return redirect('result_page')
    else:
        return render(request, 'upload_pic/homepage.html', context)
