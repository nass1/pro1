from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
import shopify
#from .models import ProductsModels
import time
#from .forms import NameForm, ProductForm
from .forms import APIform, SearchForm




#-------------------------------------------------------------------
api = "d8abe2f7be6107b6f6f4cc5f220f14ca"
password = "73f30d24102f182b6cb7b1b4e9b8b6f1"
shared_secret = "0b4c643fa7edd739a1dda92bade84e22"
url_format = "https://apikey:password@hostname/admin/resource.json"
shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
shopify.ShopifyResource.set_site(shop_url)
#------------------------------------------------------------------------

key = "DA8gz8DqfsXnYcm8iH54zM9x_zRynBRw_IJAnL8Xszw."
# Create your views here.



def contact(request):
    shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
    shopify.ShopifyResource.set_site(shop_url)
    url = "https://secure.chinavasion.com/api/getProductDetails.php"
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            codeFinal = cd['Search']
            getProductDetails_dic = {
                "key": key,
                "model_code": codeFinal,
            }
            try:
                r = requests.post(url, json=getProductDetails_dic)
                json_r = r.text
                json_load = json.loads(json_r)

                for i in json_load["products"]:
                      product_id_lst = i["product_id"]
                      product_name_lst = i["short_product_name"]
                      product_url_lst = i["product_url"]
                      product_price = i["price"]
                      category_name_lst = i["category_name"]
                      overview_lst = i["overview"]
                      main_picture_lst = i["main_picture"]
                      additional_images_lst = i["additional_images"]
                      print (additional_images_lst)

                context = {"product_id_lst": str(product_id_lst),
                   "product_url_lst": product_url_lst,
                   "product_name_lst": product_name_lst,
                   "category_name_lst": category_name_lst,
                   "overview_lst": overview_lst,
                   "main_picture_lst": main_picture_lst,
                   "additional_images_lst": additional_images_lst,
                   "product_price": product_price,
                   }
                return render(request, 'index.html', context)
            except:
                return render(request, 'index.html', {'error':'error'})
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form':form})





def mainINDEX(request):
    try:
        code = str(request)
        code2, code1 = code.split("Search=")
        codeFinal = code1[:-2]
        #global codeFinal
        context = {
            "code": codeFinal
        }

        print (code)
    except:
        return render(request, "base.html", {})
    return render(request, "base.html", context)


def getProducts(request):
    shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
    shopify.ShopifyResource.set_site(shop_url)
    url = "https://secure.chinavasion.com/api/getProductDetails.php"

    try:
        if 'Search' in request.GET and request.GET['Search']:
            q = request.GET['Search']
            codeFinal = q

            getProductDetails_dic = {
                "key": key,
                "model_code": codeFinal,
            }
        r = requests.post(url, json=getProductDetails_dic)
        json_r = r.text
        json_load = json.loads(json_r)

        for i in json_load["products"]:
              product_id_lst = i["product_id"]
              product_name_lst = i["short_product_name"]
              product_url_lst = i["product_url"]
              product_price = i["price"]
              category_name_lst = i["category_name"]
              overview_lst = i["overview"]
              main_picture_lst = i["main_picture"]
              additional_images_lst = i["additional_images"]
              print (additional_images_lst)
        """
        db1 = ProductsModels(product_id_mod=product_id_lst,
                             product_url_mod=product_url_lst,product_price_mod=product_price,
                             product_name_mod=product_name_lst,overview_lst_mod=overview_lst,
                             main_picture_mod=main_picture_lst, additional_images_mod=additional_images_lst)
        db1.save()
        """
        context = {"product_id_lst": str(product_id_lst),
                   "product_url_lst": product_url_lst,
                   "product_name_lst": product_name_lst,
                   "category_name_lst": category_name_lst,
                   "overview_lst": overview_lst,
                   "main_picture_lst": main_picture_lst,
                   "additional_images_lst": additional_images_lst,
                   "product_price": product_price,
                   }

    except:
        return render(request, "base.html", {"error":"Wrong Url try again"})

    return render(request, "base.html", context)



def getList(request):
    db1 = ProductsModels.objects.all()
    dbAddImages = []
    for i in db1:
        dbAddImages.append(i.additional_images_mod)
    context = {
        "db1": db1,
        "dbAddImages":dbAddImages

    }

    return render(request, "getlist.html", context)


"""
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
"""

def editProduct(request):
    instance = ProductsModels.objects.get(pk=21)

    if request.method == "POST":
        form = ProductForm(request.POST or None, instance=instance)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect("base.html")
    else:
        form = ProductForm()
    return render(request, 'name.html', {'form': form})

def PostToShpify(request):
    shop_url = "https://%s:%s@mr-nice.myshopify.com/admin" % (api, password)
    shopify.ShopifyResource.set_site(shop_url)
    url = "https://secure.chinavasion.com/api/getProductDetails.php"
    new_product = shopify.Product()
    try:
        if 'ProductName' in request.GET and request.GET['ProductName']:
            q = request.GET['ProductName']
            dis = request.GET['dis']
            price = request.GET['price']
            mainPic = request.GET['mainPic']
            productType = request.GET['productType']
            additionalPic = request.GET['additionalPic']

            new_product.title = q
            new_product.body_html = dis
            new_product.product_type = productType
            new_product.save()

            makelist = additionalPic

            #Price
            product = shopify.Product.find(new_product.id)
            product.variants[0].price = price
            product.save()

            #Main Image
            new_image = shopify.Image()
            new_image = shopify.Image(dict(product_id=new_product.id))
            new_image.src = mainPic
            new_image.save()
            #additinola images
            makelist1 = makelist.replace("[","").replace("u'","").replace("]","").replace(",","").replace("'","")
            for i in makelist1.split():
                new_image = shopify.Image()
                new_image = shopify.Image(dict(product_id=new_product.id))
                new_image.src = i
                new_image.save()

            print type(additionalPic)
            #print ("======>>>>>>>>>>", makelist1)





    except:
        return render(request, "base.html", {"error":"Error"})

    return render(request, "base.html", {})
