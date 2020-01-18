from django.shortcuts import render

# Create your views here.

from .serializers import EmployeeSerializer,DepartmentModelSerializer,RegistrationSerializer,LoginSerializer
from . models import Employee,Department
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
import json
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView  # Added for Swagger to work
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
import jwt
from django.conf import settings

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCrud(GenericAPIView):

    serializer_class=EmployeeSerializer  # Added for Swagger to work

    def get(self,request,*args,**kwargs):

        queryset=Employee.objects.all()

        print(type(queryset), '--------->queryset')

        # emp_obj=Employee.objects.get(ename="saurabh")
        # print(type(emp_obj),'--------->emp_obj')
        #
        # emp_obj_list = Employee.objects.filter(eaddr="kandivali east")
        # print(emp_obj_list)
        """
        Here we are getting single emp_obj ,we are getting collection of emp objects i.e Queryset
        In order to convert this Queryset into python native type ,We need to pass many as True in our
        EmployeeSerializer(queryset,many=True)
         
        """
        eserializer_with_queryset=EmployeeSerializer(queryset,many=True)

        """
        Here emp_obj is complex type i.e it is a instance of class Employee ,
        so in order to send this object into json format ,first we need convert this emp_obj into 
        python native data type,this work will be done by serializer ,EmployeeSerializer(emp_obj) 
        will take emp_obj as an argument and convert this in native type ,here Dict,
        After that we can easily convert this dict into json  And we get those native type into
        eserializer.data
        
        """

        """
        Here Employee.objects.filter(eaddr="kandivali east") returns List of objects means ,collection 
        of emp objects ,so we need to take many=True
        """
        eserializer=EmployeeSerializer(queryset,many=True)
        print(eserializer.data, type(eserializer.data), '------->')


        json_data=json.dumps(eserializer.data)

        print(eserializer.data, type(eserializer.data),'------->')
        return HttpResponse(json_data,status=200)

    def post(self,request,*args,**kwars):

        response={'success':False,
                'message':'something went wrong',
                'data':[]
                  }

        json_data=request.body
        stream=io.BytesIO(json_data)
        request_data=JSONParser().parse(stream)
        
        eserializer=EmployeeSerializer(data=request_data)


        if eserializer.is_valid():

            print(eserializer.validated_data,type(eserializer.validated_data))

            obj=eserializer.save(user=request.user)

            print('---->obj',obj)

            response['success']=True
            response['message']='record successfully created'

        print(eserializer.errors,'---->errors')

        json_response=JSONRenderer().render(response)

        print(json_response,type(json_response))

        return HttpResponse(json_response,status=201)


    def put(self,request,*args,**kwargs):

        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }

        json_data=request.body

        stream=io.BytesIO(json_data)
        request_data=JSONParser().parse(stream)

        id=request_data['id']
        emp_obj=Employee.objects.get(id=id)
        eserializer=EmployeeSerializer(data=request_data,instance=emp_obj,partial=True)

        if eserializer.is_valid():

            eserializer.save(user=request.user)

            response['success']=True
            response['message']='updated successfully'
        print(eserializer.errors,'-------->errors')


        return JsonResponse(response,status=200)




@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCrudWithId(APIView):

    def get(self,request,eid=None,*args,**kwargs):

        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }
        try:
            if eid:

                emp_obj=Employee.objects.get(id=eid)
                eserializer=EmployeeSerializer(emp_obj)

                print(eserializer.data)
                data=eserializer.data

                response['success']=True
                response['message']='successful'
                response['data']=[data]

        except Employee.DoesNotExist:
            response['success'] = False
            response['message'] = 'DoesNotExist'

        return JsonResponse(response,status=200)

    def delete(self, request, eid=None, *args, **kwargs):

        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }
        print(eid)
        emp_obj=Employee.objects.get(id=eid)

        if emp_obj:

            emp_obj.delete()
            response['success']=True
            response['message']='successfully deleted'

        return JsonResponse(response,status=200)

@method_decorator(csrf_exempt,name="dispatch")
class DepartmentCrud(APIView):


    def get(self,request,*args,**kwargs):
        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }

        dept_queryset=Department.objects.all()
        print(dept_queryset)
        serializer=DepartmentModelSerializer(dept_queryset,many=True)
        print(serializer.data)

        # response=json.dumps(serializer.data)
        response['success']=True
        response['message']="successfully listed all records"
        response['data']=serializer.data
        # return HttpResponse(res)
        """
        TypeError: In order to allow non-dict objects to be serialized set the safe parameter to False.
        for JsonResponse(safe=False) , if we want to send list etc other than dict as json then we need to pass safe=False 
            as argument
            
            return JsonResponse(serializer.data,safe=False) 
        """
        return JsonResponse(response,status=200)


    def post(self,request,*args,**kwargs):

        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }

        request_data=json.loads(request.body)

        serializer=DepartmentModelSerializer(data=request_data)

        if serializer.is_valid():

            obj=serializer.save()
            print(obj,'-------->')
            response['success']=True
            response['message']='successfully saved'
            response['data']=[]

        return JsonResponse(response,status=201)




@method_decorator(csrf_exempt,name="dispatch")
class DepartmentCrudWithId(APIView):

    def put(self, request, dept_id, *args, **kwargs):
        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }
        print(dept_id)
        request_data = json.loads(request.body)

        dept_obj = Department.objects.get(id=dept_id)

        dept_serializer=DepartmentModelSerializer(data=request_data, instance=dept_obj, partial=True)

        if dept_serializer.is_valid():

            dept_serializer.save()
            response['success'] = True
            response['message'] = "successfully upupdateddated"

        return JsonResponse(response)

    def delete(self, request,dept_id, *args, **kwargs):

        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }
        print(dept_id)

        dept_obj = Department.objects.get(id=dept_id)

        dept_obj.delete()
        response['success'] = True
        response['message'] = 'successfully deleted'

        return JsonResponse(response,status=200)

from django.contrib.sites.shortcuts import get_current_site
from . utils import *
from bitly_api import Connection,BitlyError, Error

@method_decorator(csrf_exempt,name="dispatch")
class Registeration(APIView):

    serializer_class= RegistrationSerializer
    permission_classes=(IsAuthenticated,)

    def post(self,request,*args,**kwargs):

        response = {'success': False,
                    'message': 'something went wrong',
                    'data': []
                    }

        request_data = json.loads(request.body)
        username=request_data["username"]
        password=request_data["password"]
        email=request_data["email"]
        user_obj=User(username=username,password=password,email=email)
        user_obj.set_password(password)
        user_obj.is_active = False

        user_obj.save()

        token=jwt.encode({"username":username},key="saurabhSecret",algorithm='HS256').decode('utf-8')
        print(token,'-->')
        subject="Email Verification"

        message="http://"+get_current_site(request).domain+"/"+"activate"+"/"+token

        API_USER = "o_1ucgrsfbmr"
        API_KEY = "R_2d82deb00a324c4d9aa562de748135c0"
        bitly = Connection(API_USER, API_KEY)

        bitly_response = bitly.shorten(message)

        print(bitly_response,'bitly_response-------->')


        message=bitly_response['url']

        # message=render_to_string('serializerApp/account_activate.html',{
        #     "token":token,
        #     "domain":get_current_site(request).domain
        # })
        #
        # print(message)

        to="singh.saurabh3333@gmail.com"
        recipient_list=[to]
        # status=send_mail(subject,message,'singh.saurabh3333@gmail.com',[to])
        # print(status,'----status')
        status=ee.emit('event',subject,message,recipient_list)
        print(status)
        response['success']=True
        response['message']="Registeration successful"

        return JsonResponse(response)

def activate(request,token):

    response = {'success': False,
                'message': 'something went wrong',
                'data': []
                }

    payload=jwt.decode(token,key="saurabhSecret",algorithms=['HS256'])
    print(payload)
    username=payload["username"]
    obj=User.objects.get(username=username)

    if obj.is_active is not True:
        obj.is_active=True
        obj.save()

        response['success'] = True
        response['message'] = "account verified successfully"

    else:
        response['success'] = False
        response['message'] = "account already verified"

    return JsonResponse(response)

from django.contrib.auth import authenticate


class UserLogin(GenericAPIView):

    serializer_class = LoginSerializer
    # permission_classes=(AllowAny,)

    def post(self,request,*args,**kwargs):

        try:
            response={
                'success':False,
                'message':'something went wrong',
                'data':[]
            }

            request_data=(request.data) # it is giving dict

            print(request_data,'request_data------>',type(request_data))
            username=request_data['username']
            password=request_data['password']

            user_obj=authenticate(username=username,password=password)
            print(user_obj,'-----user_obj')
            payload={'username':user_obj.username}
            token=jwt.encode(payload=payload,key="its a secret",algorithm='HS256').decode('utf-8')

            response['success']=True
            response['message']='successfully logged in'
            response['data']={'token':token}

            response=json.dumps(response)

        except User.DoesNotExist:

            response=response['message'] = 'User Does Not Exist'
            response=json.dumps(response)

        return HttpResponse(response)


from auth.decorator import IsAuthenticated_User

@method_decorator(IsAuthenticated_User,name="dispatch")
class HelloView(GenericAPIView):


    # permission_classes = (AllowAny,)

    def get(self, request):

        content = {'message': 'Hello, World!'}

        print(request.user,'----------->request.user')
        print(request.META.get('HTTP_AUTHORIZATION'),'--------->Meta Headers')

        print(request.user.is_authenticated,'--->is_authenticated')
        token_scheme=request.META.get('HTTP_AUTHORIZATION')

        # token_list=token_scheme.split(' ')
        # print(token_list[1])
        #
        # payload=jwt.decode(token_list[1],settings.SECRET_KEY)
        # print(payload,'---------->payload')

        return Response(content)

from django.core.files.storage import FileSystemStorage

# @method_decorator(csrf_exempt,name="dispatch")
class UploadFile(APIView):


    def post(self,request,*args,**kwargs):

        response = {
            'success': False,
            'message': 'something went wrong',
            'data': []
        }


        # print(request.body,'------>body')

        print('------->')
        f=json.loads(request.body)

        # print(f,'----------->f')
        # print(request.POST,'---------->request.POST')

        # print(type(request.POST))
        # print(eval(request.POST))
        # print(request.FILES['inpFile'],'------->inpFile')
        # myfile=f['inpFile']
        #
        # import base64
        # decoded = base64.b64decode(f['inpFile'])
        # print(type(decoded),'------->decoded')
        # print(json.loads(decoded.decode('utf-8')))

        import base64
        # decoded=base64.b64decode(json.loads(f['inpFile'].read()))
        # print(decoded,'------d')
        # # print(request.FILES['inpFile'])
        # # myfile = request.FILES['inpFile']
        # # print(type(myfile),'----->type','---->',myfile.name)
        from django.core.files.base import ContentFile

        image_data = f['inpFile']
        # format, imgstr = image_data.split(';base64,')
        # print("format", format)
        # ext = format.split('/')[-1]

        data = ContentFile(base64.b64decode(image_data))
        print(type(data),'===========>data')
        file_name = "myphoto.jpg"
        # user.image.save(file_name, data, save=True)

        fs = FileSystemStorage()
        filename = fs.save(file_name, data)
        # uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url,'----->',filename,'----->',fs)

        return JsonResponse(response)

@method_decorator(csrf_exempt,name="dispatch")
class ImageUploadAlongWithOtherData(APIView):

    def post(self,request,*args,**kwargs):

        response = {
            'success': False,
            'message': 'something went wrong',
            'data': []
        }
        import ast
        print(request.data,'----->request.data')
        """
        in request.data ,i am getting all form data along with image file also 
        just i need to serializer ,that will automatically save all things
        
        """

        print(request.FILES)
        print(request.POST)
        print(request.POST.get('labels'),type(request.POST.get('labels')))
        l=request.POST.get('labels')
        d=request.POST.get('dicttry')
        res = ast.literal_eval(l)
        res_d = ast.literal_eval(d)
        # print(type(int(l)))
        print("final list", res,type(res))
        print("final dict", res_d,type(res_d))
        print(type(res))
        img=request.FILES['profile1']
        img2=request.FILES['inpFile']

        print(img)
        print(img2)

        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)

        return JsonResponse(response)

# def send_reminder(request):
#
#     pass
#
#     time_to_match=""
#     return HttpResponse('hi')
#
import requests
class A(APIView):

    def get(self,request,*args,**kwargs):

            _url="https://accounts.google.com/o/oauth2/v2/auth"
            client_id="681108048610-ujjurhikob4653vol9jb0kfst5u41k2a.apps.googleusercontent.com"
            client_secret="MqANqGZPuyGYSf8pmsoDfC4W"
            response_type="code"
            scope="https://www.googleapis.com/auth/gmail.send"
            redirect_uri="http://localhost"
            access_type="offline"

            # url=_url+client_id+response_type+scope+redirect_uri+access_type

            # url=f"https://accounts.google.com/o/oauth2/v2/auth?client_id=681108048610-ujjurhikob4653vol9jb0kfst5u41k2a.apps.googleusercontent.com&response_type=code&scope=https://www.googleapis.com/auth/gmail.send&redirect_uri=http://localhost&access_type=offline"
            # response=requests.get(url)
            # print(json.loads(response.text))
            # print(response.text)

            request_data = {

                "code":"4/vgFHz2bHYXCvK5ni0pQ7zGytk4yYyPXGmIqxrCuKiZFeOTV_VV9PYpdUAWeAr395SyjM7COXRoPNUQ9ekdTiv8k",
                "client_id":"681108048610-ujjurhikob4653vol9jb0kfst5u41k2a.apps.googleusercontent.com",

                "client_secret":"MqANqGZPuyGYSf8pmsoDfC4W",

                "grant_type": "authorization_code",
                "redirect_uri": "http://localhost:8000"

            }

            headers = {

                "Content-Type": "application/x-www-form-urlencoded"
            }

            response = requests.post(url='https://www.googleapis.com/oauth2/v4/token', data=request_data,headers=headers)

            print(response.text)


            return JsonResponse(data=[],safe=False)