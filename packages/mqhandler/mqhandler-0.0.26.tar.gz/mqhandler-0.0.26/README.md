# MaxQuant Handler

## Setup for proper usage


### Install package
```shell
pip install mqhandler
```

## Run mqhandler
### 1. Filter IDs
Filter proteins or genes by organism and/or decoy names.
#### 1.1 Imports
```python
# imports
import pandas as pd
from mqhandler import filter_ids as fi
from mqhandler.mq_utils.runner_utils import find_delimiter
```
#### 1.2 Load your data
```python
# load data into a dataframe with automated delimiter finder
data = pd.read_table(file, sep=find_delimiter(<file>)).fillna("")
```
#### 1.3 Set preferences
```python
organism = "human" # Specify organism the ids should match to
in_type = "protein" #  Define what type should be the source
protein_column = "Protein IDs" # Name of column with protein IDs
gene_column = "Gene names" # Name of column with gene names
action = "delete" # What to do, if IDs cell is empty after filtering. Keep empty cell, delete it or fill it based on gene name.
reviewed = True # Bool to indicate if newly retrieved protein IDs should be reduced to reviewed ones
decoy = False # Bool to indicate if protein ids from decoy fasta (REV__, CON__) should be kept
```
#### 1.4 Filter IDs
```python
# load data into a dataframe with automated delimiter finder
filtered_data = fi.filter_protein_ids(data = data, id_column = protein_column, organism = organism,
                                      decoy = decoy, action = action, gene_column = gene_column,
                                      reviewed = reviewed)
```
### 2. Remap gene names
Re-map gene names in MaxQuant file.
#### 2.1 Imports
```python
# imports
import pandas as pd
from mqhandler import remap_genenames as rg
from mqhandler.mq_utils.runner_utils import find_delimiter
```
#### 2.2 Load your data
```python
# load data into a dataframe with automated delimiter finder
data = pd.read_table(file, sep=find_delimiter(<file>)).fillna("")
```
#### 2.3 Set preferences
```python
organism = "human" # Specify organism the ids should match to
mode = <mode> #  Mode of refilling. See below for more infos
protein_column = "Protein IDs" # Name of column with protein IDs
gene_column = "Gene names" # Name of column with gene names
skip_filled = True # Bool to indicate if already filled gene names should be skipped
fasta = <file> # Fasta file when mode all or fasta
```
Modes
```shell
all		Use primarly fasta infos and additionally uniprot infos.
fasta		Use information extracted from fasta headers.
uniprot	        Use mapping information from uniprot and use all gene names.
uniprot_primary Use mapping information from uniprot and only all primary gene names.
uniprot_one	Use mapping information from uniprot and only use most frequent single gene name.

```
#### 2.4 Remap gene names
```python
# load data into a dataframe with automated delimiter finder
remapped_data = rg.remap_genenames(data = data, mode = mode, protein_column = protein_column, gene_column = gene_column,
                                   skip_filled = skip_filled, organism = organism, fasta = fasta)
```
### 3. Get orthologs
Get ortholog gene names from origin organism to target organism.
#### 3.1 Imports
```python
# imports
import pandas as pd
from mqhandler import map_orthologs as mo
from mqhandler.mq_utils.runner_utils import find_delimiter
```
#### 3.2 Load your data
```python
# load data into a dataframe with automated delimiter finder
data = pd.read_table(file, sep=find_delimiter(<file>)).fillna("")
```
#### 3.3 Set preferences
```python
source_organism = "rat" # Specify organism the ids should match to
target_organism = "human" # Specify organism the ids should match to
protein_column = "Protein IDs" # Name of column with protein IDs
gene_column = "Gene names" # Name of column with gene names
```
#### 3.4 Get orthologs
```python
# load data into a dataframe with automated delimiter finder
ortholog_data = mo.get_orthologs(data = data, protein_column = protein_column, gene_column = gene_column,
                                 organism = source_organism, tar_organism = target_organism)
```