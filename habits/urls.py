import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.WeekScores.as_view()),
    path('__debug__/', include(debug_toolbar.urls)),
]