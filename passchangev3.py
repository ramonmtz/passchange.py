# -*- coding: utf-8 -*-
"""
Aplicación DEFINITIVA para cambiar contraseñas mediante SSH en un rango de IPs
para dispositivos Ubiquiti con AirOS.

- VERSIÓN 7 (Final y Robusta): Añade validación completa de la IP base para
  asegurar que contenga 3 octetos válidos (0-255).
- Utiliza la librería 'passlib' para ser multiplataforma y a prueba de futuro.

                    Maded By Ramonmtz
                    Final Version refined by community feedback & Gemini
"""

import sys
import getpass
import ipaddress  # <-- Módulo para validar IPs
from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Dependencias ---
try:
    import paramiko
except ImportError:
    print("Error: La librería 'paramiko' no está instalada.", file=sys.stderr)
    print("Por favor, instálala con: pip install paramiko", file=sys.stderr)
    sys.exit(1)

try:
    from passlib.hash import md5_crypt
except ImportError:
    print("Error: La librería 'passlib' no está instalada.", file=sys.stderr)
    print("Por favor, instálala con: pip install passlib", file=sys.stderr)
    sys.exit(1)
# --------------------


class SSHPasswordChangerUbiquiti:
    # ... (El resto de la clase no necesita cambios) ...
    def __init__(self, username: str, current_password: str, max_threads: int = 10):
        self.username = username
        self.current_password = current_password
        self.timeout = 20
        self.max_threads = max_threads
        print(f"🔩 Configurado para ejecutarse con hasta {self.max_threads} hilos simultáneos.")

    def generate_airos_hash(self, password: str) -> str:
        return md5_crypt.hash(password)

    def generate_ip_range(self, base_ip: str, start_octet: int, end_octet: int) -> List[str]:
        return [f"{base_ip}.{i}" for i in range(start_octet, end_octet + 1)]

    def _execute_command(self, client: paramiko.SSHClient, command: str) -> Tuple[int, str, str]:
        stdin, stdout, stderr = client.exec_command(command, timeout=30)
        exit_status = stdout.channel.recv_exit_status()
        return exit_status, stdout.read().decode('utf-8'), stderr.read().decode('utf-8')

    def _change_password_on_device(self, ip: str, new_password: str) -> Tuple[str, bool, str]:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.RejectPolicy())
        
        try:
            client.connect(
                hostname=ip,
                username=self.username,
                password=self.current_password,
                timeout=self.timeout
            )
        except paramiko.AuthenticationException:
            return ip, False, "Error de autenticación. Contraseña actual incorrecta."
        except Exception as e:
            return ip, False, f"Error de conexión: {e}"

        try:
            hashed_password = self.generate_airos_hash(new_password)
            
            find_user_cmd = f"grep -E '^users\\.[0-9]+\\.name={self.username}' /tmp/system.cfg"
            status, out, err = self._execute_command(client, find_user_cmd)
            if status != 0 or not out:
                return ip, False, f"No se pudo encontrar al usuario '{self.username}' en la configuración."
            
            user_index = out.strip().split('.')[1]

            escaped_hash = hashed_password.replace("$", "\\$")
            change_cmd = f"sed -i 's|^users.{user_index}.password=.*|users.{user_index}.password={escaped_hash}|' /tmp/system.cfg"
            status, out, err = self._execute_command(client, change_cmd)
            if status != 0:
                return ip, False, f"Fallo al modificar el archivo de configuración. Error: {err}"

            apply_cmd = "/usr/etc/rc.d/rc.softrestart save"
            status, out, err = self._execute_command(client, apply_cmd)
            if status != 0:
                return ip, False, f"Fallo al guardar y aplicar la configuración. Error: {err}"
            
            return ip, True, "Contraseña hasheada, guardada y aplicada exitosamente."
        
        finally:
            client.close()

    def change_passwords_in_range(self, base_ip: str, start_octet: int, end_octet: int, new_password: str):
        ips = self.generate_ip_range(base_ip, start_octet, end_octet)
        print(f"\n🚀 Iniciando cambio de contraseñas para {len(ips)} dispositivos...")
        # ... (El resto del método no necesita cambios) ...
        pass


def is_valid_base_ip(ip_str: str) -> bool:
    """Verifica si la cadena es una base de IP válida (3 octetos entre 0-255)."""
    if ip_str.count('.') != 2:
        return False
    try:
        # Intentamos crear una IP completa añadiendo un último octeto válido.
        # Si la base es incorrecta (ej: "192.168.500"), esto generará un ValueError.
        ipaddress.ip_address(f"{ip_str}.1")
        return True
    except ValueError:
        return False

def main():
    print("🔐 CAMBIADOR DE CONTRASEÑAS PARA UBIQUITI AirOS (v7 - Final y Robusta)")
    print("========================================================================")
    
    try:
        username = input("👤 Usuario SSH (ej: ubnt): ")
        current_password = getpass.getpass("🔒 Contraseña actual: ")
        
        base_ip = input("🌐 IP base (ej: 192.168.1): ")
        # --- INICIO: Bloque de Validación de IP Base ---
        if not is_valid_base_ip(base_ip):
            print("\n❌ Error: La IP base introducida no es válida.")
            print("   Debe contener 3 octetos separados por puntos, con valores entre 0 y 255.")
            print("   Ejemplo correcto: 192.168.1")
            sys.exit(1)
        # --- FIN: Bloque de Validación de IP Base ---

        start_octet = int(input("📍 Octeto inicial (ej: 20): "))
        end_octet = int(input("📍 Octeto final (ej: 50): "))

        if not (1 <= start_octet <= 254 and 1 <= end_octet <= 254 and start_octet <= end_octet):
            print("\n❌ Error en el rango de IPs:")
            # ... (resto de la validación sin cambios) ...
            sys.exit(1)
        
        # ... (resto del script sin cambios) ...
        pass
        
    except KeyboardInterrupt:
        print("\n🚫 Operación interrumpida por el usuario.")
    except ValueError:
        print("\n❌ Error: El valor para los octetos debe ser un número entero.")
    except Exception as e:
        print(f"\n❌ Error inesperado en la aplicación: {e}")

if __name__ == "__main__":
    # He rellenado los métodos incompletos para que el script sea completamente funcional
    def patched_change_passwords_in_range(self, base_ip: str, start_octet: int, end_octet: int, new_password: str):
        ips = self.generate_ip_range(base_ip, start_octet, end_octet)
        print(f"\n🚀 Iniciando cambio de contraseñas para {len(ips)} dispositivos...")
        print("-" * 70)
        
        successful = []
        failed = []

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_ip = {executor.submit(self._change_password_on_device, ip, new_password): ip for ip in ips}
            
            for i, future in enumerate(as_completed(future_to_ip)):
                ip, success, message = future.result()
                progress = f"[{i + 1}/{len(ips)}]"
                
                if success:
                    print(f"{progress} ✅ {ip}: {message}")
                    successful.append(ip)
                else:
                    print(f"{progress} ❌ {ip}: {message}")
                    failed.append((ip, message))
        
        print("\n" + "="*70)
        print("📋 RESUMEN FINAL")
        print("="*70)
        print(f"✅ Exitosos: {len(successful)}")
        print(f"❌ Fallidos: {len(failed)}")
        
        if successful:
            print(f"\n🎉 Dispositivos con contraseña cambiada exitosamente:")
            for ip in successful:
                print(f"  • {ip}")
        
        if failed:
            print(f"\n⚠️ Dispositivos con errores:")
            for ip, error in failed:
                print(f"  • {ip}: {error}")
    
    SSHPasswordChangerUbiquiti.change_passwords_in_range = patched_change_passwords_in_range

    def patched_main():
        print("🔐 CAMBIADOR DE CONTRASEÑAS PARA UBIQUITI AirOS (v7 - Final y Robusta)")
        print("========================================================================")
        
        try:
            username = input("👤 Usuario SSH (ej: ubnt): ")
            current_password = getpass.getpass("🔒 Contraseña actual: ")
            
            base_ip = input("🌐 IP base (ej: 192.168.1): ")
            if not is_valid_base_ip(base_ip):
                print("\n❌ Error: La IP base introducida no es válida.")
                print("   Debe contener 3 octetos separados por puntos, con valores entre 0 y 255.")
                print("   Ejemplo correcto: 192.168.1")
                sys.exit(1)

            start_octet = int(input("📍 Octeto inicial (ej: 20): "))
            end_octet = int(input("📍 Octeto final (ej: 50): "))

            if not (1 <= start_octet <= 254 and 1 <= end_octet <= 254 and start_octet <= end_octet):
                print("\n❌ Error en el rango de IPs:")
                print("  - Ambos octetos deben estar en el rango de 1 a 254.")
                print("  - El octeto inicial no puede ser mayor que el octeto final.")
                print("Saliendo...")
                sys.exit(1)
            
            new_password = getpass.getpass("🔑 Nueva contraseña: ")
            confirm_password = getpass.getpass("🔑 Confirmar nueva contraseña: ")
            
            if new_password != confirm_password:
                print("\n❌ Las contraseñas no coinciden. Saliendo...")
                sys.exit(1)
            
            ips_to_process = end_octet - start_octet + 1
            print(f"\n⚠️ ADVERTENCIA: Se intentará cambiar la contraseña del usuario '{username}' en {ips_to_process} antenas.")
            
            confirm = input("¿Está seguro de que desea continuar? (s/N): ").lower()
            if confirm not in ['s', 'si', 'y', 'yes']:
                print("🚫 Operación cancelada por el usuario.")
                sys.exit(0)
            
            changer = SSHPasswordChangerUbiquiti(username, current_password)
            changer.change_passwords_in_range(base_ip, start_octet, end_octet, new_password)
            
        except KeyboardInterrupt:
            print("\n🚫 Operación interrumpida por el usuario.")
        except ValueError:
            print("\n❌ Error: El valor para los octetos debe ser un número entero.")
        except Exception as e:
            print(f"\n❌ Error inesperado en la aplicación: {e}")

    patched_main()

