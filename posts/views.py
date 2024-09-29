from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render, redirect
from posts.forms import PostForm, CommentForm, searchForm
from posts.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

def main_page_view(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def post_list_view(request):
    form = searchForm(request.GET)
    posts = Post.objects.all()

    search = request.GET.get('search')
    tags = request.GET.getlist('tags')
    ordering = request.GET.get('ordering')

    # Поиск по заголовку и контенту
    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))

    # Фильтрация по тегам
    if tags:
        posts = posts.filter(tags__in=tags).distinct()

    # Сортировка
    if ordering:
        posts = posts.order_by(ordering)

    # Пагинация
    paginator = Paginator(posts, 3)  # Показываем по 3 поста на странице
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {'posts': posts, 'form': form, 'max_pages': range(1, paginator.num_pages + 1)}
    return render(request, "posts/post_list.html", context=context)


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            Comment.objects.create(post=post, text=text)
            return redirect(f"/posts/{post_id}/")

    return render(request, "posts/post_detail.html", context={"post": post, "form": form, "comments": comments})


@login_required()
def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/post_create.html", context={"form": form})

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/posts/")
    return render(request, "posts/post_create.html", context={"form": form})
