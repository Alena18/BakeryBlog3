from . import views
from django.urls import path, include
from .views import BlogPost, BlogDetail, BlogHeart, TipPost, TipDetail
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_details'),
    path('recipes.html', views.BlogPost.as_view(), name='recipes'),
    path('tips/<slug:slug>', views.TipDetail.as_view(), name='tip_details'),
    path('tips.html', views.TipPost.as_view(), name='tips'),
    path('sign_up.html', views.sign_up, name='sign_up'),
    path('sign_upconfirm.html', views.confirm, name='confirm'),
    path('connect.html', views.connect, name='connect'),
    path('askconfirm.html', views.askconfirm, name='askconfirm'),
    path('blog_details.html', views.blog_details, name='blog_details'),
    path('like/<slug:slug>', views.BlogHeart.as_view(), name='blog_hearts'),
    path('profile.html', views.profile, name='profile'),
    path('delete_comment/<int:id>', views.delete_comment,
         name='delete_comment'),
    ]
