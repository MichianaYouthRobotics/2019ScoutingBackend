from django.shortcuts import render, redirect
from scouts.forms import ScoutForm
from scouts.models import Scout


# Create your views here.
def scout_form(request):
    first_name = 'Pierce'
    if request.method == 'POST':
        my_form = ScoutForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect('thanks')
    else:
        my_form = ScoutForm()
    return render(request, 'myapp/scout_form.html', {'first_name': first_name,
                                               'my_form': my_form})


def scout_thanks(request):
    first_name = 'Pierce'
    return render(request, 'myapp/thanks.html', {'first_name': first_name})


def scout_all(request):
    all_scouts = Scout.objects.all()
    return render(request, 'myapp/all.html', {'all_scouts': all_scouts})

