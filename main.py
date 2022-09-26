import asyncio

# USERS
# from src.controllers.users import users_crud

# loop = asyncio.new_event_loop()
# loop.run_until_complete(users_crud())

# ADDRESS
# from src.controllers.address import address_crud

# loop = asyncio.new_event_loop()
# loop.run_until_complete(address_crud())

# PRODUCT
# from src.controllers.product import product_crud

# loop = asyncio.new_event_loop()
# loop.run_until_complete(product_crud())

# ORDER
# from src.controllers.order import order_crud

# loop = asyncio.new_event_loop()
# loop.run_until_complete(order_crud())

# ORDER_ITEMS  
from src.controllers.order_items import order_items_crud

loop = asyncio.new_event_loop()
loop.run_until_complete(order_items_crud())