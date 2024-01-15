from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField()
    quantity = models.IntegerField()
    image = models.FileField(upload_to='products/')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=255)
    age = models.IntegerField()
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

    class Meta:
        db_table = 'cart'
        verbose_name = 'cart'
        verbose_name_plural = 'cart'

    def __str__(self):
        return self.customer


class Order(models.Model):
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    total = models.FloatField()
    address = models.TextField()
    status = models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'),('delivered', 'delivered')], default='pending', max_length=255)

    class Meta:
        db_table = 'order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

class OrderDetails(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

    class Meta:
        db_table = 'order_details'
        verbose_name = 'order_details'
        verbose_name_plural = 'order_details'