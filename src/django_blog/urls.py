from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blog import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', blog_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('', include('blog.urls')),
]


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)