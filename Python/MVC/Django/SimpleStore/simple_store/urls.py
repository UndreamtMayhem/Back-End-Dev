from store import urls as appurls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(appurls)),
    path('admin/', admin.site.urls),
]


