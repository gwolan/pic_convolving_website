from django.shortcuts import render
from .src.EffectType import EffectType


def upload_pic(request):
    context = {
        'title': 'Witaj!',
        'effects': EffectType.__members__,
    }

    return render(request, 'upload_pic/homepage.html', context)
