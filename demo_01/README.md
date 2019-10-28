# Demo 1. Preparación de la Raspberry Pi

La Raspberry Pi es un ordenador de bajo coste y tamaño reducido, tanto es así que cabe en la palma de la mano, pero puedes conectarle un televisor y un teclado para interactuar con ella exactamente igual que cualquier otra computadora.

Para ponerlo en marcha tenemos que conectar conectar periféricos de entrada y salida para poder interactuar como una pantalla, un ratón y un teclado y grabar un sistema operativo para Raspberry Pi en la tarjeta SD. Ya solo queda conectarlo a la corriente y estamos listos para funcionar.

Este demo aprenderemos como configurar desde cero nuestra Raspberry Pi.


## 1. Pre-requisitos

* Una laptop o desktop con Linux o MacOS.
* Descargar la Imagen [Raspbian Buster](https://downloads.raspberrypi.org/raspbian_full_latest).
* Descargar el software [Etcher](https://balena.io/etcher/) que permite instalar una imagen en una tarjeta SD/micro SD. Diponible para OSX, Linux.
* Acceso a Internet.
* Tener instalado `git`, `python 3.7`, `pip`, `wget` y `openssl`.
* Teclado y mouse.
* Tener instalado VNC para el acceso remoto. (`opcional`)
* Instalar las librerias extras
## 2. Estructura del proyecto

A continuación se describen los archivos que forman parte del demo, así como la función que juega cada uno de ellos:
- [01_Sensors.py](01_Sensors.py): En este archivo tenemos las configuraciones basicas para el uso de hardware
(`boton`, `web_cam`,`led`, [DHT_SENSOR](https://github.com/adafruit/Adafruit_Python_DHT)).

- [02_Firebase-upload.py](02_Firebase_upload.py): Este documento contiene la configuracion para enviar un archivo a firebase.
- [03_Cognitive-services.py](03_cognitive_services.py): Con este archivo podras enviar peticiones a servicios cognitivos de Microsoft Azure [Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/).


## 3. Instrucciones de uso

Para iniciar la primer practica necesitamos tener el repositorio [iot_supermercado.](git@github.com:vcubells/iot_supermercado.git) actualizado en tu Raspberry pi

- Instalar la imagen Raspbian en la micro SD.
    
    BONUS: ALTERNATIVA EN LINUX Y OSX

    En la mayoría de distribuciones Linux no necesitamos el uso de herramientas de terceros para instalar la imagen en la tarjeta SD/micro SD. Simplemente necesitaremos la consola de comandos.

    En primer lugar, determinamos la partición que corresponde a la tarjeta con el siguiente comando.

    `df -h`    
    Una vez determinada la partición, desmontamos la unidad. Por ejemplo, suponiendo que la partición de la tarjeta sea /dev/sdb1, ejecutamos el siguiente comando (sustituir por la unidad correspondiente a vuestro equipo).

    `umount /dev/sdb1`

    Finalmente, instalamos la imagen que hemos descargado a la tarjeta SD/micro SD usando el siguiente comando.

    `unzip -p NombreImagen.zip | sudo dd of=/dev/sdb bs=4M conv=fsync`

    donde debemos sustituir 'NombreImagen' por el nombre del archivo que hemos descargado (que depende de la versión actual),y /dev/sdb por la unidad de la tarjeta de memoria en nuestro equipo.

    Si en lugar de haber descargado el fichero Zip tenemos el fichero Img, podemos usar este comando.

    `sudo dd bs=4M if=NombreImagen.img of=/dev/sdb`    

### 3.4. Felicidades!!! 
Has completado el demo satisfactoriamente.



## 4. Recursos

Para conocer más sobre Rapbian consulte la [documentación oficial](https://www.raspberrypi.org/downloads/raspbian/).

Para conocer más sobre Microsoft Azure Cognitive Services consulte la [documentación oficial](https://azure.microsoft.com/en-us/services/cognitive-services/).

Para conocer más sobre Google Firebase consulte la documentación oficial disponible en  [documentación oficial](https://firebase.google.com/).
