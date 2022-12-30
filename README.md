# desici-test
Proyecto de evaluación de desarrollo para el puesto backend developer en DeSiCi.

Stack tecnológico:

-Backend: 

	python 3.8.10
	
	Django 3.2.16
	
-Frontend:

	HTML
	
	Javascript
	
	Jquery 3.6.3
	
	Bootstrap 5.3
	
-BD:

	Mysql
	


Este proyecto sirve de base para la generación de una agenda,  haciendo uso de python y django, en la parte del backend y hml, css y javascript en la parte de frontend.


Para creación del entorno virtual es necesario tener instalado 
Python y una vez instalado ejecutar el siguiente comando dentro 
de nuestro cmd:

	python3 -m venv venv


Para acceder al entorno es necesario ejecutar la siguiente linea:


	en sistemas operativos Windows: myvenv\Scripts\activate
	en sistemas operativos Linux: source myvenv/bin/actívate


Una vez dentro de nuestro entorno virtual podremos instalar
nuestros paquetes requeridos, que se encuentran especificados en 
el documento requirements.txt, ejecutando el siguiente comando


	pip install -r requirements.txt


Se genero una app dentro de la carpeta de apps esta fue llamada 
‘phonebook’, traducción de agenda telefónica. Para ello se usaron los comandos:

	django-admin startapp ./apps/phonebook


Dentro de esta app se generaron los modelos requeridos para la 
agenda.

Se utilizó la siguiente configuración dentro 
de la base de datos, la cual debe ser generada por medio de una
herramienta visual o bien, por medio del cmd con los siquientes 
comandos:


	-CREATE DATABASE phonebook;
	-CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
	-GRANT ALL PRIVILEGES ON `phonebook` . * TO 'root'@'localhost';
	FLUSH PRIVILEGES; 



	DATABASES = {
  	  'default': {
      'HOST': '127.0.0.1',
      'PORT': '3307',
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'phonebook',
      'USER': 'root',
      'PASSWORD': 'root',
    }
 

Una vez creada nuestra base de datos deberán ejecutarse los 
siguientes comandos para poder crear nuestras tablas que 
previamente fueron generadas en el archivo models.py

		python manage.py makemigrations
		python manage.py migrate


Dentro de la base de datos se tradujeron los campos a su versión 
más acode del inglés por lo cual quedaron de la siguiente manera:

	Contacto => Person
  	 	 nombre => name 
    	appellidos => last_name
    	fotografia => picture 
    	Fecha de Nacimiento => birth_date

	Dirección => Address
  	 	 Calle => street_name 
    	Numero externo => external_number
    	Numero interno => internal_number
    	Colonia => settlement
    	Municipio => district
    	Estado => state
    	Referencias => references
    	Id de relación con la table persona => person

	Teléfono => Phone
  		  Tipo => type
    	Alias => alias   
    	Numero => number
    	Id de relación con la table persona => person


Y finalmente una vez ejecutados estos pasos solo nos queda ejecutar el siguiente comando:

	  python manage.py runserver

y podremos dirigirnos a la url para poder acceder al proyecto:

		127.0.0.1:8000/phonebook/person
