from .models import Storage, ProductSet, Client


class Init_store():

    def start(self):
        has_client = Client.objects.count()
        if has_client == 0:
            print('provider is not exists')
            self.create_provider()

        has_store = Storage.objects.count()
        if has_store != 0:
            print('storage already exists')
            return
        print('storage is not exists')
        product_set = self.create_product_set()
        self.create_storage(product_set)


    def create_provider(self):
        provider = Client(name='ИП \"Баймуратов\"', form='PD')
        provider.save()


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
    init_store.start()
