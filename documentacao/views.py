from django.shortcuts import render

def metodo(request):
    return render(request, 'documentacao/index.html')