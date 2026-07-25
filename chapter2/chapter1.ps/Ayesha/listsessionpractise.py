# metro_line=["Majestic","Indiranagar","MGRoad"]
# if "Cubbon Park" not in metro_line:
#     metro_line.insert(1,"Cubbon Park")
#     print(metro_line)
#     metro_line.extend(["halasuru","trinity"])
#     print(metro_line)
# for index,value in enumerate(metro_line):
#      print("Station",index,":",value)


#1st program metro_line
# metro = ["MG Road", "Majestic", "Yelahanka", "Indiranagar", "Whitefield"]

# metro.append("Silk Board")      # add at end
# metro.insert(0, "Kengeri")      # add at start

# print(metro)

    
# 2. The Roll Call
# names = ["Ayesha", "Rahul", "Neha", "Arjun"]

# for name in names:
#     print(name.upper())

# 3. Vowel Counter
# chars = ('a', 'b', 'e', 'i', 'o', 'u', 'x')
# vowels = ('a', 'e', 'i', 'o', 'u')

# count = 0
# for ch in chars:
#     if ch in vowels:
#         count += 1

# print("Vowel count:", count)

# # 4. The Membership Check
# foods = ["Dosa", "Idli", "Vada", "Biryani"]

# dish = input("Enter a dish name: ")

# if dish in foods:
#     print("Yes, it's on the list!")
# else:
#     print("Not on the list.")

 # 5. The Empty Cafe
# customers = ["A", "B", "C", "D"]

# while customers:
#     print("Serving:", customers.pop())

# print("Cafe is empty")

# # 6. The Singleton
# single_tuple = (10,)
# single_list = [10]

# print(type(single_tuple))
# print(type(single_list))

 # 7. The Traffic Filter

# vehicles = ["Auto", "Car", "Bus", "Auto", "Bike"]

# filtered = []
# for v in vehicles:
#     if v != "Auto":
#         filtered.append(v)

# print(filtered)

# 8. Token System 2.0
# people = ["Ravi", "Sita", "Aman"]

# for i, name in enumerate(people, start=1):
#     print(f"Token #{i}, your order is ready, {name}!")

# # 9. The Price Hike
# prices = (100, 200, 300)

# price_list = list(prices)

# for i in range(len(price_list)):
#     price_list[i] += 50

# prices = tuple(price_list)
# print(prices)

 # 10. The Unique Visitor
# names = ["A", "B", "A", "C", "B"]

# unique = []
# for n in names:
#     if n not in unique:
#         unique.append(n)

# print(unique)

# # 11. The “Every-Other” Slice
# nums = list(range(10))

# even_index_items = nums[0::2]
# print(even_index_items)

# # 12. The Shuffle Draw
# import random

# friends = ["A", "B", "C", "D", "E"]

# random.shuffle(friends)
# winner = random.choice(friends)

# print("Lucky Winner:", winner)

# # 13. The Unpacker
# places = [("Silk Board", 45), ("Indiranagar", 20)]

# for place, time in places:
#     print(f"It takes {time} mins to reach {place}")


# 14. The Salary Split
# salaries = [30000, 60000, 45000, 80000]

# high = []
# entry = []

# for s in salaries:
#     if s > 50000:
#         high.append(s)
#     else:
#         entry.append(s)

# print(tuple(high))
# print(tuple(entry))


# 15. The Matrix Search

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in range(3):
#     for j in range(3):
#         if matrix[i][j] == 7:
#             print("Position:", (i, j))

# 16. The Reverse Order

# words = ["apple", "banana", "cherry"]

# result = []
# for w in words[::-1]:
#     result.append(w[::-1])

# print(result)


#  17. The Shopping Cart

# cart = [("Pen", 10), ("Book", 50), ("Bag", 300)]

# max_item = cart[0]

# for item in cart:
#     if item[1] > max_item[1]:
#         max_item = item

# print("Most expensive:", max_item)


 # 18. The Frequency Map
areas = ["Whitefield", "BTM", "Whitefield", "BTM", "Whitefield"]

for area in set(areas):
    print(area, ":", areas.count(area))

# # 20. The FizzBuzz List

nums = list(range(1, 31))

for i in range(len(nums)):
    if nums[i] % 3 == 0 and nums[i] % 5 == 0:
        nums[i] = "FizzBuzz"
    elif nums[i] % 3 == 0:
        nums[i] = "Fizz"
    elif nums[i] % 5 == 0:
        nums[i] = "Buzz"

print(nums)