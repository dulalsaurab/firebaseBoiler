from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path
from backend import views as core
from authentication import views as auth
# from authentication import views as awt
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', core.home_page, name='home_page'),
    path('awt/', include('authentication.urls'), name="authentication"),
    path('article/', include('backend.urls'), name="articles"),

    # path('awt/', awt.login_page, name='login_page'),
    path('post/', core.post_page, name='post_page'),
    path('author/', core.author_profile, name='author_profile'),
    path('editor/', core.editor, name='editor_page'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url('', auth.postSingin, name='welcome page')
]
