from django.shortcuts import render
from .models import Familiars

# Create your views here.

def show_data(request):
    my_data = Familiars.objects.all()
    one_data = Familiars.objects.get(pk=1)
    context = {
        'my_data':my_data,
        'one_data':one_data,
    }

    return render(request, 'show_data.html', context=context)
