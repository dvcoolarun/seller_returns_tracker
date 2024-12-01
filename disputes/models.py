from django.db import models
from orders.models import Order
from returns.models import ReturnRequest

class DisputeCase(models.Model):
    DISPUTE_STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('UNDER_REVIEW', 'Under Review'),
        ('CLOSED', 'Closed'),
        ('RESOLVED', 'Resolved'),
        ('REJECTED', 'Rejected')
    ]

    order = models.OneToOneField(
        Order, 
        related_name='dispute_case',
        on_delete=models.CASCADE
    )

    return_request = models.OneToOneField(
        ReturnRequest, 
        related_name='dispute_case',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


    dispute_reason = models.TextField()

    status = models.CharField(
        max_length=20, 
        choices=DISPUTE_STATUS_CHOICES, 
        default='OPEN'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolution_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Dispute Case for Order {self.order.order_id}"