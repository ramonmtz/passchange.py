🚀 Aplicación de Cambio Masivo de Contraseñas para Antenas Ubiquiti 🚀
¡Simplifica la gestión de tu red Wi-Fi con esta potente herramienta! Diseñada para que actualizar las contraseñas de tus antenas Ubiquiti sea pan comido, incluso cuando tienes muchas. ¡Di adiós a la tediosa tarea manual! 👋

✨ Funcionalidades Principales
Cambio Masivo de Contraseñas: 🔄 Modifica la contraseña de acceso de tus puntos de acceso Ubiquiti de forma eficiente. ¡Así de fácil! 💨
Gestión por Rango de IPs: 🎯 Especifica un rango de direcciones IP para aplicar los cambios de contraseña, asegurando que solo los dispositivos deseados sean actualizados. ¡Control total en tus manos!
Interfaz Sencilla: 🖱️ Proporciona una forma intuitiva de ingresar la información necesaria para el proceso.
📋 Requisitos
🐍 Python 3.x instalado en tu sistema.
📚 Bibliotecas necesarias (detalladas en la sección de instalación).
🛠️ Instalación
Clonar el Repositorio: 📂

git clone https://github.com/ramonmtz/passchange.py

cd passchange
Instalar las Dependencias: 📦

pip install paramiko
▶️ Uso
Ejecuta la Aplicación: 💻

python passchange.py
Ingresa los Datos Solicitados: ✍️

Rango de IPs: Introduce el rango de direcciones IP de las antenas Ubiquiti que deseas actualizar (ej. 192.168.1.). 🌐
Rango del último Octeto: Introduce el rango de direcciones IP que quieras para cambiar la password (ejem: 10).
Contraseña Antigua: La clave de acceso actual. 🔑
Nueva Contraseña: ¡La nueva y segura contraseña que deseas establecer! 🤫
¡Observa la Magia! ✨ La aplicación recorrerá inteligentemente el rango de IPs especificado, se conectará a cada antena Ubiquiti y aplicará la nueva contraseña de forma automática.

🔒 Consideraciones de Seguridad
🔐 Manejo de Credenciales: Trata las contraseñas con la máxima confidencialidad. Considera el uso de variables de entorno o sistemas de gestión de secretos para evitar exponer credenciales directamente en el código fuente.
🛡️ Seguridad de Red: Asegúrate de que tu red esté robustamente protegida y que solo los dispositivos autorizados tengan acceso a tus antenas.
🤝 ¡Únete al Equipo! (Contribuciones)
¡Tus ideas y mejoras son muy valiosas! Si tienes alguna sugerencia o encuentras algún error, no dudes en abrir un issue o enviar un pull request. ¡Hagamos esta herramienta aún mejor juntos! 🙏
