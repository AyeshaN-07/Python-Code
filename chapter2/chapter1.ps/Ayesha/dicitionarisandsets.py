# pet = {'type':'cat', 'color':'oranage','collar':False,'age':2}
# print(pet)
# print(type(pet))

# pet2 = {'color':'oranage','collar':False,'type':'cat','age':2}
# print(pet == pet2)

# print(pet.keys())
# print(pet.values())
# print(pet.get('color',1))
# print(pet.items())
# print(pet.get('funny','not there'))

#2nd program
# grocery = {'milk':100, 'meat':200, 'soap':20, 'maida':2000}
# print(grocery)
# print('price of milk',grocery.get('milk'))
# # print('price of milk:', grocery['milk']) we can use this type also of list
# grocery['avacado']=160
# print(grocery)

# del grocery['meat']
# print(grocery)

# if 'milk' in grocery:
#     print('yes')
# else:
#     print('no')

# # for item_name in grocery.keys():
# #     print(item_name)

# # for price in grocery.values():
# #     print(price)

# for price,item in grocery.items():
#     print(price,item)

#     print(grocery.get('mango', 'out of stock'))

#3rd program
# name = {'milk':1000,'meat':300,'maida':300,'chocolate':200}
# print(name)

# cost = 0
# for price in name.values():
#   cost = cost + price #or cost+=price
# print('total price',cost)

# discount=0
# for item,price in name.items():
#   name[item] = price*0.9 #0.9 bcoz there is 10% so 100-10 is 90 so we are takig 0.9
  
#   print(name)

#4th program
pg={'roomno1':['Sagar', 8000, True],
      'roomno2':['Vinay', 7000, False], 
      'roomno3':['Sahil', 8000, False]
      } 
print(type(pg))
print(pg)
# pg['roomno1']=8000+500
# pg['roomno2']=7000+500
# pg['roomno3']=8000+500
# print(pg)
# for price in pg.values():
#   print(price)

pg['roomno2'][2]=True #index 2 bcoz false index is 2
print(pg)
