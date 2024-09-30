from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from posts.views import MainPageView, PostListView, PostDetailView, PostCreateView, PostUpdateView
from django.conf.urls.static import static
from user.views import register_view, login_view, logout_view, profile

urlpatterns = [
                  path('', MainPageView.as_view(), name='home'),
                  # Используем классовое представление для главной страницы
                  path('login/', login_view, name='login'),
                  path('logout/', logout_view, name='logout'),
                  path("register/", register_view, name="register"),
                  path('admin/', admin.site.urls),

                  # Посты
                  path('posts/', PostListView.as_view(), name="posts"),  # Список постов через ListView
                  path("posts/<int:post_id>/", PostDetailView.as_view(), name="post_detail"),
                  # Детализация поста через DetailView
                  path("posts/create/", PostCreateView.as_view(), name="post_create"),
                  # Создание поста через CreateView
                  path('posts/<int:post_id>/update/', PostUpdateView.as_view(), name="post_update"),
                  # Обновление поста через UpdateView

                  path("profile/", profile, name="profile"),
                  path('', include('parser.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
