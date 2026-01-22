"""
Script interactivo para configurar el sistema de notificaciones por correo electrónico
"""
import json
import getpass
from pathlib import Path
import smtplib
from email.mime.text import MIMEText

CONFIG_FILE = Path(__file__).parent / "server" / "email_config.json"

def test_smtp_connection(smtp_server, smtp_port, email, password):
    """Test SMTP connection"""
    try:
        with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
            server.starttls()
            server.login(email, password)
        return True, "Conexión exitosa"
    except smtplib.SMTPAuthenticationError:
        return False, "Error de autenticación. Verifica tu correo y contraseña."
    except smtplib.SMTPException as e:
        return False, f"Error SMTP: {str(e)}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    print("=" * 60)
    print("CONFIGURACIÓN DEL SISTEMA DE NOTIFICACIONES POR EMAIL")
    print("=" * 60)
    print()
    
    # Check if config exists
    if CONFIG_FILE.exists():
        print("⚠️  Ya existe un archivo de configuración.")
        overwrite = input("¿Deseas sobrescribirlo? (s/n): ").lower()
        if overwrite != 's':
            print("Configuración cancelada.")
            return
        print()
    
    config = {}
    
    # Email provider selection
    print("Selecciona tu proveedor de correo:")
    print("1. Gmail")
    print("2. Outlook/Hotmail")
    print("3. Otro (configuración manual)")
    
    provider = input("\nOpción (1-3): ").strip()
    
    if provider == "1":
        config['smtp_server'] = 'smtp.gmail.com'
        config['smtp_port'] = 587
        print("\n📧 Gmail seleccionado")
        print("IMPORTANTE: Necesitas una 'Contraseña de Aplicación'")
        print("Crea una en: https://myaccount.google.com/apppasswords")
    elif provider == "2":
        config['smtp_server'] = 'smtp-mail.outlook.com'
        config['smtp_port'] = 587
        print("\n📧 Outlook seleccionado")
    else:
        config['smtp_server'] = input("\nServidor SMTP: ").strip()
        config['smtp_port'] = int(input("Puerto SMTP (generalmente 587): ").strip())
    
    print()
    
    # Sender email
    config['sender_email'] = input("Correo remitente: ").strip()
    
    # Password
    print("\nIngresa la contraseña (no se mostrará en pantalla):")
    config['sender_password'] = getpass.getpass("Contraseña: ")
    
    # Test connection
    print("\n🔄 Probando conexión SMTP...")
    success, message = test_smtp_connection(
        config['smtp_server'],
        config['smtp_port'],
        config['sender_email'],
        config['sender_password']
    )
    
    if success:
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")
        retry = input("\n¿Deseas intentar de nuevo? (s/n): ").lower()
        if retry == 's':
            return main()
        else:
            print("Configuración cancelada.")
            return
    
    # Recipients
    print("\n" + "=" * 60)
    print("DESTINATARIOS DE NOTIFICACIONES")
    print("=" * 60)
    
    recipients = []
    print("\nIngresa los correos que recibirán las notificaciones.")
    print("(Presiona Enter sin escribir nada para terminar)")
    
    while True:
        email = input(f"\nDestinatario {len(recipients) + 1}: ").strip()
        if not email:
            break
        if '@' in email:
            recipients.append(email)
            print(f"✓ Agregado: {email}")
        else:
            print("❌ Correo inválido")
    
    if not recipients:
        recipients = [config['sender_email']]
        print(f"\n⚠️  No se agregaron destinatarios. Usando: {config['sender_email']}")
    
    config['recipients'] = recipients
    
    # Monitored locations
    print("\n" + "=" * 60)
    print("UBICACIONES A MONITOREAR")
    print("=" * 60)
    
    default_locations = input("\n¿Usar ubicaciones por defecto (5658, 2699)? (s/n): ").lower()
    
    if default_locations == 's':
        config['monitored_locations'] = ['5658', '2699']
    else:
        locations = []
        print("\nIngresa las ubicaciones a monitorear.")
        print("(Presiona Enter sin escribir nada para terminar)")
        
        while True:
            loc = input(f"\nUbicación {len(locations) + 1}: ").strip()
            if not loc:
                break
            locations.append(loc)
            print(f"✓ Agregado: {loc}")
        
        config['monitored_locations'] = locations if locations else ['5658', '2699']
    
    # Enable notifications
    config['enabled'] = True
    
    # Save configuration
    print("\n" + "=" * 60)
    print("RESUMEN DE CONFIGURACIÓN")
    print("=" * 60)
    print(f"\nServidor SMTP: {config['smtp_server']}:{config['smtp_port']}")
    print(f"Remitente: {config['sender_email']}")
    print(f"Destinatarios: {', '.join(config['recipients'])}")
    print(f"Ubicaciones monitoreadas: {', '.join(config['monitored_locations'])}")
    print(f"Estado: {'Activado' if config['enabled'] else 'Desactivado'}")
    
    confirm = input("\n¿Guardar configuración? (s/n): ").lower()
    
    if confirm == 's':
        # Ensure directory exists
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        
        print(f"\n✅ Configuración guardada en: {CONFIG_FILE}")
        print("\n🎉 ¡Sistema de notificaciones configurado exitosamente!")
        print("\nPuedes modificar la configuración desde la interfaz web:")
        print("   http://localhost:5173/email-config")
    else:
        print("\nConfiguración cancelada.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nConfiguración cancelada por el usuario.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
