Requisitos
-pytest (pip install pytest)

Proyecto
En este proyecto en el  archivo de test_integracion.py prueba el funcionamiento real entre:

-Clientes TCP
-Comunicación con el servidor
-Recepción simultánea mediante threads
-Envío entre múltiples conexiones
-Manejo de desconexiones

Características probadas:

-Dos clientes se conectan al servidor
-Un cliente envía un mensaje
-El servidor reenvía correctamente el mensaje al destinatario
-El emisor no recibe su propio mensaje
-Un cliente desconectado no causa fallos
-El sistema sigue funcionando aunque un cliente cierre la conexión 

Objetivo del Proyecto
-Este proyecto permite aprender y practicar:
-Validación de datos antes de enviarlos por red
-Manejo de sockets TCP en Python
-Hilos para recibir mensajes en paralelo
-Diseño de pruebas unitarias e integración con pytest
-Detección temprana de errores en sistemas distribuidos
