from django.shortcuts import render

# Create your views here.
def vistaPrincipal(request):
    return render(request, 'base/base.html')
 