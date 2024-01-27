products=[
    {"code":100,"name":"redminote13","brand":"redmi","price":30000,"network":"5g"},
    {"code":101,"name":"iphone15","brand":"apple","price":130000,"network":"5g"},
    {"code":102,"name":"samsunga18","brand":"samsung","price":20000,"network":"4g"},
    {"code":103,"name":"redminote12","brand":"redmi","price":30000,"network":"4g"},
    {"code":104,"name":"s23ultra","brand":"samsung","price":150000,"network":"5g"},
    {"code":105,"name":"motoedge","brand":"motorola","price":24000,"network":"5g"},
    {"code":106,"name":"oneplus9r","brand":"oneplus","price":30000,"network":"5g"},    
]
#1) total number of product ---------------------
print("total number of product :- ",len(products))

#2) apple product price-------------------
# for mobile in products:
#     if mobile.get("brand")=="apple":
#         print("apple mobile price :- ",mobile.get("price"))
apple_price=[p.get("price") for p in products if p.get("brand")=="apple"]
print("apple mobile price :- ",apple_price)

#3) mobiles avialable under 20k - 25k-------------------
price_filter=[p.get("name") for p in products if p.get("price") in range(20000,25001)]
print("mobiles avialable under 20k - 25k :- ",price_filter)

#4) costly brand-------------------------
def get_price(dictionary):
    return dictionary.get("price")
costly_product=max(products,key=get_price)
print("costly brand :- ",costly_product.get("brand"))

#5)cheapest brand--------------------------
cheapest_product=min(products,key=get_price)
print("cheapest brand :- ",cheapest_product.get("brand"))

#6) print all 5g network phones-----------------
fiveg_phones=[p.get("name") for p in products if p.get("network")=="5g"]
print("5g phones :- ",fiveg_phones)

#7) brand:3,redmi3--------------------------------
all_brands=[p.get("brand") for p in products]
wc={b:all_brands.count(b)for b in set(all_brands)}
print("count of brands :- ",wc)