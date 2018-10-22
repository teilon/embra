from .models import Storage, ProductSet, Client, Transaction, TransactionStatus


class Init_store():

    def start(self):
        has_client = Client.objects.count()
        if has_client == 0:
            self.create_provider()

        has_store = Storage.objects.count()
        if has_store != 0:
            return
        product_set = self.create_product_set()
        self.create_storage(product_set)

    def create_provider(self):
        provider = Client(name='ИП \"Баймуратов\"', form='PD')
        provider.save()

    def create_transactions_status(self):
        status = TransactionStatus(status='AC')
        status.save()
        status = TransactionStatus(status='RT')
        status.save()
        status = TransactionStatus(status='RC')
        status.save()

    def create_product_set(self):
        product_set = ProductSet(m1=0, m2=0, m3=0, m4=0, m5=0, m6=0, m7=0, m8=0, m9=0, m10=0,
                                 w1=0, w2=0, w3=0, w4=0, w5=0, w6=0, w7=0, w8=0, w9=0, w10=0)
        product_set.save()
        return product_set

    def create_storage(self, product_set):
        storage = Storage(product_set=product_set)
        storage.save()


def init_storage():
    init_store = Init_store()
    # init_store.start()
    init_store.create_transactions_status()

class Store:

    def create_transaction(self, status, ps_dict, client_id):
        ps = self.product_set_from_dict(ps_dict)
        client = self.get_client_by_id(client_id)
        if status == 'AC':
            pass
        if status == 'RT':
            pass
        if status == 'RC':
            transaction_status = TransactionStatus.objects.get(status='RC')
            transaction = Transaction(status=transaction_status, client=client, product_set=ps)
            transaction.save()
            self.receipt(ps)

    def get_client_by_id(self, client_id):
        return Client.objects.get(id=client_id)

    def get_storage_ps(self):
        ps = Storage.objects.first().product_set_id
        return ProductSet.objects.get(id=ps)

    def receipt(self, ps):
        storage_ps = self.get_storage_ps()
        storage_ps.m1 = storage_ps.m1 + ps.m1
        storage_ps.m2 = storage_ps.m2 + ps.m2
        storage_ps.m3 = storage_ps.m3 + ps.m3
        storage_ps.m4 = storage_ps.m4 + ps.m4
        storage_ps.m5 = storage_ps.m5 + ps.m5
        storage_ps.m6 = storage_ps.m6 + ps.m6
        storage_ps.m7 = storage_ps.m7 + ps.m7
        storage_ps.m8 = storage_ps.m8 + ps.m8
        storage_ps.m9 = storage_ps.m9 + ps.m9
        storage_ps.m10 = storage_ps.m10 + ps.m10

        storage_ps.w1 = storage_ps.w1 + ps.w1
        storage_ps.w2 = storage_ps.w2 + ps.w2
        storage_ps.w3 = storage_ps.w3 + ps.w3
        storage_ps.w4 = storage_ps.w4 + ps.w4
        storage_ps.w5 = storage_ps.w5 + ps.w5
        storage_ps.w6 = storage_ps.w6 + ps.w6
        storage_ps.w7 = storage_ps.w7 + ps.w7
        storage_ps.w8 = storage_ps.w8 + ps.w8
        storage_ps.w9 = storage_ps.w9 + ps.w9
        storage_ps.w10 = storage_ps.w10 + ps.w10

        storage_ps.save()

    def product_set_from_dict(self, d):
        ps = ProductSet(m1=d['m1'], m2=d['m2'], m3=d['m3'], m4=d['m4'],
                        m5=d['m5'], m6=d['m6'], m7=d['m7'], m8=d['m8'],
                        m9=d['m9'], m10=d['m10'], w1=d['w1'], w2=d['w2'],
                        w3=d['w3'], w4=d['w4'], w5=d['w5'], w6=d['w6'],
                        w7=d['w7'], w8=d['w8'], w9=d['w9'], w10=d['w10'])
        ps.save()
        return ps

def test_receipt():

    pstest={'m1': 100,
            'm2': 100,
            'm3': 100,
            'm4': 100,
            'm5': 100,
            'm6': 100,
            'm7': 100,
            'm8': 100,
            'm9': 100,
            'm10': 100,
            'w1': 100,
            'w2': 100,
            'w3': 100,
            'w4': 100,
            'w5': 100,
            'w6': 100,
            'w7': 100,
            'w8': 100,
            'w9': 100,
            'w10': 100}
    clientid = 1
    status = 'RC'

    storage = Store()
    storage.create_transaction(status, pstest, clientid)

