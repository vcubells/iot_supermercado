# Demo 2. Conexión de sensores básicos

Este demo muestra el armado de los diferentes sensores en la tabla de pruebas (Protoboard) así como su conexión con la Rapberrypi.

## 1. Pre-requisitos

* Una laptop o desktop con Linux o MacOS.
* Tener instalado `git`, `python 3.7`, `pip`, `wget` y `openssl`.
* Acceso a Internet.
* Pinzas de corte.
* Pinza de punta.
* Protoboard.
* 3 Resistencias de 180 Ohms.
* 2 Switch's.
* 1 Buzzer.
* 2 Led's
* 1 Sensor de Temperatura.
* Cables de conexión.

## 2. Estructura del proyecto

A continuación se describen los archivos que forman parte del demo, así como la función que juega cada uno de ellos:

- [img](img): En la carpeta de imágenes se encuentran los diagramas necesarios para poder armar en la tabla de pruebas los circuitos.
- - [diagrama_01.png](img/diagrama_01.png) - Diagrama del circuito buzzer.
- - [diagrama_02.png](img/diagrama_02.png) - Diagrama del circuito led.
- - [diagrama_03.png](img/diagrama_03.png) - Diagrama del circuito botón.
- - [diagrama_04.png](img/diagrama_04.png) - Diagrama del circuito de temperatura.
- [01_Sensors.py](01_Sensors.py): En este archivo tenemos las configuraciones básicas para el uso de hardware (botón, web_cam,led, DHT_SENSOR) así como el código necesario para poder poner en marcha con la Rapberrypi.

## 3. Instrucciones de uso

Para iniciar la primer practica necesitamos tener el repositorio [iot_supermercado.](git@github.com:vcubells/iot_supermercado.git) actualizado en tu Raspberry pi.

Posteriormente es necesario realizar las conexiones necesarias para el armado de los [diagrama_01.png](img/diagrama_01.png), [diagrama_02.png](img/diagrama_02.png), [diagrama_03.png](img/diagrama_03.png) y [diagrama_04.png](img/diagrama_04.png).

Recuerda que es muy importante tomar en cuenta la polaridad de los componentes como lo son el buzzer [buzzer.png](img/buzzer.png)y los led's [led.png](img/led.png).

Una vez armado los circuitos es necesario realizar una prueba de cada uno de ellos corroborando:

1. El buzzer suene al momento de que el botón es presionado.
2. El led encienda cuando se alimente el circuito como lo muestra el [diagrama_05.png](img/diagrama_05.png).
3. El led se encienda al momento de que el botón es presionado.

Realizadas las pruebas de cada uno de los circuitos, procedemos a conectar cada uno de los circuitos en la posición indicada (cuadro azul) en la Raspberry pi como lo muestra la siguiente imagen.

### 3.4. Felicidades!!!

Haz armado y conectado tus primeros circuitos en tu Raspberrypi satisfactoriamente.

## 4. Recursos
Para conocer más sobre Rapbian consulte la [documentación oficial](https://www.raspberrypi.org/downloads/raspbian/).