from rdflib import URIRef, Graph, Namespace, Literal
from rdflib.namespace import RDF, OWL, XSD
import json
import pandas as pd
import glob
import re

# List patient files

json_files = glob.glob('../01_simulation/output/fhir/*json')

# We define global empty lists of allergies types and susbtances

# We create a list of allergy types to not create redundant nodes
allergy_types_all = []

# And we do the same for allergy substances
allergy_substances = []

# We repeat the code from above to recontruct our ontology from scratch

# Importing ontology
g = Graph()
g.parse("sphn_ontology.ttl")

# Adding allergies and patients as prefixes
allergies = Namespace("http://sib.swiss/allergies/")
g.bind("allergies", allergies)
patients = Namespace("http://sib.swiss/fictivePatients/")
g.bind("patients", patients)
substances = Namespace("http://sib.swiss/substances/")
g.bind("substances", substances)

# Adding also SPHN as a variable since this is not automatic
sphn = Namespace("https://biomedit.ch/rdf/sphn-ontology/sphn#")

# We create a splitting function to extract the terms we need
# from the allergy types we find

def split_allergen(allergen):
    first_split = Literal(allergen).split(' (')[0]
    no_spaces = first_split.replace(' ', '')
    # remove special characters
    clean = re.sub(r"[^a-zA-Z0-9 ]", "", no_spaces)
    return(clean)

def split_allergies_types(allergies):
    first_split = Literal(allergies).split('[')[1]
    second_split = first_split.split(']')[0]
    # remove special characters
    clean = re.sub(r"[^a-zA-Z0-9 ]", "", second_split)
    return(clean)

# looping through JSON files
for json_file in json_files:
    
    print(json_file)
    
    # Load data
    data = json.load(open(json_file, 'r'))
    
    # Adding patient ID to the ontology
    ID_patient = Literal(data['entry'][0]['resource']['id'])
    g.add((URIRef(patients + ID_patient), RDF.type, sphn.SubjectPseudoIdentifier))

    # we convert JSON import into dataframe
    df = pd.DataFrame.from_dict(pd.json_normalize(data['entry']), orient='columns')

    # We isolate the rows with allergies and get the allergy name(s)

    allergen_rows = df[df['resource.resourceType'] == 'AllergyIntolerance']
    
    if len(allergen_rows) == 0:
        print("No allergies found!")
        continue
    else:
        print("Allergies found!")
        allergen = allergen_rows['resource.code.text']

        # We isolate the allergy type as well

        allergies_types = allergen_rows['resource.category']
    
        # Now we create a loop to go through the terms
        # and add them to our ontology

        for i,j in zip(allergen,allergies_types):
        
            # Convert allergy type and substance to literal
            allergy_type = Literal(split_allergies_types(j))
            allergy_substance = Literal(split_allergen(i))
    
            # Check if any is part of a global list
            # and if not, we can add them to the ontology
    
            if allergy_type not in allergy_types_all:
                allergy_types_all.append(allergy_type)
                g.add((URIRef(allergies + allergy_type), RDF.type, sphn.Allergy))
        
            if allergy_substance not in allergy_substances:
                allergy_substances.append(allergy_substance)
                g.add((URIRef(allergies + allergy_type), sphn.hasSubstance, URIRef(substances + allergy_substance)))
    
            # Add to ontology by associating to the patient ID
            g.add((URIRef(allergies + allergy_type), sphn.hasSubjectPseudoIdentifier, URIRef(patients + ID_patient)))
            

# Output extended ontology

g.serialize(destination="output/sphn_ontology_extended.ttl")