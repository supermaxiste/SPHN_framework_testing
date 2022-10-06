## Validation

To validate our extended ontology, we used the official SPHN RDF Quality Check Tool. To run this tool, make sure the following requirements are met:

 - Apache Jena4 with TDB2 requires: Java JDK 11 installed (minimum version)
 - Java Virtual Machine JVM with memory allocation minimum as 4 GB.
 - Disk storage equal to the size of the original data x 2.5

To run the check, use the following command:

```
sh quality_check.sh
```
### Output file intepretation

The `report.log.txt` file shows the results off the validation and includes several quality checks. Since we just added elements to the ontology without modifying its structure, the quality check counting the SPHN concepts confirms that:

```
#Counts the number of SPHN concepts
Executing queries/queries2022/QC00010-count-sphn-distinct-concepts.rq against resources files
--------------------------------------------------------------------------------------------------
| concept                      | sphn_concepts_resources | subject_cnt | case_cnt | provider_cnt |
==================================================================================================
| sphn:SubjectPseudoIdentifier | 134                     | 0           | 0        | 0            |
| sphn:Allergy                 | 29                      | 17          | 0        | 0            |
--------------------------------------------------------------------------------------------------
```

### Reference, license and copyright

All of the files in this folder, with the exception of `report.log.txt` and `debug.log` were taken from the official SPHN RDF Quality Check Tool [gitlab repository](https://git.dcc.sib.swiss/sphn-semantic-framework/sphn-rdf-quality-check-tool). For licensing, copyright and other details, please refer to their repository.