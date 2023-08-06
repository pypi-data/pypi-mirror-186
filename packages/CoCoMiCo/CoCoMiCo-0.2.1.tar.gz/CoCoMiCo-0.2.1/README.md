# CoCoMiCo : COoperation and COmpetition in MIcrobial COmmunities

CoCoMiCo aims at characterising the metabolism of microbial communities through genome-scale metabolic networks: it calculates cooperation and competition potentials for the communities.
It has two modes:
* a regular mode: cooperation and competition potentials are computed for a community whose associated genome-scale metabolic networks are located in a directory: (`run` mode)
* a `benchmark` mode: run can be performed systematically for a collection of microbial communities described in a `json` file

CoCoMiCo can be tested on toy data using the following command: `cocomico toys`.

## Install

Required **Python >= 3.7**. The main dependency of CoCoMiCo is an Answer Set Programming (ASP) solver. [Clyngor](https://github.com/Aluriak/clyngor) permits the connection between Python and ASP, whereas [Clyngor_with_clingo](https://github.com/Aluriak/clyngor-with-clingo/) provides the solver binaries in the Python environment. If you work in a conda environment, installing the solvers directly ([clingo](https://anaconda.org/potassco/clingo)) makes it unnecessary to install Clyngor_with_clingo.

```
pip install cocomico
```

or

```
python setyp.py install
```

or after cloning this repository

```
pip install .
```

**If you use CoCoMiCo, please cite:**

Lecomte M, Muller C, Badoual A, Falentin H, Sherman DJ, and Frioux C. 2023. CoCoMiCo: metabolic modelling of cooperation and competition potentials in large-scale bacterial communities.

## Usage

### Single community run

`run` needs the specific architecture as follow:

```
Community_folder
├── species_1.sbml
├── species_4.sbml
├── species_10.sbml
```

Metabolic network file in the community_folder can be in either `.xml` or `.sbml` format. `run` mode creates the `json` community in the appropriate format described in the section **benchmark**.

```
usage: cocomico run [-h] [-folder_path FOLDER_PATH] [-seed_path SEED_PATH] [-output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i, -folder_path FOLDER_PATH, --folder_path FOLDER_PATH
                        Directory path of a community composed of sbml or xml files.
  -s, -seed_path SEED_PATH, --seed_path SEED_PATH
                        path of seed file
  -o, -output OUTPUT, --output OUTPUT
                        output path
```

#### Exemple of execution

`
cocomico run -folder_path PATH_COMMUNITIES_FOLDER -seed_path  PATH_SEED_FILE -output PATH_OUTPUT
`
### Multiple runs: benchmarking mode

`benchmark` needs the genome-scale metabolic networks used for community construction to be stored in a directory and a json file describing the composition of each sample as follow.
For example:

```
Folder_input
├── communities.json
├── sbml
│   └── species_1.sbml
│   └── species_4.xml
|    ..
```

`communities.json`` must be in the following format:

```
{
    "com_0" :[
            species_1.sbml,
            species_4.xml,
            species_10.sbml
    ],
    "com_1" :[
            species_12.xml,
            species_120.sbml
    ]
}

```

Here, sample `com0` is composed of three species: `species_`, `species_4` and `species_10`.


```
usage: cocomico benchmark [-h] [-json_com JSON_COM] [-seed_path SEED_PATH] [-sbml_path SBML_PATH] [-output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -j, -json_com JSON_COM, --json_com JSON_COM
                        path of the json file
  -s, -seed_path SEED_PATH, --seed_path SEED_PATH
                        path of seed file
  -i, -sbml_path SBML_PATH, --sbml_path SBML_PATH
                        folder path to find sbml model
  -o -output OUTPUT, --output OUTPUT
                        output path

```

#### Exemple of execution

`
cocomico benchmark -json_com PATH_COMMUNITIES_JSON_FILE -seed_path  PATH_SEED_FILE -sbml_path PATH_SBML_DIRECTORY -output PATH_OUTPUT
`


### toys

```
usage: cocomico toys [-h] [-output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -o, -output OUTPUT, --output OUTPUT
                        output path
```

## Output

In a folder `community_scores`, the output is a json file as follow:

```
{
    ""metabolite production value (delta)": 31,
    "metabolite production value_metric": {
        "added value community": 17,
        "all individual can produce": 14
    },
    "cooP": 18.0,
    "cooP_metric": {
        "number of exchanged metabolites": 8,
        "pi producers": 8.5,
        "pi consumers": 9.5
    },
    "reaction production(rho)": 58,
    "reaction production_metric": {
        "added value comunity": 37
    },
    "comP": 3.25,
    "comP_metric": {
        "total number of limited subtrates": 13
    },
    "bacteria": [
        "Com2Org1",
        "Com2Org4",
        "Com2Org2",
        "Com2Org3"
    ]
}
```

In addition, a `scores.tsv` file is generated, in the output directory, containing all information about the communities:

- `ComP` and `Coop` are respectively the competition and the cooperation potentials.
- `rh` is a score describing the gain of activated reactions in the interacting community with respect to activated reaction in a non-interacting community
- `delt` is a score describing the gain of producible metabolites in the interacting community with respect to activated reaction in a non-interacting community
- `com_siz` describes the size of the corresponding community ie the number of genome-scale metabolic networks
- `nb_exc_cpd` denotes the putative number of metabolic exchanges in the community
- `CooP_producers` and `CooP_consumers` calculate respectively the number of producers and consumers of exchanged metabolites, applying an exponential decrease to the score each time a metabolite is produced (respectively consumed) by more than one member.

|   | delta | cooP | rho | comP | com_size | nb_exc_cpd | cooP_producers | cooP_consumers |
|---|-------|------|-----|------|----------|------------|----------------|----------------|
| 0 | 22    | 10.0 | 40  | 2.66 | 3        | 4          | 4.5            | 5.5            |
| 1 | 31    | 18.0 | 58  | 3.25 | 4        | 8          | 8.5            | 9.5            |


# Version
CoCoMiCo version 0.2.1
