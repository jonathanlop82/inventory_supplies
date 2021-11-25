import db
import MySQLdb
import peewee
import datetime
import os
import pandas

title = """
   _____                   _ _             _____                      _                   
  / ____|                 | (_)           |_   _|                    | |                  
 | (___  _   _ _ __  _ __ | |_  ___  ___    | |  _ ____   _____ _ __ | |_ ___  _ __ _   _ 
  \___ \| | | | '_ \| '_ \| | |/ _ \/ __|   | | | '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
  ____) | |_| | |_) | |_) | | |  __/\__ \  _| |_| | | \ V /  __/ | | | || (_) | |  | |_| |
 |_____/ \__,_| .__/| .__/|_|_|\___||___/ |_____|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
              | |   | |                                                              __/ |
              |_|   |_|                                                             |___/ 
"""

database = peewee.MySQLDatabase(db.DATABASE, host=db.HOST, port=db.PORT, user=db.USER, passwd=db.PASSWORD)

class User(peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=50, null=True)
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'users'

class Vendors(peewee.Model):
    id = peewee.AutoField()
    name = peewee.CharField()
    webpage = peewee.CharField()

    class Meta:
        database = database
        db_table = 'vendors'

class Items(peewee.Model):
    id = peewee.AutoField()
    name = peewee.CharField()
    description = peewee.CharField()
    cant = peewee.IntegerField()
    vendor_id = peewee.ForeignKeyField(Vendors)

    class Meta:
        database = database
        db_table = 'items'


def menu():

    print(title)
    print("Sistema de Gestion de Inventario de Insumos IT")
    print()
    print("Seleccione una opcion")
    print("1: Consultar todos los datos")
    print("2: Buscar un registro por nombre")
    print("3: Insertar un nuevo registro")
    print("4: Actualizar un registro")
    print("5: Agregar compra de Insumos")
    print("6: Efectuar acta de entrega de Insumos")
    print("7: Descargar inventario en Excel")
    print("0: Salir")


def select_items():
    query = Items.select().dicts()
    titulo = "LISTADO DE INVENTARIO DE INSUMOS"
    print("            {}".format(titulo))
    print()
    print ("{:<10} {:<20} {:<40} {:<10} {:<10}".format('ID','NAME', 'DESCRIPTION', 'QUANTITY','VENDOR ID'))

    for row in query:
        id, name, description, cant, vendor = row.values()
        print ("{:<10} {:<20} {:<40} {:<10} {:<10}".format(id, name, description, cant, vendor))

    print()
    print()
    x = input()

def insert_item():
    while True:
        item_name = input("Nombre del item: ")
        item_description = input("Descripcion del item: ")
        item_cant = 0
        item_vendor = int(input("Seleccione vendor 1:Dell 2:Zebra 3:HID"))

        item = Items(name=item_name, description=item_description, cant=item_cant, vendor_id=item_vendor)
        item.save()
        print("Item ingresado!!!")
        print()
        salir = input("Desea ingresar otro registro S o N")

        if salir == 'N' or salir == 'n':
            break

def run():

    # Create Tables
    if not(User.table_exists()):
        User.create_table()

    if not(Vendors.table_exists()):
        Vendors.create_table()
    
    if not(Items.table_exists()):
        Items.create_table()
    
    while True:
        
        #Imprimir menu
        os.system("clear")
        menu()
        option = int(input("Seleccione una opcion: "))

        if option == 1:
            select_items()

        if option == 3:
            insert_item()

        if option == 0:
            break
    

if __name__ == '__main__':
    run()