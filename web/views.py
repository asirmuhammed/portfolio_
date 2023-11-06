from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)

def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)


def contact(request):
    context = {"is_contact": True}
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
