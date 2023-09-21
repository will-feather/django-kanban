from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kanban/', views.kanban, name='kanban'),
    path('kanban/update/', views.update_kanban, name='update_kanban'),
    path('kanban/data/', views.kanban_data, name='kanban_data'),
    path('kanban/testes/', views.testes, name='testes'),
]