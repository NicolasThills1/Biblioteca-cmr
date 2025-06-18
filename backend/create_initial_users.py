import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from usuarios.models import MilitarUser

def create_users():
    # Alunos -- ADICIONAR AQUI OS ALUNOS!!!!!!!!!!!
    aluno1 = MilitarUser.objects.create_user(
        matricula='170021',
        password='TestandoTestando',
        nome_completo='Nicolas Lacerda',
        tipo='aluno'
    )
    
    aluno2 = MilitarUser.objects.create_user(
        matricula='008982',
        password='TestandoNovamente',
        nome_completo='Mariana Lacerda',
        tipo='aluno'
    )
    
    # Administrador
    admin = MilitarUser.objects.create_user(
        matricula='CMRBOOK1221',
        password='18062025',
        nome_completo='Administrador do Sistema',
        tipo='admin',
        is_staff=True
    )
    
    print("Usuários criados com sucesso!")

if __name__ == '__main__':
    create_users()