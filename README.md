This repo contains the datasets used for experimentations with **[NeoMaPy](https://github.com/cedric-cnam/NeoMaPy_Daphne)** on the [ANR DAPHNE](http://daphne.huma-num.fr/) Project.

You can find several datasets:
- *Wikidata - nrockit*. The preliminaries data got from the **n-rockit** project thanks to *Chekol*. You will find the rules that must be validated for the MAP inference, and the rows of the MLN
- *wikidataExtractor* - The extraction of the MLN (nrockit) and translated into a CSV file for the **NeoMaPy Graph**. It has been processeed by the "[wikidataExtractor](https://github.com/cedric-cnam/NeoMaPy_Daphne/tree/main/Neo4j/wikidata/wikidata_extractor)" Java program.
- *NeoMapy Graph export* - The results after computation of various graphs with the *[GraphModeling](https://github.com/cedric-cnam/NeoMaPy_Daphne/tree/main/Neo4j/wikidata/graphModeling)* program of **NeoMaPy** and exports of: processing times, statistics, conflictual and no-conflictual nodes.
