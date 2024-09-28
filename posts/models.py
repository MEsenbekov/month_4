from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment on {self.post.title}: {self.text[:20]}'
