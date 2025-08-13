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