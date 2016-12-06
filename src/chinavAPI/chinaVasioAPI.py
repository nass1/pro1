import requests
import json
import pprint

key = "DA8gz8DqfsXnYcm8iH54zM9x_zRynBRw_IJAnL8Xszw."
class chinaApi():
  def getCategory(self):
    getCategory_dic = {
      "key": key,
      "include_content": "0"
    }
    url = "https://secure.chinavasion.com/api/getCategory.php"
    r = requests.post(url, json=getCategory_dic)
    json_r = r.text
    return json.loads(json_r)

  def Category_loops(self):
    Category_lst = []
    getCategoryName = self.getCategory()
    for i in getCategoryName["categories"]:
      Category_lst.append(i["name"])
      print(i["name"])
    return Category_lst

class getProductDetails():
  def getPrductsDetails_id(self):
    url = "https://secure.chinavasion.com/api/getProductDetails.php"
    modeCode = "CVVO-M281-N1" #until we figure out somthing
    getProductDetails_dic = {
      "key": key,
      "model_code": modeCode,
    }
    r = requests.post(url, json=getProductDetails_dic)
    json_r = r.text
    json_load = json.loads(json_r)
    product_id_lst = []
    product_name_lst = []
    product_url_lst = []
    category_name_lst = []
    overview_lst = []
    additional_images_lst = []
    for i in json_load["products"]:
      product_id_lst.append(i["product_id"])
      product_name_lst.append(i["short_product_name"])
      product_url_lst.append(i["product_url"])
      category_name_lst.append(i["category_name"])
      overview_lst.append(i["overview"])
      additional_images_lst.append(i["additional_images"])
    return product_name_lst, product_url_lst, category_name_lst, overview_lst, additional_images_lst