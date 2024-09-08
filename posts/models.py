from datetime import timezone
from datetime import datetime
from django.db import models

"""
Posts.objects.all()
Posts.objects.filter(title = "Text")
Posts.objects.get(title = "Text")
Posts.objects.create(title = "Text", content = "Text", rate = 0)
"""


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
