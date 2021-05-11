from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
            # select only posts with status 'published'

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    # if someone deleted some Category all Post objects with this Category will be deleted
    # PROTECT won't allow to delete Category if Post objects with this Category exist
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    # CASCADE - if we delete user, all posts from this user will be deleted as well
    status = models.CharField(
        max_length=10, choices=options, default='published')

    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published', )
        # display the data in descending order based on published field

    def __str__(self):
        return self.title
