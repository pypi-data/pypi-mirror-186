# TexPj

Es una forma sencilla para manejar plantillas de LaTeX.

## Instalar plantilla con git

Si es desde **Github** puede simplemente referirse a USUARIO/PROYECTO, en otro
caso active la bandera de url para clonar directamente desde el link.

### Ejemplos

```
texpj install BenyaminGaleano/report reporte "reportes para electrónica"
```


**Explicación:** texpj install recibe el Usuario y el nombre con el que se va a registrar
en este caso se podrá hacer uso de la plantilla a través de **reporte**, y sólo funcionaría si el
repositorio pertenece a **Github**, la descripción es opcional.

```
texpj install https://github.com/BenyaminGaleano/report.git "reportes para electrónica" reporte --url
```

**Explicación:** al igual que el anterior instala la plantilla con el nombre **reporte**, pero esta forma funciona con cualquier url compatible con git.


## Comandos disponibles

  * **add**      Registra DIRECTORY como una plantilla de latex y lo identifica...
  * **create**   Crea una copia del template registrado como ALIAS en la posición...
  * **install**  Instala el TEMPLATE de forma local y lo regitra como ALIAS.
  * **launch**   Se encarga de abrir los archivos (primitivo).
  * **list**     Lista todas las posibles plantillas guardadas.
  * **remove**   Elimina la plantilla identificada como ALIAS, si es un enlace...
  * **update**   Actualiza el template identificado con el ALIAS.
  * **describe** cambiar la descripción de una plantilla.


