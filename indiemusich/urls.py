"""
URL configuration for indiemusich project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from blog.views import post_detail, spotlight_post
from django.contrib import admin
from django.urls import path
from links.views import links_list
from members.views import home, member_detail, member_form, members_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home_page"),
    path("members/", members_list, name="members_list"),
    path("members/form/", member_form, name="member_form"),
    path("members/<slug:slug>/", member_detail, name="member_detail"),
    path("about/", spotlight_post, name="about_page"),
    path("blog/<slug:slug>/", post_detail, name="post_detail"),
    path("resources/", links_list, name="links_list"),
]
