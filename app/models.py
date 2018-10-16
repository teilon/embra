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

    def create_transaction(self, status, psdict):
        product_set = self.new_product_set(psdict)
        if status == 'AC':
            pass
        if status == 'RT':
            pass
        if status == 'RC':
            pass

    def new_product_set(self, psdict):
        ps = ProductSet(m1=int(psdict['m1']), m2=int(psdict['m2']), m3=int(psdict['m3']), m4=int(psdict['m4']),
                        m5=int(psdict['m5']), m6=int(psdict['m6']), m7=int(psdict['m7']), m8=int(psdict['m8']),
                        m9=int(psdict['m9']), m10=int(psdict['m10']), w1=int(psdict['w1']), w2=int(psdict['w2']),
                        w3=int(psdict['w3']), w4=int(psdict['w4']), w5=int(psdict['w5']), w6=int(psdict['w6']),
                        w7=int(psdict['w7']), w8=int(psdict['w8']), w9=int(psdict['w9']), w10=int(psdict['w10']))
        ps.save()
        return ps


class Storage(models.Model):
    product_set = models.ForeignKey('ProductSet', on_delete=models.CASCADE)
    updating_date = models.DateTimeField(auto_now=True)


