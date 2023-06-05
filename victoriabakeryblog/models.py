import readtime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0,"Draft"), (1, "Published"))

class RecipePost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField(blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    read_time = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)    
    status = models.IntegerField(choices=STATUS, default=0)
    hearts = models.ManyToManyField(
        User, related_name='blogpost_hearts', blank=True)


    def read_time(self):
      result = readtime.of_text(self.content)
      return result.text
    
    def number_of_hearts(self):
        return self.hearts.count()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class UserComment(models.Model):
    blog = models.ForeignKey(RecipePost, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
            related_name="comments", null=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

class Tips(models.Model):

    class Meta:
        verbose_name_plural = "Tips"

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tips"
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

class TipComments(models.Model):
    
    class Meta:
        verbose_name_plural = "TipComments"
        
    post = models.ForeignKey(Tips, on_delete=models.CASCADE,
                             related_name="tcomments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
            related_name="tcomments", null=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
