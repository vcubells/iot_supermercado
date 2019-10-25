# Demo 7. Generación de tableros analíticos

Este demo muestra como ejecutar una consulta en [BigQuery](https://cloud.google.com/bigquery/) y, a partir de los resultados, generar un dashboard en [Data Studio](https://datastudio.google.com/).  

IMPORTANTE!!!

Este demo es una continuación del [demo_06](../demo_06), por lo tanto, utiliza los recursos generados en el mismo. Si aún no ha realizado el [demo_06](../demo_06), necesita comenzar por ahí.


## 1. Pre-requisitos

* Haber realizado el [demo_06](../demo_06).
* Una laptop o desktop con Linux o MacOS.
* Tener una cuenta activa en [Google Cloud Platform](https://cloud.google.com/).
* Tener instalado el [Google Cloud SDK](https://cloud.google.com/sdk/).
* Acceso a Internet.



## 2. Instrucciones de uso

### 2.1. Generación de tableros en Data Studio

1. Acceda a la [Consola de Google Cloud Platform](https://console.cloud.google.com) y seleccione el mismo proyecto utilizado en el [demo_06](../demo_06).

![Seleccionar el proyecto](../demo_06/img/demo_06_01.png)

2. Dentro de la  consola, en el menú de la izquierda, localice el grupo titulado **BIG DATA** y seleccione la opción BigQuery.

![Acceder a BigQuery](../demo_06/img/demo_06_06.png)

3. Localice el nombre de la tabla creada y seleccione la opción **Vista previa**. Deberá ver algunos registros similares a los que aparecen en la siguiente imagen:

![Vista previa de la tabla](../demo_06/img/demo_06_12.png)

4. En el editor de consultas, escriba la siguiente sentencia SQL y de clic en el botón **Ejecutar**.

```sql
SELECT ts, temperature, pressure, humidity
FROM semana_i.telemetry
```

![Ejecutar consulta SQL](img/demo_07_01.png)

5. En la sección titulada **Resultados de la consulta** seleccione la opción **Explorar con Data Studio**.

![Explorar en Data Studio](img/demo_07_02.png)

6. Se abrirá la [Consola de Data Studio](https://datastudio.google.com). Modifique el nombre en la parte superior izquierda y, posteriormente, de clic en el nombre del dataset.

![Adicionar conjunto de datos](img/demo_07_03.png)

7. Seleccione el botón **Crear nueva fuente de datos**.

![Adicionar fuente de datos](img/demo_07_04.png)

8. Seleccione la opción BigQuery.

![Acceder a BigQuery](img/demo_07_05.png)

9. Seleccione la tabla que contiene las mediciones de los sensores y luego seleccione el botón **Conectar**.

![Seleccione el conjunto de datos](img/demo_07_06.png)

10. En la siguiente pantalla, modifique el tipo de dato del campo `ts` tal como se muestra en la imagen  y de clic en el botón **Aplicar**.

![Crear conjunto de datos](img/demo_07_07.png)

11. De clic en el menú de tres puntos que aparece a la izquierda y en el menú de opciones seleccione la opción **Eliminar**.

![Eliminar listado](img/demo_07_08.png)

12. Adicione una nueva gráfica tal como se muestra en la imagen.

![Adicionar gráfica](img/demo_07_09.png)

13. Adicione las métricas que desee visualizar en la gráfica. Los cambios realizados se muestran en tiempo real.

![Tablero con mediciones](img/demo_07_10.png)

14. (Opcional) Diseñe un tablero más elaborado como el que se muestra a continuación.

![Tablero con varias mediciones](img/dashboard.png)


### 2.2. Felicidades!!! 
Has completado el demo satisfactoriamente.


## 3. Recursos

Para conocer más sobre Data Studio consulte la [documentación oficial](https://datastudio.google.com/).

Para conocer más sobre BigQuery consulte la [documentación oficial](https://cloud.google.com/bigquery/).

Para conocer más sobre Google Cloud Platform consulte la documentación oficial disponible en  [GCP Documentation](https://cloud.google.com/docs/).

