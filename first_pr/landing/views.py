from django.shortcuts import render
from .forms import subscriberForm, subscriberName
import random

def landing(request):
    n1 = "1"
    n2 = "2"
    n3 = "3"
    name = "dfg"
    form = subscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():  # is valid  for cleaned data
        print(request.POST)
        d = form.cleaned_data
        print(d)
        data = d['name']
        print(data)
        new_form = form.save()

    form2 = subscriberName(request.POST or None)
    if request.method == "POST" and form2.is_valid():  # is valid  for cleaned data

        n1 = 10
        n2 = random.choice(subscriberName.name.all())
        n3 = random.choice(subscriberName.name.all())

    return render(request, 'landing/landing.html', locals())
