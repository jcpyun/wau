from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from .models import click
from .forms import clickForm

# Create your views here.
def home(request):
    form=clickForm(request.POST or None)
    print form
    if form.is_valid():
        save_it= form.save(commit=False)
        save_it.save()
    #instance= get_object_or_404(click, id=1)
    # instance= click.objects.get(id=1)
    queryset = click.objects.all()
    test = click.objects.all()
    yolo= test[:1]
    print yolo[0]
    template= "home.html"
    context={
        "object_list": queryset,
        "cur": yolo[0]
    }
    return render(request, template, context)