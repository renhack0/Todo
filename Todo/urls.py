from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ishlar/', ishlar),
    path('todo_ochir/<int:son>/', todo_ochir),
]
