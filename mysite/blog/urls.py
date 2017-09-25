from django.conf.urls import url
from . import views
from . api import PostApi, CommentApi

app_name = 'post'

urlpatterns = [
    url(r'^$',views.PostListView.as_view(), name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/edit/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'^draft/$',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comments_to_post, name='add_comments_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post$',PostApi.as_view()),
    url(r'^comment$',CommentApi.as_view()),
]
