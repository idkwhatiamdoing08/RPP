from django.db import models

class Items(models.Model):
    vendor_code = models.CharField('Артикул', max_length=8)
    name = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.vendor_code

    def get_absolute_url(self):
        return f'/main/{self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ItemQuantity(models.Model):
    vendor_code = models.OneToOneField(Items, on_delete=models.CASCADE, primary_key=True)
    quantity = models.IntegerField('Количество')

    def __str__(self):
        return self.vendor_code

    class Meta:
        verbose_name = 'Количество товара'
        verbose_name_plural = 'Количество товаров'


class Orders(models.Model):
    id = models.IntegerField('Идентификатор', primary_key=True)
    date = models.DateField('Дата')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderContent(models.Model):
    id = models.ForeignKey(Orders, primary_key=True, on_delete=models.CASCADE)
    vendor_code = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Содержание заказа'
        verbose_name_plural = 'Содержание заказов'

class Clients(models.Model):
    client_id = models.IntegerField('Индентификатор клиента')
    name = models.CharField('Имя', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class ClientsOrders(models.Model):
    id = models.ManyToManyField(Orders)
    client_id = models.ManyToManyField(Clients)

    def __str__(self):
        return self.client_id

    class Meta:
        verbose_name = 'Заказ клиента'
        verbose_name_plural = 'Заказы клиентов'


















