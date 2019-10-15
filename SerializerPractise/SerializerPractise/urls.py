"""SerializerPractise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from serializerApp.views import *
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Employee API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp_crud/',EmployeeCrud.as_view(),name="employee"),
    path('emp_crud/<int:eid>/',EmployeeCrudWithId.as_view(),name="employee_id"),
    path('api-auth/', include('rest_framework.urls')),
    path('dept_crud/',DepartmentCrud.as_view(),name="dept_crud"),
    path('dept_crud/<int:dept_id>/',DepartmentCrudWithId.as_view(),name="dept_crud_id"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('register/', Registeration.as_view(), name='register'),
    # url(r'docs/$',schema_view),
    url(r'^$', schema_view),
    path('activate/<token>',activate,name="activate"),
    path('login/',UserLogin.as_view(),name="user_login"),


    path('send/',RabbitMq.as_view(),name="producer")
]
