# links/views.py

from django.shortcuts import render

from .models import LINK_CATEGORIES, Link


def links_list(request):
    atproto_links = Link.objects.filter(category=LINK_CATEGORIES["ATProto"]).order_by(
        "created_at"
    )
    fediverse_links = Link.objects.filter(
        category=LINK_CATEGORIES["Fediverse"]
    ).order_by("created_at")
    openweb_links = Link.objects.filter(category=LINK_CATEGORIES["Open Web"]).order_by(
        "created_at"
    )

    context = {
        "atproto_links": atproto_links,
        "fediverse_links": fediverse_links,
        "openweb_links": openweb_links,
    }
    return render(request, "resources.html", context)
