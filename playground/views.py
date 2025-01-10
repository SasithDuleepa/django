from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

# def say_hallo(request):
#     return HttpResponse('Hello World!')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ExampleModel
from .serializers import ExampleModelSerializer

class ExampleCreateView(APIView):
    def post(self, request):
        print(request.data)
        serializer = ExampleModelSerializer(data=request.data)
        if serializer.is_valid():
            print('serializer valid!')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('serializer not valid!')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        print(request.data)
        queryset = ExampleModel.objects.all()
        serializer = ExampleModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, request):
        instance = ExampleModel.objects.get(id=request.query_params['id'])
        serializer = ExampleModelSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        print(request.data)
        instance = ExampleModel.objects.get(id=request.data['id'])
        serializer = ExampleModelSerializer(instance, data=request.data)
        if serializer.is_valid():
            print('serializer valid!')
            serializer.update(instance, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        print(request.data)
        instance = ExampleModel.objects.get(id=request.data['id'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
