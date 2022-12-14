## Simulation


### Synthea run

To run the simulation, simply use the following command:

```
sh patient_simulation.sh
```

This will download `Synthea`, run a simulation generating synthetic clinical data for 100 live patient in `JSON` format (in an `output` folder), remove the tool and remove `JSON` files not related to the patients. For details on the simulation and its parameters, find information in the next sections. 

The structure of the `output` is as follows:

 - `metadata` is a folder including an individual `JSON` file with all the parameters related to the simulation
 - `fhir` is a folder with one `JSON` file for each patient that includes the clinical data we're looking for

### Simulation details

The patient simulator `Synthea` offers A LOT of different options, but for this specific task there was no need to dig too deep into them, since the goal is to obtain some data to play with. There were two main aspects taken into account:

 - The number of patients
 - The output file format
 
Each of these is further explained in the sections below. Note that to make this simulation reproducible, a seed was defined leading to the same output every time. Also, the only other parameter set in the simulation was the age range: between 20 and 90 years.
 
### Number of patients

When trying to simulate a 1'000 patients with the default output, the total file size was a bit excessive (>500Mb) so I chose 100 patients instead to have a number high enough to include as many different clinical infos as possible. Note that these 100 patients are the amount of alive patients in the simulation, while deceased ones are not counted. This leads to a total of over 100 patients simulated.

### Output file format

Not being familiar with the semantization process and with the large amount of file format standards, I wasn't sure which format to select. Three main standards seemed reasonable: HL7 FHIR (`JSON`), C-CDA (`XML`) and `CSV`. Since the first two represented standards for health-related data, I preferred to use either of them and with `JSON` files being more human-readable, I chose HL7 FHIR.