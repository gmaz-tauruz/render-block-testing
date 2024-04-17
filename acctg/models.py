from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


# Create your models here.
class Voucher(models.Model):
    voucher_date = models.DateField()
    payee_name = models.CharField(max_length=250) 
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    particulars = models.CharField(max_length=250)
    
    # check details
    bank_account = models.CharField(max_length=50, null=True, blank=True)
    cheque_num = models.CharField(max_length=50, null=True, blank=True,
                                  validators=[RegexValidator(r'^\d{1,10}$')]) 
    cheque_date = models.DateField(null=True, blank=True)

    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                             on_delete=models.SET_NULL, related_name='approved_vouchers')
    approved_date = models.DateField(null=True, blank=True)

    date_forwarded = models.DateField(null=True, blank=True) # forwarded to bankrecon

    voucher_series = models.IntegerField(null=True, blank=True)

    active = models.BooleanField(default=True)
    locked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                             on_delete=models.SET_NULL)
    
    class Meta:
        ordering =('voucher_date', 'payee_name')

    def __str__(self) -> str:
        return f'Voucher No.: {self.id} | {self.payee_name}'