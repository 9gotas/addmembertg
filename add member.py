import csv
import random
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

# Configurações
api_id = 'sua api id'
api_hash = 'sua api hash'
phone_number = 'seu numero'

# Criar cliente do Telegram
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone_number)

# Ler membros do arquivo CSV
def read_members_from_csv(file_path):
    members = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            row['__line__'] = i + 1  # Adicionar número da linha
            members.append(row)
    return members

# Verificar se o membro já está no grupo
async def is_member_in_group(group_entity, member_username):
    participants = await client.get_participants(group_entity)
    usernames = [participant.username for participant in participants if participant.username is not None]
    return member_username in usernames

# Adicionar membros ao grupo selecionado
async def add_group_members(group_entity, members):
    # Adicionar membros ao grupo
    for i, member in enumerate(members, start=1):
        name = member['Nome']
        username = member['Username']

        if username:
            try:
                # Verificar se o membro já está no grupo
                if await is_member_in_group(group_entity, username):
                    print(f"Membro {username} já faz parte do grupo {group_entity.title}")
                    continue

                # Adicionar membro ao grupo
                await client(InviteToChannelRequest(group_entity, [username]))

                print(f"Membro {username} adicionado ao grupo {group_entity.title}")

                # Intervalo de tempo aleatório entre os valores fornecidos
                sleep_time = random.choice([55, 42, 33, 61, 49, 36, 59, 44, 52])
                time.sleep(sleep_time)

                # Aguardar 5 segundos
                time.sleep(5)

                if i % 10 == 0:
                    press_alt_f3()

                # Aguardar 4 segundos
                time.sleep(4)

            except Exception as e:
                print(f"Erro ao adicionar membro {username}: {str(e)}")

                # Intervalo de tempo aleatório entre os valores fornecidos em caso de erro
                sleep_time = random.choice([55, 42, 33, 61, 49, 36, 59, 44, 52])
                time.sleep(sleep_time)
        else:
            print(f"Linha do arquivo CSV não contém um valor válido para 'Username' para o membro {name}")

    print("Adição de membros concluída.")

# Função para simular o atalho do teclado "Alt+F3"
def press_alt_f3():
    print("Executando atalho do teclado: Alt+F3")
    # Implemente a lógica para simular o atalho do teclado "Alt+F3"
    # Lembre-se de respeitar os intervalos de tempo entre as pressionadas de teclas

# Executar script
with client:
    # Obter lista de grupos dos quais você é membro
    dialogs = client.get_dialogs()

    print("Lista de grupos que você faz parte:")
    for i, dialog in enumerate(dialogs, start=1):
        print(f"{i}. {dialog.title}")

    print("")

    # Selecionar grupo para adicionar membros
    selected_group = int(input("Selecione o número do grupo para adicionar membros: "))
    group_entity = dialogs[selected_group - 1]

    # Ler membros do arquivo CSV
    members = read_members_from_csv('membros_grupo.csv')

    # Adicionar membros ao grupo selecionado
    client.loop.run_until_complete(add_group_members(group_entity, members))
