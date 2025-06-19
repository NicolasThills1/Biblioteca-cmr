from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user_type = data.get('user_type')
        
        user = authenticate(username=username, password=password)
        
        if user is not None and user.tipo_usuario == user_type:
            return JsonResponse({
                'success': True,
                'redirect': 'https://www.youtube.com/watch?v=S_AEnOGOxUA'
            })
        return JsonResponse({'success': False, 'error': 'Credenciais inválidas'}, status=401)
    return JsonResponse({'error': 'Método não permitido'}, status=405)