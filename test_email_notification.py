"""
Script de prueba para el sistema de notificaciones por correo electrónico
"""
import sys
from pathlib import Path

# Add server to path
sys.path.insert(0, str(Path(__file__).parent / "server"))

from email_notifier import send_notification_email, load_email_config
from product_monitor import detect_new_products, reset_state
from datetime import datetime

def test_email_send():
    """Test sending a notification email"""
    print("=" * 60)
    print("TEST: Envío de Correo Electrónico")
    print("=" * 60)
    
    # Load config
    config = load_email_config()
    print(f"\n📧 Configuración cargada:")
    print(f"   Servidor: {config.get('smtp_server')}:{config.get('smtp_port')}")
    print(f"   Remitente: {config.get('sender_email')}")
    print(f"   Destinatarios: {', '.join(config.get('recipients', []))}")
    print(f"   Estado: {'Activado' if config.get('enabled') else 'Desactivado'}")
    
    if not config.get('sender_password'):
        print("\n❌ ERROR: No hay contraseña configurada")
        print("   Ejecuta: python setup_email_config.py")
        return False
    
    # Create test products
    test_products = [
        {
            "sku": "TEST-001",
            "descripcion": "Producto de Prueba 1",
            "ubicacion": "5658",
            "cantidad": 10,
            "usuario": "ga.castillo",
            "fecha": datetime.now().strftime('%Y-%m-%d %H:%M')
        },
        {
            "sku": "TEST-002",
            "descripcion": "Producto de Prueba 2",
            "ubicacion": "2699",
            "cantidad": 25,
            "usuario": "sistema",
            "fecha": datetime.now().strftime('%Y-%m-%d %H:%M')
        }
    ]
    
    print(f"\n📦 Productos de prueba: {len(test_products)}")
    for p in test_products:
        print(f"   • {p['sku']} - {p['ubicacion']}")
    
    print("\n🔄 Enviando correo de prueba...")
    success = send_notification_email(test_products)
    
    if success:
        print("✅ Correo enviado exitosamente")
        print(f"   Revisa la bandeja de entrada de: {', '.join(config.get('recipients', []))}")
        return True
    else:
        print("❌ Error al enviar correo")
        print("   Verifica la configuración y las credenciales")
        return False

def test_product_monitoring():
    """Test product monitoring system"""
    print("\n" + "=" * 60)
    print("TEST: Sistema de Monitoreo de Productos")
    print("=" * 60)
    
    print("\n⚠️  Este test requiere acceso al archivo de datos de Analytics")
    print("   Asegúrate de que exista: datos/INVENTARIO A IINVESTIGAR.xlsx")
    
    try:
        # Import here to avoid errors if pandas not available
        import pandas as pd
        from server.main import get_analytics_df
        
        df = get_analytics_df()
        
        if df.empty:
            print("\n❌ No se pudo cargar el archivo de datos")
            return False
        
        print(f"\n✅ Datos cargados: {len(df)} registros")
        
        # Get monitored locations
        config = load_email_config()
        monitored = config.get('monitored_locations', ['5658', '2699'])
        
        print(f"📍 Ubicaciones monitoreadas: {', '.join(monitored)}")
        
        # Check current products
        for loc in monitored:
            loc_df = df[df['LOC'].astype(str) == str(loc)]
            print(f"   • {loc}: {len(loc_df)} productos")
        
        print("\n🔄 Detectando nuevos productos...")
        new_products = detect_new_products(df, monitored)
        
        if new_products:
            print(f"\n✅ Se detectaron {len(new_products)} nuevos productos:")
            for p in new_products:
                print(f"   • {p['sku']} - {p['ubicacion']}")
        else:
            print("\n✓ No se detectaron productos nuevos")
            print("   (Esto es normal en la primera ejecución)")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def reset_monitoring_state():
    """Reset the monitoring state"""
    print("\n" + "=" * 60)
    print("RESET: Estado de Monitoreo")
    print("=" * 60)
    
    confirm = input("\n⚠️  ¿Estás seguro de reiniciar el estado? (s/n): ").lower()
    
    if confirm == 's':
        reset_state()
        print("✅ Estado reiniciado exitosamente")
        print("   La próxima verificación detectará todos los productos como nuevos")
    else:
        print("❌ Operación cancelada")

def main():
    print("\n" + "=" * 60)
    print("SISTEMA DE NOTIFICACIONES - SUITE DE PRUEBAS")
    print("=" * 60)
    
    print("\nSelecciona una opción:")
    print("1. Probar envío de correo")
    print("2. Probar sistema de monitoreo")
    print("3. Reiniciar estado de monitoreo")
    print("4. Ejecutar todas las pruebas")
    print("0. Salir")
    
    option = input("\nOpción: ").strip()
    
    if option == "1":
        test_email_send()
    elif option == "2":
        test_product_monitoring()
    elif option == "3":
        reset_monitoring_state()
    elif option == "4":
        print("\n🚀 Ejecutando todas las pruebas...\n")
        test_email_send()
        test_product_monitoring()
    elif option == "0":
        print("\n👋 Hasta luego!")
        return
    else:
        print("\n❌ Opción inválida")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Pruebas canceladas por el usuario")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
