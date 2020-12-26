from django.shortcuts import render
from .src.EffectType import EffectType


def upload_pic(request):
    supported_effects = list(EffectType.__members__.keys())

    context = {
        'title': 'Witaj!',
        'effects': EffectType.__members__,
        'checked': ' checked',
        'first_checkbox_value': EffectType.__members__[supported_effects[0]].value[1],
    }

    return render(request, 'upload_pic/homepage.html', context)
