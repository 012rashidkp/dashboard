from rest_framework import serializers
from .models import Task,Products
from rest_framework import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User=get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
         
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=65,min_length=6,write_only=True)
    email = serializers.EmailField(max_length=255,min_length=6),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User

        fields = ['username','first_name','last_name','password','email'
        ]

            

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                
                err={
                    'error': True,
                    'message':"Unable to login with given credentials."
                }
                raise exceptions.ValidationError(err)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data


class ProductSerializer(serializers.ModelSerializer):
    prod_id = serializers.CharField(source='id')
    class Meta:
        model = Products
        fields = '__all__'
        fields=('prod_id','title','desc','image','available')


      
