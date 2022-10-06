wget https://github.com/synthetichealth/synthea/releases/download/master-branch-latest/synthea-with-dependencies.jar .

java -jar synthea-with-dependencies.jar -s 1663926070850 -r 20220923 -cs 1663926070850 -p 100 -a 20-90

rm synthea-with-dependencies.jar
rm output/fhir/hospitalInformation1665083909141.json
rm output/fhir/practitionerInformation1665083909141.json
