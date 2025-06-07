from django.urls import path
from . import views

urlpatterns = [
    path("", views.EntryListView.as_view(), name="entry_list"),
    path("entry/new/", views.EntryCreateView.as_view(), name="entry_new"),
    path("entry/<int:pk>/", views.EntryDetailView.as_view(), name="entry_detail"),
    path("entry/<int:pk>/edit/", views.EntryUpdateView.as_view(), name="entry_edit"),
    path("entry/<int:pk>/like/", views.toggle_like, name="entry_like"),
    path("tag/<slug:tag>/", views.tagged_list, name="tag_list"),
    path("search/", views.search, name="entry_search"),
]
