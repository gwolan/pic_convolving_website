from django.shortcuts import render, redirect

context = {'text': 'Strona powstała jako projekt inżynierski do pracy dyplomowej. Celem jej powstania była chęć zastosowania nabytych umiejętności w praktyce oraz realizacja planowanego od dłuższego czasu projektu związanego z przetwarzaniem obrazów cyfrowych.\n\nSilnik graficzny jest napisany w języku C++. Jest to implementacja dwuwymiarowego filtra dyskretnego zdolnego do wykonywania splotów dyskretnych pikseli obrazów ze współczynnikami tegoż filtra. Algorytm oparty jest na splocie dyskretnym z definicji. Ze względu na zbyt dużą złożoność obliczeniową (pesymistycznie: O(n^5)) planowane jest rozszerzenie implementacji o szybką transformatę Fouriera (FFT).\n\nMożliwe też, że dodane zostaną jeszcze inne efekty graficzne niż obecnie wspierane. Silnik został napisany tak by umożliwić jego dalsze rozwijanie.'}

def about(request):
    if 'back' in request.GET:
        return redirect('upload_pic_homepage')
    else:
        return render(request, 'about/about.html', context)
