from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


class Home(generic.TemplateView):
    """
    Home page view
    """
    template_name = "index.html"


class RecipeList(generic.ListView):
    """
    Browse All Recipes View
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'browse.html'
    paginate_by = 6


class RecipeDetail(DetailView):
    """
    Recipe see all Details View
    """
    def get(self, request, slug, *args, **kwargs):
        """Get response"""
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class RecipeLike(View):
    """
    Recipe Like's View
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class AddRecipe(CreateView):
    """
    Recipe Add View
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('browse')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Recipe Update View
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'update_recipe.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('browse')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UpdateView, self).form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Recipe Delete View
    """
    model = Recipe
    template_name = 'delete_recipe.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('browse')

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user


class UpdateComment(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Comment Update View
    """
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
    success_url = reverse_lazy('browse')

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return comment.name == self.request.user.username


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Commnet Delete View
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('browse')

    def test_func(self):
        comment = self.get_object()
        return comment.name == self.request.user.username
