import rdflib
from rdflib import Graph

g = rdflib.Graph()

g.parse("gnd-sc_20220208.ttl", format="ttl")

qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?concept
       WHERE {
        ?concept a skos:Concept .
        FILTER NOT EXISTS { ?concept skos:broader ?broaderConcept }
       }""")

with open("gnd-scTopConcepts.txt", "a") as output:
    for row in qres:
            output.write("<%s>, " % row)