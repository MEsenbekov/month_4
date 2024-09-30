from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm, searchForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPageView(TemplateView):
    template_name = 'home.html'


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3  # Пагинация: 3 поста на странице
    login_url = 'login'

    def get_queryset(self):
        queryset = Post.objects.all()
        search = self.request.GET.get('search')
        tags = self.request.GET.getlist('tags')
        ordering = self.request.GET.get('ordering')

        # Поиск по заголовку и контенту
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))

        # Фильтрация по тегам
        if tags:
            queryset = queryset.filter(tags__in=tags).distinct()

        # Сортировка
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = searchForm(self.request.GET)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        context['form'] = form
        context['max_pages'] = range(1, paginator.num_pages + 1)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = self.get_object()
        if form.is_valid():
            text = form.cleaned_data.get("text")
            Comment.objects.create(post=post, text=text)
        return redirect(f"/posts/{post.id}/")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('post_list')  # Redirect после успешного создания
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_update.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('post_list')  # Redirect после успешного обновления
    login_url = 'login'
