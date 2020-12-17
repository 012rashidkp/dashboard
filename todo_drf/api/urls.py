from django.urls import path
from . import views
from . views import TaskDetail,Taskupdate,TaskDelete,TaskComplete,Pagination

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/', views.TaskDetail.as_view(), name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/', views.Taskupdate.as_view(), name="task-update"),
	path('task-delete/', views.TaskDelete.as_view(), name="task-delete"),
	path('task-complete/', views.TaskComplete.as_view(), name="task-complete"),
	path('task-pagination/',views.Pagination.as_view(),name="pagination"),
	path('products-create/',views.productcreate,name="create-products"),
	path('products-list/',views.productList,name="product-list")

	
]