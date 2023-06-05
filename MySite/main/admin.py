from django.contrib import admin
from .models import Items
from .models import ItemQuantity
from .models import Orders
from .models import OrderContent
from .models import Clients
from .models import ClientsOrders

admin.site.register(Items)

admin.site.register(ItemQuantity)

admin.site.register(Orders)

admin.site.register(OrderContent)

admin.site.register(Clients)

admin.site.register(ClientsOrders)
