"""libreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views
from store.urls import store_patterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('about/', views.about, name="about"),
    path('pricing/', views.pricing, name="pricing"),
    path('faq/', views.faq, name="faq"),
    path('blog-home/', views.bloghome, name="blog-home"),
    path('blog-post/', views.blogpost, name="blog-post"),
    path('portfolio-item/', views.portfolioitem, name="portfolio-item"),
    path('portfolio-overview/', views.portfoliooverview, name="portfolio-overview"),
    path('contact/', include('contact.urls')),
    path('store/', include(store_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('page/', include('pages.urls')),
    # Aumentar la lista de posibles urls en la raiz de la aplicación
    path('accounts/', include('registration.urls')),
    # Social Auth
    path('social-auth/', include('social_django.urls', namespace="social")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
