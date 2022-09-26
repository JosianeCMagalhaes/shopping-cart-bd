from itertools import product
from src.models.orders_items import (create_order_items, get_order_items)
from src.server.database import connect_db, db, disconnect_db

async def order_items_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()

    order_items_collection = db.order_items_collection
    order_collection = db.order_collection

    product1 = "6330dcc1aaefb5b066eb1009"
    product2 = "6330e17d6c7fc5f88cd5d2a5"

    order_items = {
                "order": {
                    "user": {
                        "_id": "6330e0c1eed16368cbb09ee5",
                        "email": "teste2u@gmail.com",
                        "password": "00000045",
                        "is_active": True,
                        "is_admin": True},
                    "paid": True,
                    "create": "2016-05-18T16:00:00Z",
                    "address": {
                        "street" : "Rua Quarenta , Numero 378",
                        "cep" : "8465000",
                        "district" : "São Paulo",
                        "city" : "São Paulo",
                        "state" : "São Paulo",
                        "is_delivery" : False}
        },
                "product": {
                    "_id": "6330e17d6c7fc5f88cd5d2a5",
                    "name" : "Secador",
                    "description" : "Secador para cabelos bivolt",
                    "price" : 2999.89,
                    "code" : "CHAP103"}
        }

    if option == '1':
        order_items = await create_order_items(
            order_items,
            order_items_collection
        )
        print("products entered order ")

    id_order = "6330f3725ec6f7b93da7223a"
    # products = {{"_id": "6330dcc1aaefb5b066eb1009",
    #             "name" : "Chapinha de cabelo",
    #             "description" : "Chapinha para cabelos secos e molhados",
    #             "price" : 1999.89,
    #             "code" : "CHAP100"},
    #             {"_id":"6330e17d6c7fc5f88cd5d2a5",
    #             "name" : "Secador",
    #             "description" : "Secador para cabelos bivolt",
    #             "price" : 2999.89,
    #             "code" : "CHAP103"}}
                        

    if option == '2':
        order_items = await get_order_items(
            id_order,
            order_items_collection,
            product
        )
        print("products entered order ")

        
    if option == '3':
        carrinho = order_items_collection.aggregate([{"$group":{"$product":"$None", "total products":{"$sum":1}}}])
        for document in carrinho:
            print(document)


    await disconnect_db()
           