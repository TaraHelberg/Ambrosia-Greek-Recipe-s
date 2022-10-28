from .models import Comment, Recipe
from django_summernote.widgets import SummernoteWidget
from django import forms


class CommentForm(forms.ModelForm):
    """
    Add a Comment Form
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Add a Recipe Form
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'serves',
            'prep_time',
            'cooking_time',
            'ingredients',
            'method',
            'featured_image',
        ]

        widgets = {
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(RecipeForm, self).__init__(*args, **kwargs)
