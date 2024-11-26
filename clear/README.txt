Olá! Criei este software para excluir e-mails inúteis.



- Primeiro, criei uma função para decodificar o assunto dos e-mails, garantindo que mesmo assuntos codificados sejam legíveis. Também tratei possíveis erros de decodificação.


- Segundo, implementei uma função para localizar automaticamente a pasta de lixeira do Gmail, identificando nomes como [Gmail]/Trash, [Gmail]/Lixeira, ou [Gmail]/Bin.


- Terceiro, configurei o servidor IMAP do Gmail e as credenciais de login, garantindo uma conexão segura com a conta.


- Quarto, defini um intervalo de datas para filtrar apenas os e-mails enviados dentro de um período específico.


- Quinto, conectei à caixa de entrada do Gmail, filtrei os e-mails com base nas datas e identifiquei os IDs de cada mensagem.


- Sexto, para cada e-mail, decodifiquei o assunto e verifiquei se ele continha palavras-chave predefinidas que indicam mensagens indesejadas.


- Sétimo, ao identificar um e-mail como spam, movi-o para a pasta de lixeira detectada e marquei-o como deletado na pasta atual.


- Por último, finalizei apagando definitivamente os e-mails marcados e encerrei a conexão com o servidor.  

  _________    _________  _
 |___   ___|  |___   ___||_|
     | | _____    | |   _______
  __ | ||  _  |   | |  |   ____|
 | |_| || |_| |   | |  |  |____
 |     ||  _  |   | |  |_____  |
 |_____||_| |_|   |_|   _____  |
_______________________|_______|