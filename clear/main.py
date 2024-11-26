import imaplib
import email
from email.header import decode_header

# Função para decodificar o assunto com segurança
def decodificador(subject):
    try:
        decoded_subject, encoding = decode_header(subject)[0]
        if isinstance(decoded_subject, bytes):
            decoded_subject = decoded_subject.decode(encoding if encoding else "utf-8")
        return decoded_subject
    except Exception as e:
        print(f"Erro ao decodificar o assunto: {e}")
        return subject

# Função para detectar a pasta de lixeira no Gmail
def encontrar_pasta_lixeira(mail):
    status, arquivos = mail.list()
    if status == "OK":
        for arquivo in arquivos:
            if b"[Gmail]/Trash" in arquivo or b"[Gmail]/Lixeira" in arquivo or b"[Gmail]/Bin" in arquivo:
                return arquivo.decode().split(' "/" ')[-1].strip('"')
    return None

# Configurações de login e servidor
IMAP_SERVER = "imap.gmail.com"
EMAIL = "josiascraft1019@gmail.com"
PASSWORD = "ager ofnm nnpl kudc"

# Intervalo de datas desejado
inicio_data = "01-Jan-2017"  # Desde 01/01/2017
fim_data = "25-Nov-2024"  # Até 25/11/2024

# Conexão ao servidor
try:
    print("Conectando ao servidor de e-mail...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    print("Conexão bem-sucedida!")

    # Detecta a pasta da lixeira
    pasta_lixo = encontrar_pasta_lixeira(mail)
    if not pasta_lixo:
        raise Exception("Pasta de lixeira não encontrada!")

    print(f"Pasta de lixeira detectada: {pasta_lixo}")

    # Seleciona a pasta INBOX para leitura e escrita
    mail.select("inbox", readonly=False)

    # Filtra mensagens por intervalo de datas
    status, messages = mail.search(None, f'SINCE {inicio_data} BEFORE {fim_data}')
    
    mail_ids = messages[0].split()

    print(f"Total de mensagens no intervalo {inicio_data} a {fim_data}: {len(mail_ids)}")

    for mail_id in mail_ids:
        try:
            # Obtém o e-mail
            status, msg_data = mail.fetch(mail_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Decodifica o e-mail
                    msg = email.message_from_bytes(response_part[1])

                    # Obtem o assunto e decodifica com segurança
                    subject = decodificador(msg["Subject"])
                    if isinstance(subject, str):
                        print(f"Assunto: {subject}")
                        keywords = [
                            "c-date", "stellantis", "promoção", "linkedin", "freelancer", "epic games", "jobbol", "infojobs", 
                            "pinterest", "nubank", "mercado pago", "vagas estagios", "Cataratas", "Steam", "descontos", "B3", 
                            "kwai", "snapchat", "udemy", "pix", "dinheiro", "InsaneGGameS", "yoda", "vagas", "estágiario",
                            "emprego", "cupom", "twitch", "live", "compras", "viagem", "grátis", "pesquisa", "ganhe", "oferta",
                            "compartilhou", "publicações", "perfil", "marketing", "off", "mensagem", "like", "try", "us", "ganhar", "conversar",
                            "%", "convite", "R$", "cargo", "contratando", "oportunidades", "miss", "sent", "vaga", "auxiliar", "mensagem", "free",
                            "Técnico", "Desenvolvedor", "Estagiário", "contratando", "Solicitação", "off", "cargo", "curso", "mensagens", "League of Legends",
                            "kabum", "sorte", "opinião", "Aprenda", "Ninja", "Vivo", "$", "black friday", "sale", "Assistente", "Ubisoft", "Feedback",
                            "convites", "currículo", "spam", "Publicidade", "Points", "Music", "Educacional", "lol", "@Rappi", "GitHub", "Oi", "Last", "financeiro",
                            "Novidade", "XP Investimentos", "Invista", "destaques", "canal", "Oportunidade", "Netflix", "feriados", "Dicas",
                            "retrospectiva", "dúvidas", "filme", "Fantia", "inscrição", "limite", "Continue", "SSGamers", "Claim", "desconto",
                            "série", "notificações", "Full", "CodinGame", "summer", "crédito", "cupom", "Power BI", "PERCA", "Lembrete",
                            "Aproveite", "PRÉ-MATRICULA", "Updates", "Treinamento", "Pokémon", "acaba", "novo", "destrave", "inglês",
                            "Olá", "CPF", "negativado", "Atualizações", "incríveis", "promo", "99Freelas" "Novo Projeto",
                            "jogo", "tiktok", "vídeos", "pagamento", "selecionado", "Projeto", "comentou", "Aprenda", "Fiat", "contratou"
                            "sugestões", "YouTube", "Cripto", "reagiu", "preço", "HTML", "PHP", "Website", "chegou", "Jeep",
                            "Últimos"
                        ]
                        if any(keyword in subject.lower() for keyword in keywords):
                            print("E-mail identificado como spam. Movendo para a lixeira...")
                            # Move para a lixeira
                            mail.copy(mail_id, pasta_lixo)
                            # Marca como deletado na pasta atual
                            mail.store(mail_id, '+FLAGS', '\\Deleted')
        except Exception as e:
            print(f"Erro ao processar a mensagem {mail_id}: {e}")

    # Apaga todos os e-mails marcados para exclusão
    mail.expunge()
    print("E-mails movidos para a lixeira com sucesso!")

    # Encerra a conexão
    mail.logout()
    print("Conexão encerrada.")

except Exception as e:
    print("Ocorreu um erro:", e)
