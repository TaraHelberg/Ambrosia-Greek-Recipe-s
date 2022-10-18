from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin management from Admin Panel
    Used & Modified from I think therefore I blog
    Credit to Code Institute
    """
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'ingredients', 'description']
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    summernote_fields = ('description', 'serves', 'prep_time', 'cooking_time',
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
