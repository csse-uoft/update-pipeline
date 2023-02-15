import datetime
import os

from yachalk import chalk


def init(listing_name: str):
    inout_owl_filename = f"./input/v1/knowledge_graph_{listing_name}.owl"
    output_owl_filename = f"./output/v2/knowledge_graph_{listing_name}"
    output_owl_filename = f"{output_owl_filename}_{str(datetime.datetime.now()).replace(' ', '_').replace(':', '_')}.owl"

    # Set log location
    os.makedirs('./output/v2', exist_ok=True)

    # Import existed owl files
    print(chalk.green("Loading Ontologies..."))
    from src.ontologies.namespaces import cp
    from owlready2 import default_world

    print(chalk.green("Loading KG..."))
    listing_onto = default_world.get_ontology(inout_owl_filename).load()

    with listing_onto:
        # Add extra fields
        with cp:
            import src.ontologies.extras

    return listing_onto, output_owl_filename
