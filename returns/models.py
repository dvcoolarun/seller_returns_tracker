from django.db import models
from orders.models import Order

class ReturnRequest(models.Model):
    RETURN_REASON_CHOICES = [
        ('DAMAGED', 'Item Damaged'),
        ('INCORRECT', 'Incorrect Item'),
        ('DEFECTIVE', 'Defective'),
        ('NOT_NEEDED', 'No Longer Needed'),
        ('SIZE_ISSUE', 'Wrong Size'),
        ('OTHER', 'Other')
    ]

    RETURN_STATUS_CHOICES = [
        ('REQUESTED', 'Return Requested'),
        ('APPROVED', 'Return Approved'),
        ('REJECTED', 'Return Rejected'),
        ('PROCESSED', 'Return Processed')
    ]

    order = models.OneToOneField(
        Order, 
        related_name='return_request',
        on_delete=models.CASCADE
    )

    reason = models.CharField(
        max_length=20, 
        choices=RETURN_REASON_CHOICES
    )

    status = models.CharField(
        max_length=20, 
        choices=RETURN_STATUS_CHOICES, 
        default='REQUESTED'
    )

    return_tracking_number = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
    )

    return_date = models.DateTimeField(auto_now_add=True)
    additional_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Return Request for Order {self.order.order_id}"

