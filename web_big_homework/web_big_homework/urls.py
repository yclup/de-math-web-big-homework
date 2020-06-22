"""web_big_homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from graph import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home"),
    path('specify_number/<str:template>/', views.specify_number, name="specify_number"),
    path('line_info/<str:node_name>/', views.line_info_alone, name="iine_info_alone"),
    path('cv_info/<str:node_name>/', views.cv_info, name="cv_info"),
    path('line_info/<str:start_node_name>/<str:end_node_name>/', views.line_info_double, name="line_info_double"),
    path('shortest_path/', views.shortest_path_by_post, name="sp_by_post"),
    path('shortest_path/<str:start_node_name>/<str:end_node_name>/', views.shortest_path_by_name, name='sp_by_name')
]
