# SPHN_framework_testing

## Overview

This repository includes all of the code and explanation related to the task of representing patient data using the [SPHN Semantic Interoperability Framework](https://sphn.ch/network/data-coordination-center/the-sphn-semantic-interoperability-framework/). The goal of the repository is to perform the three following steps:

 1) Generate synthetic patient data using [Synthea](https://github.com/synthetichealth/synthea)
 2) Semantize the simulated data following the SPHN framework
 3) Show some examples on how to use the semantized data to validate it, querying or visualization

All of these steps will be carried out in a reproducible way with a comprehensive documentation.

## Context

A big challenge in the Swiss health system is to combine the large variety of sources and formats in data. Depending on the hospital, the ward and the amount of standard formats, just to name a few, health-related data becomes very difficult to use and explore, particularly when it comes from different sources. To overcome these challenges, the Swiss Personalized Health Network developed a Semantic Interoperability Framework with the goal of making the task of combining health-related data easier. More in detail, this framework follows the FAIR (findable, accessible, interoperable and reusable) principles and makes data understandable to both humans and machines. Find implementation details [on this page](https://sphn.ch/network/data-coordination-center/the-sphn-semantic-interoperability-framework/).

## Structure of the repo

Three main folders will include code for each one of the steps outlined above. All versions of the tools used will be documented or made available in a `yaml` file to be used with `conda`. GitHub actions will be setup to make sure that whole pipeline can run on the specified OS. Below you will find a summary for each step and more details can be found in the `README` of the respective folder.

## Generating synthetic data

I simulated data for 135 patients aged between 20 and 90 years and the biggest question about this simulation was the output format of patient files. Many standards exist and I was not sure which one would be the most ideal pick to semantize. The final choice was `JSON` format, thinking that the format might be more human readable than others. 

## Semantize simulated data

To semantize data, the `rdflib` package has everything needed to carry out such a task. After playing around with the `R` version of the package, I noticed an important shortcoming that made me switch to the Python version. Long story short, the sematization process is not easy at all and because of that I simplified the goal of the semantization to make sure to do things the right way. Some important challenges to know when trying to transform data into a semantic format:

 - Be familiar with the data format and structure you're working with (in this case I worked with `json` files)
 - Familirize yourself with the reference framework (in this case the SPHN)
 - Make sure to generate semantic data with all of the relationships needed (define terms AND ALL of their connections)

Since each simulated patient file includes an enormous amount of information and the `JSON` file format is not as easy to navigate, I set as a goal to create a semantic network where patient IDs, their allergies and some details related to their status (gender) were included. 

## Examples on how to use the semantized data
