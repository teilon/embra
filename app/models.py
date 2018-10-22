from django.db import models


class ProductSet(models.Model):
    m1 = models.IntegerField(default=0)
    m2 = models.IntegerField(default=0)
    m3 = models.IntegerField(default=0)
    m4 = models.IntegerField(default=0)
    m5 = models.IntegerField(default=0)
    m6 = models.IntegerField(default=0)
    m7 = models.IntegerField(default=0)
    m8 = models.IntegerField(default=0)
    m9 = models.IntegerField(default=0)
    m10 = models.IntegerField(default=0)
    w1 = models.IntegerField(default=0)
    w2 = models.IntegerField(default=0)
    w3 = models.IntegerField(default=0)
    w4 = models.IntegerField(default=0)
    w5 = models.IntegerField(default=0)
    w6 = models.IntegerField(default=0)
    w7 = models.IntegerField(default=0)
    w8 = models.IntegerField(default=0)
    w9 = models.IntegerField(default=0)
    w10 = models.IntegerField(default=0)


class Client(models.Model):
    CHOISE_OF_FORM = (
        ('DL', 'diler'),
        ('MT', 'market'),
        ('PS', 'person'),
        ('PD', 'provider')
    )

    name = models.CharField(max_length=50)
    form = models.CharField(max_length=2, choices=CHOISE_OF_FORM)


class TransactionStatus(models.Model):
    CHOISE_OF_TRANSACTION_STATUS = (
        ('AC', 'accept'),
        ('RT', 'return'),
        ('RC', 'receipt')
    )

    status = models.CharField(max_length=2, choices=CHOISE_OF_TRANSACTION_STATUS)


class Transaction(models.Model):
    status = models.ForeignKey('TransactionStatus', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    product_set = models.ForeignKey('ProductSet', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)


class Storage(models.Model):
    product_set = models.ForeignKey('ProductSet', on_delete=models.CASCADE)
    updating_date = models.DateTimeField(auto_now=True)


