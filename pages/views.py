from django.http import HttpResponse


def getPage(request):
    return HttpResponse(b"Hello world")
