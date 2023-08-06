from django.db import models
from django.contrib.auth.models import User
from hitcount.models import HitCountMixin, HitCount
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from _data.zenblog_contents import CATEGORY

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=0)
    thumbnail = models.ImageField(upload_to='thumbnails', default='default.jpg')
    remarkable = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("zenblog:post_detail", kwargs={"slug": str(self.slug)})
