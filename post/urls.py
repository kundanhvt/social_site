

from django.urls import path
from . import views
app_name='post'

urlpatterns = [
    path('',views.home,name='home_post'),
    path('create_post/',views.create_post,name='create_post'),
    path('view_my_post/',views.view_my_post,name='view_my_post'),
    path('view_all_post/',views.view_all_post,name='view_all_post'),
    path('create_post/post_submit',views.submit_post),
    path('comment/',views.add_comment, name='comment_post'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('like/',views.like, name='like'),
    path('dislike/',views.dislike, name='dislike'),
]

