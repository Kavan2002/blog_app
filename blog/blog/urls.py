"""blog URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from users import views as user_view

# here we use login and logout functionality given by django itself
urlpatterns = [
                  path('register', user_view.register, name="register"),  # register user
                  path('profile', user_view.profile, name='profile'),  # showing profile
                  path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
                  path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
                  path('password-reset',
                       auth_views.PasswordResetView.as_view(template_name='users/Password_reset.html'),
                       name='password-reset'),
                  path('password-reset/done',
                       auth_views.PasswordResetDoneView.as_view(template_name='users/Password_reset_done.html'),
                       name='password-reset-done'),

                  path('', include('blog_app.urls')),  # post related urls
                  path('admin/', admin.site.urls, name='admin'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# document_root = every img , document , js , jquery
