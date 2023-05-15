from os import system,environ

def city():
    all_cities = {1:'qom'}
    for k,v in all_cities.items():
        print(k,v)
    s = int(input("Enter your city name CITY: "))
    for s in all_cities.keys():
        selected_city = all_cities[s]
    #environ["CITY"] = 
    return selected_city

def category():
    all_categories = {1: "mobile-phones"}
    for k, v in all_categories.items():
        print(k, v)
    c = int(input("Enter the number you want CAT: "))
    for c in all_categories.keys():
        selected_cat = all_categories[c]
    #environ["CATEGORY"] = 
    return selected_cat

def brand():
    all_brands = {1: 'apple', 2: 'samsung', 3: 'xiaomi'}
    for k, v in all_brands.items():
        print(k, v)
    b = int(input("Enter the number BRAND: "))
    selected_brand = all_brands[b]
    #environ["BRAND"] = selected_brand
    return selected_brand

def model(selected_brand):
    apple = {1: 'apple-iphone-11', 2: 'apple-iphone-11-pro', 3: 'apple-iphone-11-pro-max',4:'apple-iphone-12',5:'apple-iphone-12-pro',6:'apple-iphone-12-pro-max',7:'apple-iphone-13',8:'apple-iphone-13-pro',9:'apple-iphone-14-pro-max',10:'apple-iphone-xs',11:'apple-iphone-x',12:'apple-iphone-7',13:'apple-iphone-7-plus'}
    samsung = {1: 'samsung-galaxy-a53-5g', 2: 'samsung-galaxy-a72-5g', 3: 'samsung-galaxy-s21', 4: 'samsung-galaxy-s20', 5:'samsung-galaxy-a30s', 6:'samsung-galaxy-a30'}
    xiaomi = {}
    if selected_brand == "apple":
        for k, v in apple.items():
            print(k, v)
        m = int(input("enter model apple: "))
        selected_model = apple[m]
        environ["MODEL"] = selected_model
    if selected_brand == "samsung":
        for k, v in samsung.items():
            print(k, v)
        m = int(input("enter model samsung: "))
        selected_model = samsung[m]
        environ["MODEL"] = selected_model
    if selected_brand == "xiaomi":
        for k, v in xiaomi.items():
            print(k, v)
        m = int(input("enter model xiaomi: "))
        selected_model = xiaomi[m]
        environ["MODEL"] = selected_model
    return selected_model

selected_city = city()
#print(selected_city)
selected_cat = category()
#print(selected_cat)
selected_brand = brand()
#print(selected_brand)
selected_model = model(selected_brand)
#print(selected_model)



with open('config.sh','w+') as f:
    l = [f'export CITY={selected_city}\nexport CATEGORY={selected_cat}\nexport BRAND={selected_brand}\nexport MODEL="{selected_model}"']
    f.writelines(l)


'''model = environ.get("MODEL")
cat = environ.get("CATEGORY")
brand = environ.get("BRAND")
city = environ.get("CITY")

print(model,cat,brand,city)'''