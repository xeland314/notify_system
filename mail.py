"""
Módulo para envío de notificaciones
Fuente: 
- https://geekflare.com/es/send-gmail-in-python/
- https://support.google.com/accounts/answer/185833?visit_id=638229635013612138-642013304&p=InvalidSecondFactor&rd=1
"""

import os
import smtplib
import ssl
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

class Mail:
    """
    Clase para enviar correos electrónicos.

    Atributos:
        port (int): Puerto del servidor SMTP.
        smtp_server_domain_name (str): Nombre de dominio del servidor SMTP.
        sender_mail (str): Correo electrónico del remitente.
        password (str): Contraseña del correo electrónico del remitente.
    """

    def __init__(self):
        """
        Inicializa la clase Mail con los atributos por defecto.
        """
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")

    def send(self, email, subject: str, content: str):
        """
        Envía un correo electrónico.

        Args:
            email (str): Correo electrónico del destinatario.
            subject (str): Asunto del correo electrónico.
            content (str): Contenido del correo electrónico.

        Returns:
            dict: Diccionario con los resultados de la operación de envío de correo electrónico.
        """
        from_email = self.sender_mail
        from_password = self.password
        to_email = email

        msg = MIMEText(content, 'html')
        msg['Subject'] = subject
        msg['To'] = to_email
        msg['From'] = from_email

        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(from_email, from_password)
        result = service.send_message(msg)
        service.quit()

        return result

if __name__ == '__main__':
    MAIL = os.getenv("EMAIL_TO")
    SUBJECT = "Desarrollo envío notificaciones"
    CONTENT = "Desarrollo de aplicación para notificaciones"

    mail = Mail()
    print(mail.send(MAIL, SUBJECT, CONTENT))
