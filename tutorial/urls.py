from django.contrib import admin
from django.urls import include, path
#from myapp .models import Employee
from rest_framework import routers
from rest_framework import routers, serializers, viewsets
#from students.views import StudentCreateView, StudentDetailView
from tutorial.quickstart import views
#from myapp import views #import EmployeeListCreate, EmployeeRetrieveUpdateDestroy'''

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#outer.register(r'student', views.StudentViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
[{
	"resource": "/c:/tutorial/tutorial/quickstart/views.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "reportMissingImports",
		"target": {
			"$mid": 1,
			"external": "https://github.com/microsoft/pylance-release/blob/main/DIAGNOSTIC_SEVERITY_RULES.md#diagnostic-severity-rules",
			"path": "/microsoft/pylance-release/blob/main/DIAGNOSTIC_SEVERITY_RULES.md",
			"scheme": "https",
			"authority": "github.com",
			"fragment": "diagnostic-severity-rules"
		}
	},
	"severity": 4,
	"message": "Import \"tutorial.quickstart.serializers\" could not be resolved",
	"source": "Pylance",
	"startLineNumber": 6,
	"startColumn": 6,
	"endLineNumber": 6,
	"endColumn": 37
}]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
	#path('students/', StudentCreateView.as_view(), name='student-create'),
    #path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),




