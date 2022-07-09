from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from blog_app.custom_mixin import RedirectMixin
from blog_app.models import Post, transaction
from .models import Post


# Create your views here.
# here we have to use login mixin coz only registered users can add post after login
# @login_required decorator is not for class it only use in methods
# we also use userPassesTest mixing coz post can be updated by whose who wrote not by everyone

class adminroleRequireMixin(RedirectMixin):
    def test_func(self):
        if self.request.user.profile.role == 'admin':
            return True
        else:
            return False

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    # def get_queryset(self):
    #     # user = get_object_or_404(User,)
    #     return Post.objects.filter(author=self.request.user).order_by('-date_posted')


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # <app>/<model>_<view_type>.html
    # context_object_name = 'posts'
    # ordering = ['-date_posted ']


class PostCreateView(adminroleRequireMixin, LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'  # <app>/<model>_<view_type>.html
    fields = ['title', 'content']
    redirect_url = '/logout'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  # <app>/<model>_<view_type>.html
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # <app>/<model>_<view_type>.html
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'data': 'about us'})


    # in function based view we have to render a specific function  and call explicitly
    # in class view we just override the variable values according to need


@receiver(post_save, sender=Post)
def create_log(sender, instance, created, **kwargs):
    if created:
        print(instance.__class__.__name__)
        # print(sender.title)
        transaction_vo = transaction()
        transaction_vo.transaction_status = True
        transaction_vo.transaction_model_name = sender.__class__.__name__
        transaction_vo.transaction_description = "inserted blog " + instance.title + " sucessfully"
        transaction_vo.transaction_user_id = instance.author
        transaction_vo.save()
        print("transaction saved...")


@receiver(post_delete, sender=Post)
def create_log_delete(sender, instance, **kwargs):
    # if created:
    # print(instance.__class__.__name__)
    # print(sender.title)
    transaction_vo = transaction()
    transaction_vo.transaction_status = True
    transaction_vo.transaction_model_name = "blog_app"
    transaction_vo.transaction_description = "deleted blog sucessfully"
    transaction_vo.transaction_user_id = instance.author

    transaction_vo.save()
    print("transaction saved of delete ...")
