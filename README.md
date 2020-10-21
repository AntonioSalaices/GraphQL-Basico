1.- Instalar e inicializar virtual environment con el siguiente comando en el shell: 
python - venv myapi(o nombre que le quieras poner al entorno virtual), la versión de python utilizada es Python 3.7.3

2.- En el repositorio está el archivo requirements.txt, procederemos a instalar las dependencias necesarias con los siguiente pasos y comando: Primero nos ubicaremos en la carpeta del entorno virtual myapi/Scripts y una vez dentro, escribiremos "activate" para activar el entorno virtual, una vez activado escribiremos el siguiente comando: "pip install -r requirements.txt", esto nos instalará las dependencias necesarias para correr la api.

3.- Una vez instaladas las dependencias, procederemos a crear la bd en phpmyadmin con el nombre "api_superavila", y a continuación
ponemos el siguiente comando en consola para que el ORM SqlAlchemy genere las tablas automáticamente: "python main.py"

4.- La api está corriendo y lista para usarse.
