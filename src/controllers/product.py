from src.models.product import (create_product, del_product)

from src.server.database import connect_db, db, disconnect_db

async def product_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()

    product_collection = db.product_collection

    product = { 
            "name" : "Secador",
            "description" : "Secador para cabelos bivolt",
            "price" : 2999.89,
            "code" : "CHAP103"}
    
    code = "CHAP100"

    if option == '1':
        product = await create_product(
            product,
            product_collection
        )
        print("Product added")

    if option == "2":
        product = await del_product(
            product_collection,
            product["code"]
        )
        print("Product Removed")


    await disconnect_db()
           
    