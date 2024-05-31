from enum import Enum

class OrderStatus(Enum):
    CREATED = 'Creado'
    PAYED = 'Pagado'
    COMPLETED = 'Completado'
    CANCELED = 'Cancelado'

choices = [(tag, tag.value) for tag in OrderStatus]