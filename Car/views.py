from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .serializers import CarSerializer

from .models import Car

class CarView(APIView):
    """
    Rental Car API
    """
    permission_classes = (IsAuthenticated,)   
    def get(self, request, pk=None):
        try:
            if pk != None:
                car = Car.objects.get(_id=pk)
                serializer = CarSerializer(car)
                return Response({"cars": serializer.data})
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response({"cars": serializer.data})
        except Exception as e:
                return Response({"message": f'{e}'}, status =  status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        car = request.data.get('car')
        serializer = CarSerializer(data=car)
        if serializer.is_valid(raise_exception=True):
            try:
                car_saved = serializer.save()
            except Exception as e:
                return Response({"message": f'{e}'}, status =  status.HTTP_400_BAD_REQUEST)
        return Response({"success": "Car '{}' created successfully".format(car_saved._id)})

    def put(self, request, pk):
        saved_car = get_object_or_404(Car.objects.all(), _id=pk)
        data = request.data.get('car')
        serializer = CarSerializer(instance=saved_car, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_saved = serializer.save()
        return Response({"success": "Car '{}' updated successfully".format(saved_car._id)})

    def delete(self, request, pk):
        try:
            car = get_object_or_404(Car.objects.all(), _id=pk)
            car.delete()
            return Response({"message": "Car with id `{}` has been deleted.".format(pk)},status=204)
        except Exception as e:
            return Response({"message": f'{e}'}, status =  status.HTTP_400_BAD_REQUEST)


