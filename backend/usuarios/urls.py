from django.urls import path
from .views import AlunoLoginView, AdminLoginView

urlpatterns = [
    path('aluno/login/', AlunoLoginView.as_view(), name='aluno-login'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
]