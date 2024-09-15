import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_lg")

# Process a text
doc = nlp("Bob, Powell, 3067501234, bob.powell@email.com")

# Print token details
for ent in doc.ents: # ents property contains all the extracted entities
    print(ent.text, ent.label_)
