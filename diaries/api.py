from rest_framework import routers, serializers, viewsets
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    class Meta:
        model = Entry
        fields = ["id", "title", "author", "body_html", "created_at", "tags"]

class EntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

router = routers.DefaultRouter()
router.register(r"entries", EntryViewSet)
urlpatterns = router.urls
