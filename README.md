# Sistema de Agendamento para Barbearia

Projeto desenvolvido em Django para gerenciamento de agendamentos em uma barbearia.

## Funcionalidades

- Escolha de barbeiro
- Seleção de data
- Visualização de horários disponíveis
- Agendamento de atendimento

## Tecnologias utilizadas

- Python
- Django
- Bootstrap
- JavaScript
- SQLite

## Como executar o projeto

1. Clone o repositório

git clone https://github.com/seuusuario/agendamento_barbearia

2. Entre na pasta do projeto

cd agendamento_barbearia

3. Crie um ambiente virtual

python -m venv venv

4. Ative o ambiente virtual

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

5. Instale as dependências

pip install -r requirements.txt

6. Execute as migrações

python manage.py migrate

7. Inicie o servidor

python manage.py runserver
