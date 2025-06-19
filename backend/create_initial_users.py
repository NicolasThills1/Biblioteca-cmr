import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from biblioteca.models import Usuario

def create_initial_users():
    # Criar aluno
    aluno, created = Usuario.objects.get_or_create(
        username='170021',
        defaults={
            'first_name': 'Nicolas',
            'tipo_usuario': 'aluno',
            'matricula': '170021',
            'is_staff': False,
            'is_superuser': False
        }
    )
    if created:
        aluno.set_password('TesteTestando')
        aluno.save()
        print("Aluno criado com sucesso!")
    else:
        print("Aluno já existe")

    # Criar administrador
    admin, created = Usuario.objects.get_or_create(
        username='Admin1',
        defaults={
            'first_name': 'Admin',
            'tipo_usuario': 'admin',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin.set_password('19062025')
        admin.save()
        print("Administrador criado com sucesso!")
    else:
        print("Administrador já existe")

if __name__ == '__main__':
    create_initial_users()