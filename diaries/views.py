from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponseBadRequest
from django_htmx.http import HttpResponseClientRedirect
from .models import Entry
from .forms import EntryForm

class EntryListView(ListView):
    model = Entry
    paginate_by = 5
    template_name = "diaries/entry_list.html"
    context_object_name = "entries"

class EntryDetailView(DetailView):
    model = Entry
    template_name = "diaries/entry_detail.html"

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    template_name = "diaries/entry_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        if self.request.htmx:  # オートセーブ返却
            return HttpResponseClientRedirect(self.object.get_absolute_url())
        return response

class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = "diaries/entry_form.html"

    def test_func(self):
        return self.get_object().author == self.request.user

def toggle_like(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "login required"}, status=403)
    entry = get_object_or_404(Entry, pk=pk)
    liked = False
    if entry.likes.filter(pk=request.user.pk).exists():
        entry.likes.remove(request.user)
    else:
        entry.likes.add(request.user)
        liked = True
    if request.htmx:
        return render(request, "diaries/tag_list_partial.html", {"entry": entry})
    return JsonResponse({"liked": liked, "count": entry.likes.count()})

def tagged_list(request, tag):
    entries = Entry.objects.filter(tags__name__iexact=tag)
    return render(request, "diaries/entry_list.html", {"entries": entries, "tag": tag})

def search(request):
    q = request.GET.get("q", "")
    entries = Entry.objects.filter(Q(title__icontains=q) | Q(body_md__icontains=q))
    return render(request, "diaries/entry_list.html", {"entries": entries, "query": q})
