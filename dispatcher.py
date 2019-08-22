from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

emails_destino = ["email1@email", "email2@email"]
email_origem = "seuemail@email"
password = "asenhadoseuemail"
assunto = "Assunto do e-mail"
de = "Seu Nome <seuemail@email>"
nome_arquivo = "CaminhoENomeDoArquivo.extensao"
texto_email = "Texto do e-mail"

for x in range (0, len(emails_destino)):

    msg = MIMEMultipart()

    msg["From"] = de
    msg["To"] = emails_destino[x]
    msg["Subject"] = assunto

    anexo = MIMEBase("application", "extensaoDoArquivo", filename = nome_arquivo)
    anexo.set_payload(open(nome_arquivo, "rb").read())
    encoders.encode_base64(anexo)
    anexo.add_header("Content-Disposition", "attachment", filename = nome_arquivo)
    msg.attach(anexo)

    msg.attach(MIMEText(texto_email, "plain"))

    server = smtplib.SMTP("smtpDoSeuProvedor:porta")

    server.starttls()

    server.login(email_origem, password)

    server.sendmail(email_origem, msg["To"], msg.as_string())

    server.quit()