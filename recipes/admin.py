from django.contrib import admin
from .models import recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(recipe)
class recipeAdmin(SummernoteModelAdmin):
    """
    Admin management from Admin Panel
    Used & Modified from I think therefore I blog
    Credit to Code Institute
    """
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'ingredients', 'description']
    list_display = ('title', 'slug', 'status', 'create_on')
    list_filter = ('status', 'create_on')
    summernote_fields = ('description', 'prep_time', 'cooking_time',
                         'ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Adds comment field in admin panel
    Used from I think therefore I blog
    Credit to Code Institute
    """
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, querset):
        querset.update(approved=True)
