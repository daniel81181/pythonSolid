# Comentarios sobre ejercicio
¿Cual es su entrada? Los datos de entrada provienen  del url: http://www.imdb.com/chart/top
¿Que procesamiento esta haciendo? Se procesa la informacion dada con la url, y se traen los datos mas relevantes de cada pelicula.
¿Cual es su salida? Los datos de estas peliculas en csv


1. S - Single Responsibility : Cada clase tiene una sola funcion que ayuda a crear el archivo final
2. O - Open Closed Principle : El codigo es entendible con cada una de las clases y respectivas funciones.
3. L - Liskov Substitution Principle : Si se desea el utilizar el codigo para expandir su funcionamiento, este codigo no necesitara modificacion.
4. I - Interface Segregation Principle : No es redundante el codigo y/o existen algunas funciones o clases incesearias
5. D - Dependency Inversion : No hay dependencia

# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME