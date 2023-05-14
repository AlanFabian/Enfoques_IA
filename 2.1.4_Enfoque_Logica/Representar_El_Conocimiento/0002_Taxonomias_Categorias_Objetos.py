#Alan de Jesus Fabian Garcia 
taxonomy = {
    'Animal': ['Mamífero', 'Reptil', 'Ave'],
    'Mamífero': ['Perro', 'Gato', 'Elefante'],
    'Reptil': ['Serpiente', 'Tortuga'],
    'Ave': ['Águila', 'Pato']
}
print(taxonomy['Animal'])  # ['Mamífero', 'Reptil', 'Ave']
print(taxonomy['Mamífero'])  # ['Perro', 'Gato', 'Elefante']

def find_objects(category):
    objects = []
    for parent, children in taxonomy.items():
        if category in children:
            objects.extend(children)
    return objects

print(find_objects('Animal'))  # ['Mamífero', 'Reptil', 'Ave', 'Perro', 'Gato', 'Elefante', 'Serpiente', 'Tortuga', 'Águila', 'Pato']
