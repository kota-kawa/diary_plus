from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Entry

# placeholder signal to keep the app from failing on import
@receiver(post_save, sender=Entry)
def entry_saved(sender, instance, **kwargs):
    """Ensure HTML body is in sync when saving via admin."""
    if not instance.body_html:
        instance.body_html = instance.body_md
        instance.save()

