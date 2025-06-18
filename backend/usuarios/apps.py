from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'
    
    def ready(self):
        # Importa os sinais para garantir que sejam registrados, finalmente descobri o erro
        import usuarios.signals