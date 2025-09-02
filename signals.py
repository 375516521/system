from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment
from apps.fees.models import FeeInvoice
from apps.notifications.models import NotificationLog

@receiver(post_save, sender=Payment)
def payment_post_save(sender, instance, created, **kwargs):
    # Very simple: mark first unpaid invoice as paid proportional to payment amount
    try:
        invoices = FeeInvoice.objects.filter(balance__gt=0).order_by('due_date')
        amount = instance.amount
        for inv in invoices:
            if amount <= 0: break
            apply = min(amount, float(inv.balance))
            inv.balance = float(inv.balance) - apply
            inv.save()
            amount -= apply
        # create notification log
        NotificationLog.objects.create(channel='sms', recipient='admin', message=f'Payment {instance.reference} processed.')
    except Exception as e:
        pass
