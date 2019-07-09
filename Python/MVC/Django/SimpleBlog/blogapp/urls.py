from django.urls import path

from blogapp.views import index, create_blog, single_blog, logout_view


urlpatterns = [

    path('blog/', index, name="home"),
    path('blog/<int:blog_id>/', single_blog, name="blog"),
    path('create/', create_blog, name ="create"),
    path('logout/', logout_view, name="logout"),

]