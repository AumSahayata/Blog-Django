from django.urls import path
from . import views

urlpatterns = [
    path("",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("home",views.index,name="index"),
    path("logout",views.logout,name="logout"),
    path("new_post",views.new_post,name="new_post"),
    path("my_posts",views.my_posts,name="my_posts"),
    path("post/<int:post_id>",views.view_post,name="view_post"),
    path("edit_post/<int:post_id>",views.edit_post,name="edit_post"),
    path("delete_post/<int:post_id>",views.delete_post,name="delete_post"),
]