
import json
from IPython.display import HTML, display

with open ('osrm_query_response.json', 'r') as f:
    osrm_response = json.load(f)


all_nodes = list()
matchings = osrm_response.get('matchings',[])
for matching in matchings:
    for leg in matching.get('legs'):
        annotation = leg.get('annotation')
        all_nodes.append(annotation.get('nodes'))

print(all_nodes)






matched_locations = list()
if 'code' in osrm_response and osrm_response['code'] == 'Ok':
    tracepoints = osrm_response.get('tracepoints')
    for tracepoint in tracepoints:
        if tracepoint :
            if 'location' in tracepoint:
                matched_locations.append(tracepoint['location'])
            if 'name' in tracepoint and tracepoint['name'] != '':
                print(tracepoint['name'])

print(matched_locations)