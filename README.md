Aplicación de Cambio Masivo de Contraseñas para Antenas Ubiquiti
Esta aplicación está diseñada para simplificar el proceso de actualización de contraseñas en múltiples antenas Ubiquiti dentro de un rango de red específico.

Funcionalidades Principales
Cambio Masivo de Contraseñas: Modifica la contraseña de acceso de tus puntos de acceso Ubiquiti de forma eficiente.
Gestión por Rango de IPs: Especifica un rango de direcciones IP para aplicar los cambios de contraseña, asegurando que solo los dispositivos deseados sean actualizados.
Interfaz Sencilla: Proporciona una forma intuitiva de ingresar la información necesaria para el proceso.
Requisitos
Python 3.x
Bibliotecas necesarias (se detallarán en la sección de instalación).
Instalación
Clonar el Repositorio:

git clone https://github.com/ramonmtz/passchange.py

cd passchange
Instalar Dependencias:

pip install paramiko

Uso
Ejecutar la Aplicación:

python passchange.py
Ingresar Datos: La aplicación te solicitará la siguiente información:

Rango de IPs: Introduce el rango de direcciones IP de las antenas Ubiquiti que deseas actualizar (ej. 192.168.1).

Rango del ultimo Octeto: Introduce el rango de direcciones ip que quieras para cambiar la password (ejem: 10)

Contraseña Antigua: La contraseña actual de acceso a las antenas.

Nueva Contraseña: La nueva contraseña que deseas establecer.

Proceso de Actualización: La aplicación iterará sobre el rango de IPs proporcionado, se conectará a cada antena Ubiquiti y aplicará la nueva contraseña.

Consideraciones de Seguridad
Maneja las contraseñas con cuidado. Considera el uso de variables de entorno o métodos de gestión de secretos para evitar exponer credenciales en el código fuente.
Asegúrate de que tu red esté protegida y que solo los dispositivos autorizados puedan acceder a las antenas.
Contribuciones
¡Las contribuciones son bienvenidas! Si tienes alguna mejora o corrección, por favor, abre un issue o envía un pull request.
