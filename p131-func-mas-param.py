#p131-func-mas-param.py

def saludatodos(*todos:str)->None:
    #todos es ('Juan','Pedro','Luis')
    for nombre in todos:
        print(f"Saludos a {nombre}")

saludatodos("Juan","Pedro","Luis")