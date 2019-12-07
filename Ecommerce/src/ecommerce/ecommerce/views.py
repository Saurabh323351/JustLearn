from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def home_page(request):

    return render(request,'home_page.html',{})

def contact_us(request):

    form=ContactForm(request.POST or None)
    if form.is_valid():

        print(form.cleaned_data)
    context={"title":"contact su page",
             "form":form}

    return render(request,'contact/view.html',context)