from django.shortcuts import render


def home(request):
    return render(request,"abcd/base.html")
def text(request):
    return render(request, "abcd/text.html")