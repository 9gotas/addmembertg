# addmembertg
 bot permite que você adicione facilmente membros aos grupos do Telegram de forma automatizada. 

Apresentando o Bot de Adição de Membros ao Telegram:

Nosso bot permite que você adicione facilmente membros aos grupos do Telegram de forma automatizada. Basta fornecer um arquivo CSV com os detalhes dos membros e o bot fará o trabalho pesado para você.

# Resumo do código:

# 1. Configurações:
No início do código, você encontrará algumas configurações básicas, como a ID e o hash da API do Telegram, além do número de telefone associado à sua conta.

# 2. Ler membros do arquivo CSV: 
O bot lê os detalhes dos membros de um arquivo CSV. Esses detalhes podem incluir o nome e o nome de usuário dos membros.

3. Verificar se o membro já está no grupo: Antes de adicionar um membro, o bot verifica se o membro já faz parte do grupo para evitar duplicatas.

4. Adicionar membros ao grupo selecionado: O bot itera por cada membro e adiciona-os ao grupo selecionado. Ele utiliza a função `InviteToChannelRequest` para enviar solicitações de convite aos membros.

5. Intervalo de tempo entre as adições: Para evitar bloqueios, o bot incorpora um intervalo de tempo aleatório entre as adições de membros. Esse intervalo é definido na linha 52, onde o bot escolhe um tempo de espera aleatório entre uma lista de valores pré-definidos.

# 6.Mudança automática de ip:

Implementamos o uso do Mouse Recorder e ProtonVPN. O Mouse Recorder grava ações do mouse e o ProtonVPN altera o IP. Ao pressionar "Alt+F3" no bot, ele executará as ações gravadas (o que já está implementado ao codigo para ser executado de forma automática a cada 10 membros adicionados, valor esse que pode ser alterado), trocando de IP automaticamente. Isso ajuda a evitar bloqueios durante a adição de membros. Certifique-se de cadastrar-se e instalar corretamente o ProtonVPN.

7. Execução do script: No final do código, o bot solicita que você selecione o grupo ao qual deseja adicionar membros e, em seguida, ele lê os membros do arquivo CSV e adiciona-os ao grupo selecionado.

Com nosso bot, você pode automatizar o processo de adicionar membros aos seus grupos do Telegram, economizando tempo e esforço.
