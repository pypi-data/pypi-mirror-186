An SDMX mapping utility to generate partial key maps for referential metadata.
Although not designed to do that, data mappings are also possible.

Three methods are available:
- *map_withFile* GET method (receiving the mapping source and mapping rules both as file references)
- *map_withURN* GET method (receiving the mapping source  as file and the mapping rules as SDMX registry endpoint + mapping ID)
- *map_json_withURN* POST method (receiving the mapping source as the body of the request in json - pandas dataframe dictionary style - and mapping rules as SDMX registry endpoint + mapping ID) (added in version 0.1.1)
