== Proceso de Ejecucion:

    Es necesario tener instalado Python en el sistema operativo

    1. Tener activado el ambiente: ejecutar \Scripts\activate.bat
    2. Ejecutar el proyecto: python main.py

    los servicios se exponen por el puerto:
    http://localhost:5000/

    El servicio para listar las personas que han realizado la compra en la empresa 123 es:

    Metodo GET:  http://localhost:5000/persona

    
    El servicio para agregar una nueva persona que realiza la compra en la empresa 123 es:

    Metodo POST: http://localhost:5000/persona 
    Body JSON: {
        "codigo": ,
        "identificacion": "",
        "nombres": "",
        "apellidos": "",
        "telefono": "",
        "direccion": "",
        "perfilCompra": ,
        "valorCompra":
    } 