from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # Read
    path('', views.index, name='index'),  # All List
    path('<int:pk>/', views.detail, name='detail'),  # Detail

    # Create
    path('create/', views.create, name='create'),  # Save

    # Update
    path('<int:pk>/update/', views.update, name='update'),

    # Delete
    path('<int:pk>/delete/', views.delete, name='delete')
]