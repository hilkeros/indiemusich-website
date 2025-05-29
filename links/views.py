# links/views.py

from django.shortcuts import render

from .models import Link  # Import the Link model we defined earlier


def links_list(request):
    """
    View to display a list of all links.
    """
    # Retrieve all Link objects from the database, ordered by link_text as defined in the model's Meta.
    # If you wanted a different order here, you could specify it, e.g., Link.objects.all().order_by('-created_at')
    links = Link.objects.all().order_by("created_at")

    # Pass the retrieved links to the template context
    context = {"links": links}

    # Render the link_list.html template, passing the links data to it
    return render(request, "resources.html", context)
