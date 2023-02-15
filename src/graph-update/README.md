## Update Log
### 2023-02-13

- Added `cp:hasSearchWords` annotation property
  - i.e. `xxx cp:hasSearchWords "Youth, Employment, Education/Training"`
- Added `cp:hasLocality` annotation property
  - i.e. `xxx cp:hasLocality "canada, alberta, calgary"`
- Removed letter in `cp:hasID` from listing2
  - i.e. `N1` -> `1`

---
### Usage
> Outputs are in `./output/v2`
```shell
python -m src.graph-update.2022-02-13.listing1
```
```text
* Owlready2 * Warning: optimized Cython parser module 'owlready2_optimized' is not available, defaulting to slower Python implementation
* Owlready2 * WARNING: DataProperty http://www.w3.org/2006/time#inXSDDateTime belongs to more than one entity types: [owl.DeprecatedProperty, owl.DatatypeProperty]; I'm trying to fix it...
* Owlready2 * WARNING: DataProperty http://www.w3.org/2006/time#xsdDateTime belongs to more than one entity types: [owl.DeprecatedProperty, owl.DatatypeProperty]; I'm trying to fix it...
* Owlready2 * WARNING: ObjectProperty https://schema.org/name belongs to more than one entity types: [owl.ObjectProperty, rdf-schema.label]; I'm trying to fix it...
* Owlready2 * WARNING: DataProperty http://ontology.eil.utoronto.ca/Survey/survey#targetProperty belongs to more than one entity types: [owl.ObjectProperty, owl.DatatypeProperty, survey.SurveyObjectProperty, survey.SurveyDataProperty]; I'm trying to fix it...
Loading Ontologies...
Loading KG...
Loading CSV...
Loaded CSV "./input/listings1.csv"; Encoding: utf-8-sig
Total 40813 rows
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 40813/40813 [00:23<00:00, 1723.70it/s]
```
```shell
python -m src.graph-update.2022-02-13.listing2
```
