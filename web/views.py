from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
import json

# Create your views here.
def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)

def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)


def portfolio(request):
    context = {"is_portfolio": True}
    return render(request, "web/portfolio.html", context)

def update(request):
    context = {"is_update": True}
    return render(request, "web/blog.html", context)

def service(request):
    context = {"is_service": True}
    return render(request, "web/service.html", context)
