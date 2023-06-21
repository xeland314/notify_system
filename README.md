# notify_system

Sistema para el envío de notificaciones por correo electrónico

## Objetivos

El objetivo de este proyecto es crear un sistema para enviar notificaciones por correo electrónico a los usuarios. El sistema debe ser capaz de enviar correos electrónicos a una lista de destinatarios y debe ser fácilmente configurable para que los usuarios puedan personalizar los mensajes y la configuración del servidor SMTP.

## Características

- Envío de correos electrónicos a una lista de destinatarios
- Personalización de mensajes y configuración del servidor SMTP
- Fácil integración con otros sistemas

## Requisitos

- Python 3.x
- Librería `smtplib`
- Librería `email`
- Librería `dotenv`

## Configuración

Para configurar el sistema, debes editar el archivo `config.py` y agregar tus credenciales SMTP y la lista de destinatarios. Aquí hay un ejemplo:

```python
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "tu_correo_electronico"
SMTP_PASSWORD = "tu_contraseña"

TO_EMAILS = ["destinatario1@example.com", "destinatario2@example.com"]
