# [CREAR BACKEND]
````shell
mkdir backend
cd backend 
django-admin startprojetc core .
````

Despues de crear un modelos debemos hacer migracion
```shell
python manage.py makemigrations
python manage.py migrate
```

Si queremos ver los modelos con una API, debemos serializar nuestros modelos