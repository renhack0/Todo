from django.shortcuts import render, redirect
from .models import *

def ishlar(request):
    if request.method == 'POST':
        Ishlar.objects.create(
            sarlafha=request.POST.get('s'),
            vaqt=request.POST.get('v'),
            batafsil=request.POST.get('b'),
            status=request.POST.get('s')
        )
        return redirect("/ishlar/")
    content = {
        "todos": Ishlar.objects.all(),
    }
    return render(request, 'todo_eski.html', content)

def todo_ochir(request, son):
    Ishlar.objects.filter(id=son).delete()
    return redirect("/ishlar/")


