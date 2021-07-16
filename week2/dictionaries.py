# states = ["NY", "PA", "CA"]
# states = ["New York", "Pennsylvania", "California"]
# states = ["New York", "NY", "Pennsylvania", "PA", "California", "CA"]

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])

print(states.get('FL', 'Not Found'))
print(states.get('NY', 'Not Found'))

print(states.keys())
print(states.values())

states['FL'] = 'Florida'
print(states)

user = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'brown', 'eyes': 'brown'}

blog_post = {'title': '11 Sexy Uses for Dictionaries', 'body': 'blabalblababla'}

print(user['name'])
print(blog_post['title'])

# dictionaries and lists can be inside of each other

animal_sounds = {
    'cat': ['meow', 'purr'],
    'dog': ['woof', 'bark'],
    'fox': ['konkon']
}

mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'brown', 'eyes': 'brown'}
chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'brown', 'eyes': 'brown'}
sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'brown', 'eyes': 'brown'}

people = [mattan, chris, sarah]
print(people)

for person in people:
    print(person.get('height'))
