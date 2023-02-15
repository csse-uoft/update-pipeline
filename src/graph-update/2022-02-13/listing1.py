from tqdm import tqdm
from yachalk import chalk
from ..utils import read_csv
from .common import init
from src.ontologies.namespaces import cp
from owlready2 import default_world

listing1_onto, output_owl_filename = init('listing1')

# Load CSV
print(chalk.green("Loading CSV..."))
data = read_csv('./input/listings1.csv')
listingId2Row = {}
for row in data:
    if listingId2Row.get(row["Id"]):
        raise Exception("Duplicated ID")
    listingId2Row[row["Id"]] = row
print("Total", len(listingId2Row.keys()), "rows")

with listing1_onto:
    for listingId in tqdm(listingId2Row.keys()):

        result = list(default_world.sparql(f"""
            PREFIX : <http://helpseeker.co/compass#>
            PREFIX cids: <http://ontology.eil.utoronto.ca/cids/cids#>
            SELECT ?s WHERE {{
                {{
                    ?s a :Organization.
                }} UNION {{
                    ?s a cids:Program.
                }}
                ?s :hasID "{listingId}".
            }}
        """))
        if len(result) == 0:
            print(chalk.red(f"Cannot find ID={listingId}"))
            continue
        elif len(result) > 1:
            # print(chalk.yellow(f"Found multiple ID={listingId}"))
            pass

        for (organization_or_program,) in result:
            # Add search words
            cp.hasSearchWords[organization_or_program] = [listingId2Row[listingId]["SearchWords"]]
            # Add Localities
            cp.hasLocality[organization_or_program] = [listingId2Row[listingId]["Localities"]]

    listing1_onto.save(output_owl_filename)
