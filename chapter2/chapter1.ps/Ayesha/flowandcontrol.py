# name = ''
# while name != 'your name':
#     print('please type your name:')
   
#     name = input()
    
#     break
# print("thank you")

#2nd program
#while True:
    
    #print("please type your name:")
    #name = input()
    #if name == 'ayesha':
        #break
#print("thank you")

# 3rd program password checking
password = input("please enter your password:")
if (len(password)>=8):
    digit = False
    upper = False
    for x in password:
        if x.isdigit()==True:
            digit=True
        if x.isupper()==True:
            upper=True 
    if digit and upper:
        print("password is strong")
else:
    print("password is to weak")

#4th program prime number checking
# a = int(input("Enter first number:"))
# b = int(input("Enter last number:"))
# for num in range(a, b+1):
#   if num > 1:
#     for i in range(2, num):
#          if num%i==0:
#            break
#     else:
#         print(num)

# 5th program Atm withdrawal
# balance = int(input("enter a balance amount:"))
# amount = int(input("enter withdrawal amount:"))
# if amount % 100==0 and amount<=balance and (balance-amount)>=500: #balance - amount bcoz if we minus by amount we will get negative value
#     print("withdrawal is succesfull")
# else:
#     print("withdrawal is unsuccessfull")

# 6th program 
# n = int(input("Enter n:"))
# for i in range(1, n+1):
#     if '3' in str(i): #converting to str bcoz int cant include 'in' keyword
#       continue
#     print(i)

# 7th program count
# count = 0
# for i in range(1, 100+1):
    
#         if i%4==0 and i%6!=0:
#            count+=1
#            print("count:", count )

#8th program
# secrect = 7
# attempts = 0
# while True:
#    guess = int(input("guess the number:"))
#    attempts+=1
#    if guess > secrect:
#     print("Too high")
#    elif guess < secrect:
#     print("too low")
#    else:
#     print("correct")
#     print("attempts:",attempts)
    # break #can be used without while and break also

#9th program
# total = 0
# while True:
#     price = int(input("Entr price(0 to stop):")) 
#     if price == 0:
#         break
#     total += price
# if total > 10000:
#     discount = total * 0.20
# elif total > 5000:
#     discount = total * 0.10
# else:
#     discount = 0
# print("final amount:", total - discount)           

#10th program


# n = int(input("Enter number: "))
# multiple = n

# while multiple <= 100:
#     multiple += n

# print("First multiple greater than 100:", multiple)

# #11th program
# pin = 1234
# attempts = 3

# while attempts > 0:
#     entered = int(input("Enter PIN: "))

#     if entered == pin:
#         print("Access Granted")
#         break
#     else:
#         attempts -= 1
#         print("Wrong PIN")

# if attempts == 0:
#     print("Card Blocked")


#12th program
marks = []
fail = False

for i in range(5):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)
    if m < 35:
        fail = True

if fail:
    print("Fail")
else:
    avg = sum(marks) / 5

    if avg >= 90:
        print("Grade A")
    elif avg >= 75:
        print("Grade B")
    elif avg >= 60:
        print("Grade C")
    else:
        print("Fail")