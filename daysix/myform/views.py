from django.shortcuts import render
from django.http import HttpResponse
from.forms import ContactForm ,FeedbackForm

def feedback(request):
    form = FeedbackForm(request.POST  or None)
    if form.is_valid():
        # process form.cleaned_data
        print(form.cleaned_data)
        form.save()
        return render(request, 'mypage/feedback.html')
    
    context = {
        "form":form
    }
    return render(request,"myform/feedback.html", context)

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # process form.cleaned_data
        print(form.cleaned_data)
        return render(request, 'myform/thankyou.html')
    
    context = {
        "form":form
    }
    return render(request,"myform/form.html", context)
    