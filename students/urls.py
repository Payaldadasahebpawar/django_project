from django.urls import path,include
#from students.views import StudentCreateView, StudentDetailView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
]

