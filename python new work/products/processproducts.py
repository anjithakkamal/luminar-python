from json import load
f=open("C:\\Users\\HP\\Desktop\\MY PYTHON\\products\\data.json","r",encoding="UTF-8")
data=load(f)

#1)no of products
print("no of products :- ",len(data))

#2) all product in names
prod_names=[p.get("title") for p in data]
print("all product names :- ",prod_names)

#3)all categories
all_categories=[p.get("category") for p in data ]
print(" all categories :- ",set(all_categories))

#4)print all product name available under rs 50
price_under50=[p.get("title") for p in data if p.get("price")<=50]
print("price under 50 :- ",price_under50)

#5)all jewelery product names filter category
jwellery_names=[p.get("title") for p in data if p.get("category")=="jewelery"]
print("all jewelery product names :- ",jwellery_names)

#6)costly product name and price 
def get_price(dictionary):
    return dictionary.get("price")
costly_product=max(data,key=get_price)
print("costly product name and price :- ",costly_product.get("title"),costly_product.get("price"))

 #7) cheapest priooduct
cheapest_product=min(data,key=get_price)
print("cheapest product name and price :- ",cheapest_product.get("title"),cheapest_product.get("price"))

#8) product title ,rating count
review_count=[(p.get("title"),p.get("rating").get("count")) for p in data]
print("product tiyle and rating count :- ",review_count)
# print(max(review_count))
#9)maximum rating
def get_rate(dictionary):
    return dictionary.get("rating").get("count")
max_review=max(data,key=get_rate)
print("max rating :- ",max_review.get("title"),max_review.get("rating").get("count"))