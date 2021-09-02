from django.shortcuts import render

# Create your views here.

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from django.http import JsonResponse
from .models import User
from django.contrib.auth.models import User as DjangoUser

# cred = credentials.Certificate("C:\\Users\\mulku\\Desktop\\iquit-507f7-firebase-adminsdk-go447-bc8b2413f2.json")
cred = credentials.Certificate("/home/iquit-507f7-firebase-adminsdk-go447-bc8b2413f2.json")
default_app=firebase_admin.initialize_app(cred)



def sign_in(request):
    #request_post = request.POST.dict()
    print(request.body)
    d=json.loads(request.body)
  

    id_token=d["token"]
    
    try:
        decoded_token = auth.verify_id_token(id_token)
        #is_info_complete=user.is_info_complete
        return JsonResponse(dict(success=True, ))
    except:
        return JsonResponse(dict(success=False))
    
    


def update_user(request):
    d=json.loads(request.body)
    try:
        user_temp = User.objects.get(id=d.id)
        user_temp.update(**d)
    except:
        return JsonResponse(dict(success=False))
    
    return JsonResponse(dict(success=True))

def get_or_create(request):
    d=json.loads(request.body)
    try:
        user_temp = User.objects.get(firebase_user_id=d.firebase_user_id)
        update_user(request)   
    except User.DoesNotExist:
        #firebase user yarat, user yarat firebase useri kullan
        User()
        user.save()
    return user
