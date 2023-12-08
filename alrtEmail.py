import smtplib, ssl

#Infos du serveur SMTP cible.
smtp_address = 'smtp.office365.com'
smtp_port = 465

#Infos sur l'adresse email expeditrice.
email_address = "test@gmail.com"
email_password = "test"

#Infos du mail destinataire.
email_receiver = "anthony.coquelet@ecoles-epsi.net"

# Création la connexion
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # Connexion au compte
  server.login(email_address, email_password)
  # Envoi du mail
  server.sendmail(email_address, email_receiver, AlrtCPU)

