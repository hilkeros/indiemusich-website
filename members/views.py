from django.shortcuts import get_object_or_404, render

from .models import Member


def home(request):
    return render(request, "home.html")


def members_list(request):
    verified_members = Member.objects.filter(verified=True).order_by("name")
    return render(request, "members_list.html", {"members": verified_members})


def member_detail(request, slug):
    member = get_object_or_404(Member, slug=slug)
    return render(request, "member_detail.html", {"member": member})
