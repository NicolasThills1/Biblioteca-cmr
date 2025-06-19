import os
import django
import sys

# Adiciona o diretório pai ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from usuarios.models import MilitarUser

def create_users():
    # Verifica se os usuários já existem
    if MilitarUser.objects.filter(matricula='170021').exists():
        print("Usuários já existem. Nada a fazer.")
        return

    # Alunos
    MilitarUser.objects.create(
        matricula='170021',
        password=make_password('TestandoTestando'),
        nome_completo='Nicolas Lacerda',
        tipo='aluno'
    )
    
    MilitarUser.objects.create(
        matricula='008982',
        password=make_password('TestandoNovamente'),
        nome_completo='Mariana Lacerda',
        tipo='aluno'
    )
    
    # Administrador
    MilitarUser.objects.create(
        matricula='CMRBOOK1221',
        password=make_password('18062025'),
        nome_completo='Administrador do Sistema',
        tipo='admin',
        is_staff=True
    )
    
    print("Usuários criados com sucesso!")

if __name__ == '__main__':
    create_users()