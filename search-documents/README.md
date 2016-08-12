## Document Search Engine

### Requirements:
- python3
- pip3
Any python / pip referred subsequently refers to major version 3. It might also work on py 2.7, but I haven't tested it.

### Installation:
Install the package dependencies using the following command:
(You may even choose to do so with a `virtualenv`)
`pip install -r requirements.txt`

### Indexing
The documents need to be indexed before you can begin searching.
To index the documents, place them inside the `data/` folder, and run:
`python IndexingService.py`
This will create the `index.p` which is an index persisted on disk. For existing data, this has already been created.

### Searching
To search and store all results in the `output/` folder run:
`python QuerySystem.py`
This will query all queries in the `query.txt` file and store results in the `output` folder in decreasing order of relevance for each query in a separate file.

For a custom query, just pass the query as a command line argument:
`python QuerySystem.py "current President of the United States"`
This will return results on stdout, with relevance scores like:
```
data/barack_hussein_obama : 139.57060293948518
data/hillary_diane_rodham_clinton : 130.36785585042304
data/united_state_presidential_election_2016 : 67.84214704751733
data/president_of_the_united_states : 47.036447551855744
data/united_states_of_america : 23.74349979953498
data/obama : 7.829186362783724
data/narendra_damodardas_modi : 7.478654158484209
```
