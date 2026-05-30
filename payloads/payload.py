from faker import Faker
import random
from datamodels.Product import Product

from unicodedata import category


class Payload:
    faker = Faker()
    categories = ["electronics","Furniture","clothings","books","beauty"]



    def product_payload(self) ->Product:
        title=self.faker.unique.catch_phrase()
        price=float(self.faker.pricetag().replace("$","").replace(",",""))
        description = self.faker.sentence()
        image_url = "https://i.pravatar.cc/100"
        category = random.choice(self.categories)
        return Product(title,price,description,image_url,category)

