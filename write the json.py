# import json

# with open('states.json') as f:
#   state_data= json.load(f)

# for state in state_data['states']:
#   del state['area_codes']

# with open('states.json', 'w') as f:
#   json.dump(state_data, f, indent=2)

import json
d=a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}

with open('lucky.json','w') as f:
    json_string=json.dump(d,f,indent=4)
f.close()