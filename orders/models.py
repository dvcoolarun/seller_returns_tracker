from django.db import models

class Order(models.Model):

    ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled')
    ];

    order_id = models.CharField(max_length=50, unique=True)

    # Customer details directly in the Order model
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=50)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='PENDING')


    def __str__(self):
        return  f"Order {self.order_id} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    
    # Product details directly in the OrderItem model
    product_name = models.CharField(max_length=300)
    product_description = models.TextField(null=True, blank=True)
    
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_name} - {self.order.order_id}"
