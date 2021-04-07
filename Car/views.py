from .models import Car
from .serializers import CarSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework.permissions import IsAuthenticated

class CarRentalView(ListModelMixin, CreateModelMixin, GenericAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' not in kwargs:
            return self.list(request, *args, *kwargs)
        car = Car.objects.get(pk=kwargs['pk'])
        serializer = CarSerializer(car)
        return Response({"Car" : serializer.data})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
    def put(self, request, pk):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(model, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car = get_object_or_404(self.queryset, pk=pk)
        car.delete()
        return Response({"message": f"Car with id {pk} has been deleted."},status=204)