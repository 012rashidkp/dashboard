from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer,UserSerializer,LoginSerializer,ProductSerializer
from rest_framework.authtoken.models import Token
from django.contrib import auth
from .models import Task,Products
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/',
		'Create':'/task-create/',
		'Update':'/task-update/',
		'Delete':'/task-delete/',
		'Register':'/register/'
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
      if (request.method=="GET"):
	          tasks = Task.objects.all()
	          serializer = TaskSerializer(tasks, many=True)
	          response={
		      'error':False,
		      'datas':serializer.data
	          }
	          return Response(response)

class TaskDetail(APIView):
    serializer_class = TaskSerializer
    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                task = Task.objects.get(id=id)
                serializer = TaskSerializer(task)
                response={
                    "error":False,
                    "data":serializer.data
                }
        except:
            response={
                "error":True,
                "message":"datas not available"
            }

        return Response(response)



@api_view(['POST'])
def taskCreate(request):
        try:
            serializer=TaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Company Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Company Data"}
        return Response(dict_response)
  

class Taskupdate(APIView):
    serializer_class = TaskSerializer
    def post(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                queryset=Task.objects.all()
                task=get_object_or_404(queryset,id=id)
                serializer=TaskSerializer(task,data=request.data,context={"request":request})
                serializer.is_valid(raise_exception=True)
                serializer.save()
                response={
                    "error":False,
                    "message":"updated success"
                }
        except:
            response={
                "error":True,
                "message":"data updated failed"
            }

        return Response(response)



class TaskDelete(APIView):
    serializer_class = TaskSerializer
    def post(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                task = Task.objects.get(id=id)
                task.delete()
                response={
                    "error":False,
                    "message":"task deleted successfully"
                }
        except:
            response={
                "error":True,
                "message":"task deleted failed"
            }

        return Response(response)

    

class TaskComplete(APIView):
    serializer_class = TaskSerializer
    def post(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                task = Task.objects.get(id=id)
                task.completed=True
                task.save()
                response={
                    "error":False,
                    "message":"task completed successfully"
                }
        except:
            response={
                "error":True,
                "message":"task completed failed"
            }

        return Response(response)


class RegisterView(APIView):
    def post(self,request,format=None):
        serializer=UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['error']=False
            data['message']='registration success'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
            data['userid']=token.user_id										
        else:
            data['error']=True
            data['message']="username or email already exist"
            
        return Response(data)



class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        data={}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data['error']=False
            data['message']='login success'
            data['username']=user.username
            data['email']=user.email
            data['userid']=token.user_id
            data['token']=token.key
        
        return Response(data)

class setpagination(PageNumberPagination):
    page_size=4


class Pagination(ListAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    pagination_class=setpagination
    filter_backends=(SearchFilter,)
    search_fields=('title','body','completed',)


@api_view(['POST'])
def productcreate(request):
        try:
            serializer=ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Product Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Product Data"}
        return Response(dict_response)

@api_view(['GET'])
def productList(request):
      if (request.method=="GET"):
	          product = Products.objects.all()
	          serializer = ProductSerializer(product, many=True)
	          response={
		      'error':False,
		      'products':serializer.data
	          }
	          return Response(response)        


