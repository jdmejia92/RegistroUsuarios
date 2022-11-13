# Api Rest Flask y PostgreSQL

Aplicación sencilla para el manejo de una API Rest con Flask y la base de datos PostgreSQL, se puede solicitar la información de los usuarios y agregar nuevos a la base, así como actualizarlos o borrarlos.

Se ira agregando funciones de manejo de usuarios con Flask Login en el futuro.

## Pasos para ejecutarla
---

1. Clonar el repositorio con Git Clone
2. Cambiar de nombre los valores de las variable de entorno
```powershell
cp .env_template .env
```
1. Crear un ambiente virtual
```powershell
python -m venv venv
```
4. Instalar todas las librerías del archivo requirements.txt
```powershell
pip install -r requirements.txt
```

5. Ejecutar el comando
```powershell
flask run
```

## Consultas que se pueden generar

1. **Get users**: obtienes la lista de todos los usuarios en la base de datos
2. **Get user**: obtienes la información de un usuario
3. **Add user**: agregar un usuario a la base de datos
4. **Delete user**: borrar un usuario de la base de datos
5. **Update user**: actualizas todos los datos facilitados de un usuario
6. **Update password**: en caso se cuente con seguridad por rangos de cuenta, aquí los usuarios podrían solo actualizar su contraseña