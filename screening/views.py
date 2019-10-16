from django.shortcuts import render, redirect
from screening.models import ScreeningForm
from screening.forms import ScreeningCrf
from django.contrib import messages


# Create your views here.

def screening(request):
    if request.method == 'POST':
        form = ScreeningCrf(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, 'Record created successful')
        return redirect('screening')
    else:
        return render(request, 'screening.html', {})
