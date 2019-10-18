from django.shortcuts import render, redirect
from screening.models import Screening
from screening.forms import ScreeningForm
from django.contrib import messages


def screening(request):
    if request.method == "POST":
        form = ScreeningForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, "Record created successful")
        return redirect("screening")
    else:
        return render(request, "screening.html", {})
