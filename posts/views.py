from django.shortcuts import render, redirect
from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment


def main_page_view(request):
    return render(request, 'home.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})


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


def post_create_view(request):
    global form
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/post_create.html", context={"form": form})

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/posts/")
    return render(request, "posts/post_create.html", context={"form": form})

# Create your views here.
