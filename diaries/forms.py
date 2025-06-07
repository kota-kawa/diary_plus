from django import forms
from .models import Entry
from taggit.forms import TagField, TagWidget

class EntryForm(forms.ModelForm):
    tags = TagField(required=False, widget=TagWidget(attrs={"class": "form-control"}))

    class Meta:
        model = Entry
        fields = ("title", "body_md", "cover_image", "tags")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body_md": forms.Textarea(attrs={"class": "form-control", "rows": 12}),
        }
