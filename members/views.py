from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MemberForm
from .models import Member


def home(request):
    return render(request, "home.html")


def members_list(request):
    verified_members = Member.objects.filter(verified=True).order_by("name")
    return render(request, "members_list.html", {"members": verified_members})


def member_detail(request, slug):
    member = get_object_or_404(Member, slug=slug)
    return render(request, "member_detail.html", {"member": member})


def member_form(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.verified = False  # New members start unverified
            member.save()
            messages.success(
                request,
                "Thank you for registering, your submission will be verified by one of our admins soon.",
            )
            return redirect("members_list")
    else:
        form = MemberForm()

    return render(request, "member_form.html", {"form": form})
