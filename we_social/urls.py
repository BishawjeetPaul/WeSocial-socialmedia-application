from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(next_page='login-view'), name='logout-view'),
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home-view'),
    # Django all-auth.
    # path('accounts/', include('allauth.urls')),
    # profiles app urls.
    path('profiles/', include('profiles.urls', namespace='profiles')),
    # posts app urls.
    path('posts/', include('posts.urls', namespace='posts')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
