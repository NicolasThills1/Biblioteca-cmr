from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import MilitarUser

@method_decorator(csrf_exempt, name='dispatch')
class AlunoLoginView(APIView):
    def post(self, request):
        matricula = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=matricula, password=password)
        
        if user is not None and user.tipo == 'aluno':
            login(request, user)
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@method_decorator(csrf_exempt, name='dispatch')
class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.tipo == 'admin':
            login(request, user)
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)