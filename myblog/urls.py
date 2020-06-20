from django.contrib import admin
from django.urls import path, include, re_path
from blog import views as blog_view
from . import settings
from django.views.static import serve

urlpatterns = [
    path('', blog_view.Index.as_view()),
    path('admin/', admin.site.urls), path('upload/', blog_view.image_upload),
    path('search/', blog_view.Search.as_view(), name='search'),
    path('comment/', blog_view.pub_comment, name='comment'),
    path('category/<int:category>', blog_view.CategoryList.as_view(), name='category'),
    path('detail/<int:pk>', blog_view.ArticleDetail.as_view(), name='detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})

]
