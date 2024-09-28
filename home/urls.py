from django.conf import settings
from django.contrib import admin
from django.urls import path
from posts.views import main_page_view, post_list_view, post_detail_view, post_create_view
from django.conf.urls.static import static
from user.views import register_view, login_view, logout_view

urlpatterns = [
    path('', main_page_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("register/", register_view, name="register"),  # Это правильный путь для регистрации
    path('admin/', admin.site.urls),
    path('posts/', post_list_view, name="posts"),
    path("posts/<int:post_id>/", post_detail_view, name="post_detail"),
    path("posts/create/", post_create_view, name="post_create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
