from django.test import TestCase
from django.contrib.auth.models import User
from .models import Entry

class EntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("alice", password="pwd")
    def test_markdown_conversion(self):
        e = Entry.objects.create(author=self.user, title="t", body_md="**bold**")
        self.assertIn("<strong>bold</strong>", e.body_html)
