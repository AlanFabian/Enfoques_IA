#Alan de Jesus Fabian Garcia
from rdflib import Graph, URIRef, RDF, RDFS, OWL

# Crear un grafo RDF
g = Graph()

# Definir los prefijos de los namespaces utilizados
ex = URIRef("http://www.example.com/ontology#")
g.bind("ex", ex)

# Definir clases y subclases
human = ex["Human"]
man = ex["Man"]
g.add((man, RDF.type, OWL.Class))
g.add((man, RDFS.subClassOf, human))

# Definir una propiedad
has_gender = ex["hasGender"]
gender = ex["Gender"]
g.add((has_gender, RDF.type, OWL.ObjectProperty))
g.add((has_gender, RDFS.domain, human))
g.add((has_gender, RDFS.range, gender))

# Definir una instancia
john = ex["John"]
male = ex["Male"]
g.add((john, RDF.type, man))
g.add((john, has_gender, male))

# Definir una restricción
g.add((gender, RDF.type, OWL.Class))
g.add((gender, OWL.oneOf, male))
g.add((gender, OWL.oneOf, ex["Female"]))

# Imprimir el grafo RDF
print(g.serialize(format="turtle").decode())
