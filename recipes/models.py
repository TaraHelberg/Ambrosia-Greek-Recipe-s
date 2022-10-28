from django.db import models
from django.template.defaultfilters import slugify
from django_unique_slugify import unique_slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """
    Model for the Post Recipe
    Used & Modified from I think therefore I blog
    Credit to Code Institute
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="recipe_posts")
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    description = models.TextField(blank=True, help_text="Describe The Recipe")
    serves = models.CharField(blank=True, max_length=20)
    prep_time = models.CharField(blank=True, max_length=20)
    cooking_time = models.CharField(blank=True, max_length=20)
    ingredients = models.TextField()
    method = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes',
                                   blank=True)

    class Meta:
        """
        Orders the recipes in Descending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string method "AKA :The Magic method""
        """
        return str(self.title)

    def amount_of_likes(self):
        """
        Shows the number of likes on a recipe.
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        """
        Generate unique slug
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Add a comment.
    Used from I think therefore I blog
    Credit to Code Institute
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Orders the comments in Ascending order.
        """
        ordering = ['created_on']

        def __str__(self):
            return f"Comment {self.body} by {self.name}"
