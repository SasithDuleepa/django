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
        # serializer = ExampleModelSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


