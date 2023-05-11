# API REST para Simulación check-in Aerolínea, reto técnico.

## Explicación de la solución

Este es un proyecto de API REST para realizar el check-in automático de pasajeros de una aerolínea. Sin embargo ahora está aún en construcción.

La solución implementada utiliza **Python** con el **framework FastAPI** para crear la API rest y una conexión con una base de datos **MySQL**.

Por el momento, 
- Logra conectarse a la base de datos.
- Logra controlar la reconexión, dado que el servidor está configurado para que todas aquellas conexiones inactivas por más de 5 segundos sean abortadas.
- Los campos en la BD están llamados en Snake case, pero en la respuesta de la API son transformados a Camel case.
- Logra manipular la data para construir una estructura de respuesta exitosa.
- La estructura de la respuesta exitosa contiene una lista de objetos de pasajeros con sus atributos y añade los atributos de boarding_pass requeridos:

    {
        passengerId: passengerId
        dni: dni
        name: name
        age: age
        country: country
        boardingPassId: boardingPassId
        purchaseId: purchaseId
        seatTypeId: seatTypeId
        seatId: seatId
    }

## Requisitos

- Python 3.x
- Entorno virtual (recomendado)
- MySQL

## Instalación

1. Clonar el repositorio:

    https://github.com/KamilaOjeda/Simulacion-check-in


2. Instalar las dependencias:

    **pip install -r requirements.txt**


## Uso

1. Activar el entorno virtual (opcional):

    **source venv/bin/activate**    


2. Iniciar la aplicación:

    **uvicorn app.main:app --reload**


3. Acceder al endpoint **/passengers_with_boarding_pass** para ver la lista de pasajeros.

## Documentación

Para ver la documentación de la API, acceder a la siguiente URL:

    http://localhost:8000/docs


## Notas

- La API logra conectarse con una base de datos de motor MySQL externa, y controla la reconexión.
- El endpoint /passengers_with_boarding_pass, muestra una lista con todos los pasajeros con los mismos atributos de la API, pero incluye los atributos necesarios de la tabla de boarding_pass.
- Este es un proyecto incompleto, pero logra conectarse a la base de datos y manipular la data para construir una estructura de respuesta.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.

## Autor
by Kamila Ojeda
