# SPHN_framework_testing

## Overview

This repository includes all of the code and explanation related to the task of representing patient data using the [SPHN Semantic Interoperability Framework](https://sphn.ch/network/data-coordination-center/the-sphn-semantic-interoperability-framework/). The goal of the repository is to perform the three following steps:

 1) Generate synthetic patient data using [Synthea](https://github.com/synthetichealth/synthea)
 2) Semantize the simulated data following the SPHN framework
 3) Show some examples on how to use the semantized data to validate it or for querying

All of these steps will be carried out in a reproducible way with a comprehensive documentation.

## Context

A big challenge in the Swiss health system is to combine the large variety of sources and formats in data. Depending on the hospital, the ward and the amount of standard formats, just to name a few, health-related data becomes very difficult to use and explore, particularly when it comes from different sources. To overcome these challenges, the Swiss Personalized Health Network developed a Semantic Interoperability Framework with the goal of making the task of combining health-related data easier. More in detail, this framework follows the FAIR (findable, accessible, interoperable and reusable) principles and makes data understandable to both humans and machines. Find implementation details [on this page](https://sphn.ch/network/data-coordination-center/the-sphn-semantic-interoperability-framework/).

## Structure of the repo

Three main folders will include code for each one of the steps outlined above. All versions of the tools used will be documented or made available in a `yaml` file to be used with `conda`. If you're not familiar with conda, check it out [here](https://docs.conda.io/en/latest/). Below you will find a summary for each step and more details can be found in the `README` of the respective folder.

## Generating synthetic data

I simulated data for 100 patients aged between 20 and 90 years and the biggest question about this simulation was the output format of patient files. Many standards exist and I was not sure which one would be the most ideal pick to semantize. The final choice was `JSON` format from the HL7 FHIR standard, thinking that this format might be closer to real health-related data and also more human readable than others. 

## Semantize simulated data

Since each simulated patient file includes an enormous amount of information and the `JSON` file format is not as easy to navigate, I set as a goal to create a semantic network where patient IDs, their allergies and some details related to their status (gender) were included. I divided the semantization task into smaller subtasks to address the following problems individually: 

 - Parsing the 2022 SPHN ontology and adding some elements to it
 - Parsing patient data in `JSON` format to find patient ID and allergy information
 - Create a loop to both parse patient data and add all patient IDs and allergy info in the ontology

## Validation of the extended ontology

Through the Shapes Constraint Language (SHACL) it is possible to validate whether a dataset follows a set of rules defined by a specific ontology. For the SPHN ontology, the SPHN RDF Quality Check Tool was developed for this purpose. Since the scope of this project was small and the SPHN ontology was only extended, one quality check was used to confirm that the semantization was successful.

## Query data

As a final step to show how to use semantized data, I used SPARQL to explore the new extended ontology. Specifically, we looked for patients (i.e. their IDs) having an allergy and we also checked which allergens are associated to which allergy types. This query offered an insight on how data could be extracted and visualized from a given ontology.
