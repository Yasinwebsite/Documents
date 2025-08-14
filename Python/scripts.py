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