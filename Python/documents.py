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
a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
c=int(input("Enter number3: "))

print(a<b<c)

