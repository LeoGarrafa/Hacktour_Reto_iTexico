# Hacktour_Reto_iTexico
Código de Python para generación de reportes.

En la realidad, los siguientes archivos deben correr en paralelo:
  - "IoT_main.py":
    *Este es el que genera reportes en base a la lectura de los sensores.*
  - "sensors_main.py"
    *Éste sólo lee los datos que vienen del puerto serial.*
    
Si desean "simular":
  - Correr sólo "IoT_main.py", pero antes...
  - Comenten las lineas de código dónde aparece "fb_api".
  - Modifiquen el archivo "dict_sensors" para poner diferentes valores a los sensores.
  - Vean resultados en "dummy_report" (generado durante el proceso).
