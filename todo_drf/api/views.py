from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer,UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib import auth
from .models import Task
from rest_framework.views import APIView


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		'Register':'/register/'
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	  tasks = Task.objects.all().order_by('-id')
	  serializer = TaskSerializer(tasks, many=True)
	  res={
		  'error':False,
		  'datas':serializer.data
	  }
	  return Response(res)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response({'error':False,'message':'created successfully','datas':serializer.data})
    
@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully deleted!')

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
            data['message']=serializer.errors
            
        return Response(data)


