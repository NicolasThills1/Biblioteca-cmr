import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
Usuario = get_user_model()

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            # Extrair dados da requisição
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user_type = data.get('user_type')
            
            # Autenticar usuário
            user = authenticate(username=username, password=password)
            
            # Verificar tipo de usuário
            if user is not None and user.tipo_usuario == user_type:
                return JsonResponse({
                    'success': True,
                    'redirect': 'https://www.youtube.com/watch?v=S_AEnOGOxUA'
                })
            
            return JsonResponse({
                'success': False,
                'error': 'Credenciais inválidas ou perfil incorreto'
            }, status=401)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dados inválidos'}, status=400)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)