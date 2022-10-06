### Query

To query data from the newly generated ontology I used the `sparqlwrapper` Python package. To find out how to use it, I referred to the [SPARQL guide from the SPHN documentation](https://sphn-semantic-framework.readthedocs.io/en/latest/user_guide/sparql.html). To query the extended ontology, a conda environment from `query.yaml` must be created and JupyterLab should be used to go through the `query.ipynb` file.

The commands to run:

```
conda env create -f query.yaml -n query
conda activate query
jupyter-lab
```

Then open `query.ipynb` from the panel on the left side to run the code to query.