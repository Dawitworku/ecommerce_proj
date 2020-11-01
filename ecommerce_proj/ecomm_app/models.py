from django.db import models

# Create your models here.
LABEl = (
    ('N', 'New'),
    ('BS', 'Best Seller'),
    ('MP', 'Most Popular')
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    preview_text = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField(null=True)
    # how can i create this product using django admin
    label = models.CharField(choices=LABEl, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category():
    title = models.CharField(max_length=255)
    product = models.ManyToManyField(Product, related_name="categories")

class Image(models.Model):
    img_name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, blank=True, null = True)
    date_added = models.DateTimeField(auto_now_add = True)				
    updated_at = models.DateTimeField(auto_now = True)


class Review():
    pass


class Cart():
    pass


class Order(models.Model):
    # user = models.ForeignKey('Login-Reg_app.User',related_name="orders", on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    # user = models.ForeignKey('Login-Reg_app.User',related_name="orders", on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_prod", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class BillingProfile(models.Model):
    # user = models.OneToOneField(User, null=True, blank=True)  #####
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
