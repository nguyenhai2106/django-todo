from django.urls import path
from todoapp import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mask_as_done, name='markAsDone' ),
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name='markAsUndone'),
    path('edit/<int:pk>', views.edit_task, name='editTask'),
    path('delete/<int:pk>', views.delete_task, name='deleteTask')
]