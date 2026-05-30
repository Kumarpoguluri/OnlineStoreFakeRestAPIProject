import requests
import pytest
import  json
from routes.Routes import Routes
from datamodels.Product import Product
from utils.DataProviders import read_json_data
import os
from payloads.payload import Payload


path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "product.json"))

class TestProductAPI:
    @pytest.fixture(autouse=True)
    def init_class_vars(self,setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.category = "jewelery"
        # self.payload = Payload().product_payload()

    @pytest.mark.regression
    @pytest.mark.parametrize("order_data",read_json_data(path))
    def test_add_new_product_deleteproduct(self,order_data):
        product_data = order_data[0]


        ##extract feilds
        title= product_data["title"]
        price=product_data["price"]
        description= product_data["description"]
        image=product_data["image"]
        category=product_data["category"]
        payload = Product(title, price, description, image, category)


        #addning new product
        response = requests.post(self.base_url+Routes.CREATE_PRODUCT,json=payload.__dict__)
        assert response.status_code == 201
        data = response.json()
        print(json.dumps(data, indent=4))
        assert data["title"] == payload.__dict__["title"]
        product_id = data["id"]


        #deleting product
        endpoint = self.base_url+Routes.DELETE_PRODUCT.format(id=product_id )
        response = requests.delete(endpoint)
        # assert response.status_code == 204
        # data = response.json()
        # print(json.dumps(data, indent=4))
