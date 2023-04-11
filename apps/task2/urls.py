from django.urls import path

from apps.task2.views import ReviewCreate, ReviewDetail, ReviewList, ServiceListAV

urlpatterns = [
    path('service/<int:pk>/', ServiceListAV.as_view(), name="service--detail"),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'), # create review for specific service // creating review for specific service
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),  # specific service review list // all reviews for specific service
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')  # specific review

]
