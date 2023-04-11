from django.db.models import Sum
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.task3.models import Car


class CarDetail(APIView):

    def get(self, request, pk, *args, **kwargs):
        car = get_object_or_404(Car.objects.all(), id=pk)
        mark = car.mark

        sum_price = mark.cars.aggregate(Sum('price'))
        avg_price = sum_price['price__sum'] / mark.cars.count()

        difference_price = car.price - avg_price
        difference_percentage = difference_price / avg_price * 100
        stat_percentage = car.price / avg_price * 100

        data = {
            "difference_price": difference_price,
            "difference_percentage": difference_percentage,
            "stat_percentage": stat_percentage,
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )


__all__ = ['CarDetail']
