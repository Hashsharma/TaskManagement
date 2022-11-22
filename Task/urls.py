from django.urls import path
from .views import Tasks


urlpatterns = [
    path('create', Tasks.create_task),
    path('lists/', Tasks.get_all_tasks),
    path('completed/', Tasks.get_completed_tasks),
    path('mark-completed', Tasks.mark_task_completed),
    path('delete', Tasks.delete_task),
    path('deleted-task/', Tasks.get_deleted_tasks),
    path('pending/', Tasks.get_pending_tasks),
]
