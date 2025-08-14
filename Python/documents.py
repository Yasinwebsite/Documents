# F String

# name = 'Amirali'
# familyName = 'Borji'
# age = 16.439312

# print(f'Hello you are {name} {familyName} and you are {age:1.1f}')




# Data Types


# List (Arrays [])

# names = ['jadi', 'zahra', 'sina', 'amir', 'ali']
# things = [False, 2, 3.14, 'amir']

# names.index('amir')
# names.reverse()
# names.pop()
# names.append(10)
# names.sort(w)
# names.remove('zahra')

# print(names)

# my_list = [1, 2, 4]
# my_list.insert(2, 3)   درج عدد 3 در ایندکس 2
# print(my_list)   خروجی: [1, 2, 3, 4]



# Dic (Object)

# score = {'riazi': 16, 'programming': 20}

# score['farsi'] = 20
# print(len(score))w


# scores = {'jadi': {
#              'riazi': 16,
#              'programming': 21
#         },
#          'amir': {
#              'riazi': 15,
#              'programming': 20
#          },
# }

# print(scores['amir']['programming'])
# print(scores['jadi']['riazi'])

# scores.keys()
# scores.values()
# scores.items()
# scores.pop('jadi')

# print(scores.get('jadi', -1))
# اگر ورودی اول رو یپدا نکرد ورودی دوم را برمیگرداند


# Dic exercise
# fruit_prices = {
#    'apple': 1500,
#    'banan': 1000,
#    'orange': 1200
# }

# fruit_prices['banan'] = 1100
# fruit_prices.pop('apple')
# print(fruit_prices)



# Tuple

# همون لیست ولی با فرق اینکه نمیشه مقدار اونهارو عوض کرد یعنی اونها 
# (Immutable)
# هستند

# t1 = (1, 2, 3, 4, 'ali', 3.14)

# resault = ('jadi', 12)
# name, nomre = resault
# هر کدوم از عناصر داخل یک متغیر قرار میگیرد و این کار در لیست هم امکان دارد

# tuple exercise
# coordinates = (3 ,4)
# distance = (coordinates[0] ** 2 + coordinates[1] ** 2) ** 0.5
# print(f"[Distance] => {distance}")

# Fileio
# دیتایی که محتویات بقیه فایل هارو میخونه

# file_io = open('file.txt') #اوپن یه کلمه کلیدی هست
# file_io.close() #فایل رو میبندیم و دیگه باهاش کاری نداریم
# file_io.seek(0) #به اول فایل برمیگردیم

# روش بهتر برای استفاده از fileio

# with open('file.txt') as file_io_2 :
#     lines = file_io_2.readlines()
#     print(lines)

# بعد اتمام بلوک خودش فایل رو میبنده

# FileIo modes:

# with open('file.txt', "(modes)") as file_io_2 :

# r: فقط خوندن
# w: فقط برای نوشتن
# rb or wb: برای خوندن یا نوشتن باینری
# a: همون اضافه کردن


# عملگرهای مقایسه ای

# ==, <, >, <=, >=, !=

# تمرین
# a=int(input("Enter number1: "))
# b=int(input("Enter number2: "))
# c=int(input("Enter number3: "))
# print(a<b<c)



# Statements

# sen = 16

# if sen < 18:
#    print('salam bache')
# elif sen < 40:
#    print('salam miansal')
# else :
#    print('salam mosen')

# تمرین سبد خرید

price = int(input('mablagh kharid ra vared konid'))
final_price = None

if price > 50000:
   final_price = price * (1 - 20 / 100)
elif 50000 > price > 20000:
   final_price = price * (1 - 10 / 100)
else:
   final_price = price


print(final_price)




# Loops

# for

list = [1, 2, 3, 4, 6, 10]
even_numbers = []
odd_numbers = []

for list_item in list:
   print(list_item) #هر سری که حلقه اجرا میشه یه ایتم از لیست رو پرینت میکنه
   
   if list_item % 2 == 0:
      even_numbers.append(list_item)
   else:
      odd_numbers.append(list_item)



print(f'Even numbers: \n{even_numbers}')
print(f'Odd numbers: \n{odd_numbers}')


Unpacking in js

people = {'amirali': (16,180), 'amir': (16,183)}

for sen, ghad in people.values():
   print(sen,ghad)


# While
# تا زمانی که یه شرطی برقرار باشه دستورات اجرا میشن
a = 0

print('im starting')

while a <= 5:
   print(f'a is {a}')
   a += 1
print('finished')

# مسئله مشهور «مسئله کولاچ» (Collatz conjecture)

number = int(input('Adad  ra vared konid: '))

while number != 1:
   print(number)
   if number % 2 == 0:
      number = number // 2
   else:
      number =  (number * 3) + 1

print(1)

# دستور هایی برای خارج شدن از حلقه

for item in [1, 2, 3]:
   if item == 2:
      # pass
      # break
      # بهش برسه لوپ میشکنه
      continue
      # باعث میشه دستورات بعد از این کلمه اجرا نشن و لوپ دوباره از اول با ایتم بعدی اجرا بشه
   print(item)


# تمرین برسی بخش پذیری اعداد به سبک باری هوپ

n = 0

while n < 200:
   n += 1
   if (n % 3 == 0) and (n % 5 == 0):
      print('hiphop')
      continue
   if n % 3 == 0:
      print('hope')
      continue
   if n % 5 == 0:
      print('hip')
      continue
   print(n)


   # List Comprehation

# میشه بجای این کار
list = [1, 2, 3, 4]

# list_2 = []
# for list_item in list:
#    list_2.append(list_item * 2)
# print(list_2)

# # این کار رو بکنیم که حرفه ای تر و خلاصه تره
# list_2 = [list_item * 2 for list_item in list]
# print(list_2)



# همین ترفند تو شرط ها
# a = 6

# resault = ('fard' if a % 2 != 0 else 'zoje')
# print(resault)


# اگر بخوایم لیستی بسازیم که از لیست قبلی عدد های زوجش رو به ما بده

# list_2 = [n for n in list if n % 2 == 0]
# print(list_2)

#  یا اینکه به ازای هر عنصر لیست بگه زوجه یا فرد

# list_2 = ['zoje' if n % 2 == 0 else 'fard' for n in list]
# print(list_2)







# enumerate

list = ['amir', 'jadi', 'ali', 'sarah']

for list, a in enumerate(list):
   # متد بالا میاد اجزای یک لیست رو به صورت ایندکسی برمیگردونه و یجورایی شماره گذاری میکنه
   print(list, a)



# zip
name = ['amir', 'soroosh']
family = ['borji', 'mehr']

for i in zip(name, family):
   # دقیقا همون کاری رو میکنه که زیپ لباس انجام میده
   print(i)


# in

names = ['amir', 'ali', 'jadi']

people = {
   'amir': {'sen': 16, 'ghad': 180},
   'jadi': {'sen': 45, 'ghad': 180}
}

for name in names:
   if name in people:
      print(f'{name} is {people[name]['sen']} and his height is {people[name]['ghad']}')
   else:
      print(f'i have no data for {name}')