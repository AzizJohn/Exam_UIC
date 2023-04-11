from django.urls import path, include

urlpatterns = [
    path('task1/', include('apps.task1.urls')),
    path('task2/', include('apps.task2.urls')),
    path('task3/', include('apps.task3.urls')),
]
