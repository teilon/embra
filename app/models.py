from django.db import models


class ProductItem(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=80)


class ProductSet(models.Model):

    product_item = models.ForeignKey('ProductItem', on_delete=models.CASCADE)
    account = models.IntegerField(default=0)
    transaction = models.ForeignKey('TransactionSet', on_delete=models.CASCADE)
    storage = models.ForeignKey('StorageSet', on_delete=models.CASCADE)

    # m1 = models.IntegerField(default=0)
    # m2 = models.IntegerField(default=0)
    # m3 = models.IntegerField(default=0)
    # m4 = models.IntegerField(default=0)
    # m5 = models.IntegerField(default=0)
    # m6 = models.IntegerField(default=0)
    # m7 = models.IntegerField(default=0)
    # m8 = models.IntegerField(default=0)
    # m9 = models.IntegerField(default=0)
    # m10 = models.IntegerField(default=0)
    # w1 = models.IntegerField(default=0)
    # w2 = models.IntegerField(default=0)
    # w3 = models.IntegerField(default=0)
    # w4 = models.IntegerField(default=0)
    # w5 = models.IntegerField(default=0)
    # w6 = models.IntegerField(default=0)
    # w7 = models.IntegerField(default=0)
    # w8 = models.IntegerField(default=0)
    # w9 = models.IntegerField(default=0)
    # w10 = models.IntegerField(default=0)


class PartnerSet(models.Model):
    CHOISE_OF_CODE = (
        ('DL', 'diler'),
        ('MT', 'market'),
        ('PS', 'person'),
        ('PD', 'provider')
    )

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2, choices=CHOISE_OF_CODE)


class TransactionStatus(models.Model):
    CHOISE_OF_TRANSACTION_CODE = (
        ('AC', 'accept'),
        ('RT', 'return'),
        ('RC', 'receipt')
    )

    status_code = models.CharField(max_length=2, choices=CHOISE_OF_TRANSACTION_CODE)


class TransactionSet(models.Model):
    status = models.ForeignKey('TransactionStatus', on_delete=models.CASCADE)
    # user
    partner = models.ForeignKey('PartnerSet', on_delete=models.CASCADE)
    storage = models.ForeignKey('StorageSet', on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now_add=True)


class StorageSet(models.Model):
    name = models.CharField(max_length=25)
    # product_set = models.ForeignKey('ProductSet', on_delete=models.CASCADE)
    # updating_date = models.DateTimeField(auto_now=True)


