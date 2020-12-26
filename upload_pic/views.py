from django.shortcuts import render, redirect
from .src.EffectType import EffectType


def upload_pic(request):
    supported_effects = list(EffectType.__members__.keys())

    context = {
        'title': 'Witaj!',
        'effects': EffectType.__members__,
        'checked': ' checked',
        'first_checkbox_value': EffectType.__members__[supported_effects[0]].value[1],
    }

    if request.method == 'POST':
        return redirect('result_page')
    else:
        return render(request, 'upload_pic/homepage.html', context)
