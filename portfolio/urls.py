
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home,name='home_page'),
    path('blog/',include ('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
