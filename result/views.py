from django.shortcuts import render


def result(request):
    return render(request, 'result/result_page.html')
