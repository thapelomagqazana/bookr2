"""bookr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
# from bookr import reviews.views
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('books/', views.book_list,
         name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    # path('', include('reviews.urls')),
    # path('', reviews.views.index),
    path('book-search', views.book_search, name='book_search'),
    path("publishers/<int:pk>/", views.publisher_edit, name="publisher_edit"),
    path("publishers/new/", views.publisher_edit, name="publisher_create"),
    path("books/<int:book_pk>/reviews/new/",
         views.review_edit, name="review_create"),
    path("books/<int:book_pk>/reviews/<int:review_pk>",
         views.review_edit, name="review_edit"),
]
