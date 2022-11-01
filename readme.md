# Api Rest Flask y PostgreSQL

Aplicación sencilla para el manejo de una API Rest con Flask y la base de datos PostgreSQL, se puede solicitar la información de los usuarios y agregar nuevos a la base, así como actualizarlos o borrarlos.

Se ira agregando funciones de manejo de usuarios con Flask Login en el futuro.

## Pasos para ejecutarla
---

1. Clonar el repositorio con Git Clone
2. Cambiar de nombre los archivos config_template y .env_template, y cambiar los valores de las variable de entorno

```powershell
cp config_template.py config.py
```

```powershell
cp .env_template .env
```
3. Crear un ambiente virtual
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
