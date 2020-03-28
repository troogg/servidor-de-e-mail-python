import smtplib  # bibli. responsavel pela conecxao com a inter
from email.mime.text import MIMEText

smtp = smtplib.SMTP("smtp.live.com", 587)
smtp.starttls()

smtp.login("seuemail@outlook.com.br", "sua_senha")

de = "seuemail@outlook.com.br"
para = ["destinatario@outlook.com"]
ass = "assinatura"

msn = input("\nDigite sua mensagem: ")
mail = MIMEText(msn)  # 'msn(variavel)' pega os caracteres digitados e envia para 'mail = MIMEText()'
print("\nSeu e-mail foi enviado !")
mail["seuemail@outlook.com.br"] = de
mail["Subject"] = ass

smtp.sendmail("seuemail@outlook.com.br", "destinatario@outlook.com", mail.as_string())  # extensão que envia o email
smtp.close()  # fecha a aplicação
