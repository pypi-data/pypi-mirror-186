# Hefesto

Preprocessing datatable toolkit

Makes easier to allign with EJP CDE semantic model requirements


## To install:
```bash
pip install Hefesto
```


## To use:
**Requirements:**

- YAML configuration file to define which CDE do you want to execute and which columns contains the information
- CSV datatable with your CDE data

**Exemplar config file:**

This configuration file helps to fit with the requirements of [CDE implementation docs](https://github.com/ejp-rd-vp/CDE-semantic-model-implementations/tree/master/YARRRML_Transform_Templates) 

```yaml

Diagnosis: # Model tagname to identify the proper CDE
  columns: # columns based on the requirements:
    pid: pat_id  # pid is the tagname for patient identifier based on CDE implementations docs
                 # pat_id is the name of the column in your datatable 
    valueAttributeIRI: diagnosis # same for any column required

# you can add all model tagname you want as a new YAMl object
```
exemplar YAML file [here](https://github.com/pabloalarconm/hefesto/blob/main/data/config.yaml) 

**Test:**

```py
from Hefesto.main import Hefesto
import yaml

# Import YAML configuration file with all parameters:
with open("data/config.yaml") as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)

test = Hefesto.transform_shape(path_datainput ="data/exemplarCDEdata.csv", configuration=configuration)
test.to_csv ("data/result.csv", index = False, header=True)
```

