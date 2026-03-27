from django.shortcuts import render


def home_views(request):
    return render(request, 'home_page/index.html')
