from owlready2 import default_world

default_world.get_ontology('https://csse-uoft.github.io/ontologies/time.rdf').load()
default_world.get_ontology('https://csse-uoft.github.io/ontologies/geosparql.owl').load()

# Force mapping http://ontology.eil.utoronto.ca/5087/2/Bylaw.owl -> https://csse-uoft.github.io/ontologies/Bylaw.owl
bylaw_onto = default_world.get_ontology('https://csse-uoft.github.io/ontologies/Bylaw.owl').load()
default_world.ontologies['http://ontology.eil.utoronto.ca/5087/2/Bylaw.owl#'] = bylaw_onto

# Force mapping http://ontology.eil.utoronto.ca/tove/icontact.owl -> https://csse-uoft.github.io/ontologies/icontact.owl
icontact_onto = default_world.get_ontology('https://csse-uoft.github.io/ontologies/icontact.owl').load()
default_world.ontologies['http://ontology.eil.utoronto.ca/tove/icontact.owl#'] = icontact_onto

compass = default_world.get_ontology('https://github.com/csse-uoft/compass-ontology/releases/download/latest/compass.owl').load()
ic = default_world.get_namespace('http://ontology.eil.utoronto.ca/tove/icontact#')
geo = default_world.get_namespace('http://www.w3.org/2003/01/geo/wgs84_pos/')
cids = default_world.get_namespace('http://ontology.eil.utoronto.ca/cids/cids#')
org = compass.get_namespace("http://ontology.eil.utoronto.ca/tove/organization#")
tove_org = org
time = default_world.get_namespace("http://www.w3.org/2006/time#")
schema = default_world.get_namespace("http://schema.org/")
dcterms = default_world.get_namespace("http://purl.org/dc/terms/")


hs_data_onto = default_world.get_ontology('http://helpseeker.co/import1#')
hs_data_onto.imported_ontologies = [compass]


hs_data_cp_ns = hs_data_onto.get_namespace('http://helpseeker.co/compass#')
cp = hs_data_cp_ns
