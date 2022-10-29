import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, reverse

from user.models import PostUser
from django.contrib.auth import authenticate, login as login_fun, logout
from post.views import home as post_home


from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from user.serializers import UserSerializer
from user.utils import generate_access_token, generate_refresh_token

# Create your views here.



# @api_view(['POST'])
# @permission_classes([AllowAny])
# @ensure_csrf_cookie
# def login_view(request):
#     PostUser = get_user_model()
#     username = request.data.get('username')
#     password = request.data.get('password')
#     response = Response()
#     if (username is None) or (password is None):
#         raise exceptions.AuthenticationFailed(
#             'username and password required')

#     user = PostUser.objects.filter(username=username).first()
#     if(user is None):
#         raise exceptions.AuthenticationFailed('user not found')
#     if (not user.check_password(password)):
#         raise exceptions.AuthenticationFailed('wrong password')

#     serialized_user = UserSerializer(user).data

#     access_token = generate_access_token(user)
#     refresh_token = generate_refresh_token(user)

#     response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
#     response.data = {
#         'access_token': access_token,
#         'user': serialized_user,
#     }
#     print('Token in login page:')
#     print(access_token)

#     request.session['token']=access_token
#     print('In session')
#     print(request.session.get('token'))
#     # return redirect(reverse('post.home',request))
#     print(reverse('post:home_post'))
#     return redirect('/post/')






def home(request):
    return render(request,'index.html')

def login(request):


    if request.method == 'POST':

        data = request.POST.dict()
        username=data.get('username')
        password=data.get('password')

        print(username)
        print(password)
        print(data)

        user = authenticate(request,username=username, password=password)
        if user is not None:
            print('authenticate successfully')
            login_fun(request, user)
            print('login successfull')
            # request.session['username']=username
            print(request.user.username)
            # request.session['user_id'] = PostUser.objects.get(username=username)
            return redirect('/post/')
        else:
            return render(request,'login.html',{
                    'error':True
            })

    return render(request,'login.html',{
        'error':False
    })

def signup(request):
    if request.method == 'POST':
        try:
            data = request.POST.dict()
            print(data)
            first=data.get('first')
            last=data.get('last')
            username=data.get('username')
            password=data.get('password')
            email=data.get('email')
            city=data.get('city')
            phone=data.get('phone')
            user = PostUser.objects.create_user(first_name=first, last_name=last, username=username, email=email,password=password,city=city,phone=phone)
            return redirect(reverse('user:login'))
        except Exception as ex :
            print('Exception occured')
            print(ex)
            return render(request, 'signup.html',{
                'error':True
            })

    return render(request, 'signup.html',{
        'error':False
    })

