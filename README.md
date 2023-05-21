# Proyecto Django con Postgres

Este repositorio contiene un proyecto Django que utiliza Postgres como base de datos. A continuación se describen los pasos para configurar y ejecutar el proyecto.

## Instalación

1. Clona el repositorio en tu máquina local:

   ```
   git clone https://github.com/Galaoox/django-basic-course-fazt
   cd https://github.com/Galaoox/django-basic-course-fazt
   ```

2. Instala las dependencias utilizando Docker:

   ```
   make install_deps
   ```

## Configuración

1. Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

2. Configura las variables de entorno en el archivo `.env` según tus preferencias. Asegúrate de configurar las variables relacionadas con la base de datos Postgres.

## Uso

El proyecto proporciona una serie de comandos Make para facilitar la ejecución de tareas comunes:

- `make build`: Construye las imágenes de Docker necesarias para el proyecto.
- `make start`: Inicia los contenedores de Docker.
- `make stop`: Detiene los contenedores de Docker.
- `make migrate`: Ejecuta las migraciones de la base de datos.
- `make makemigrations`: Crea las migraciones de la base de datos.
- `make install_deps`: Instala las dependencias del proyecto especificadas en el archivo `requirements.txt`.
- `make run_command cmd="<COMANDO>"`: Ejecuta un comando personalizado en el contenedor de Docker.
- `make reset_db`: Detiene y elimina los contenedores de Docker, elimina los datos de la base de datos y vuelve a iniciar los contenedores. Además, ejecuta las migraciones de la base de datos.

## Configuración

1. Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

2. Crea un archivo `.env` en la raíz del proyecto y configura las siguientes variables de entorno según tus preferencias:

   ```plaintext
   DATABASE_NAME=postgres
   DATABASE_USER=postgres
   DATABASE_PASSWORD=postgres
   DATABASE_HOST=db
   DATABASE_PORT=5432
   SECRET_KEY=<tu_clave_secreta>
   ```

   Asegúrate de reemplazar `<tu_clave_secreta>` con una clave segura de tu elección.

   Estas variables de entorno se utilizarán para configurar la base de datos Postgres y la clave secreta utilizada por Django.

   **Nota:** Es importante mantener la seguridad de la clave secreta y no compartirla públicamente.

## Uso

El proyecto proporciona una serie de comandos Make para facilitar la ejecución de tareas comunes:

- `make build`: Construye las imágenes de Docker necesarias para el proyecto.
- `make start`: Inicia los contenedores de Docker.
- `make stop`: Detiene los contenedores de Docker.
- `make migrate`: Ejecuta las migraciones de la base de datos.
- `make makemigrations`: Crea las migraciones de la base de datos.
- `make install_deps`: Instala las dependencias del proyecto especificadas en el archivo `requirements.txt`.
- `make run_command cmd="<COMANDO>"`: Ejecuta un comando personalizado en el contenedor de Docker.
- `make reset_db`: Detiene y elimina los contenedores de Docker, elimina los datos de la base de datos y vuelve a iniciar los contenedores. Además, ejecuta las migraciones de la base de datos.

Recuerda ejecutar `make install_deps` antes de iniciar el proyecto por primera vez para instalar las dependencias necesarias.

Si deseas personalizar algún aspecto del proyecto, puedes modificar los archivos de configuración en la carpeta del proyecto según tus necesidades.

## Contribución

Si deseas contribuir a este proyecto, sigue los siguientes pasos:

1. Crea un nuevo branch para realizar tus modificaciones:

   ```
   git checkout -b nombre-del-branch
   ```

2. Realiza tus modificaciones y realiza commit de los cambios:

   ```
   git commit -m "Descripción de los cambios"
   ```

3. Sube tus cambios al repositorio:

   ```
   git push origin nombre-del-branch
   ```

4. Crea un pull request en GitHub para que tus cambios sean revisados e integrados en la rama principal.

## Licencia

Este proyecto se encuentra bajo la Licencia [MIT](LICENSE).