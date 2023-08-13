from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # name = request.GET.get("name") or "world"
    # return HttpResponse("Hello, {}!".format(name))
    # name = "world"
    # return render(request, "base.html", {"name": name})
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})

