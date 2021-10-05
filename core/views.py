from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def faq(request):
    return render(request, 'core/faq.html')

def bloghome(request):
    return render(request, 'core/blog-home.html')

def blogpost(request):
    return render(request, 'core/blog-post.html')

def portfolioitem(request):
    return render(request, 'core/portfolio-item.html')

def portfoliooverview(request):
    return render(request, 'core/portfolio-overview.html')

# def store(request):
#     return render(request, 'core/store.html')

# def contact(request):
#     return render(request, 'core/contact.html')