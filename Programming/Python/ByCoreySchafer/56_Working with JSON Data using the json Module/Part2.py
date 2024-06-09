'''JavaScript Object Notation'''
import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']: print(state)
#Output
#{'name': 'Alabama', 'abbreviation': 'AL', 'area_codes': ['205', '251', '256', '334', '938']}
#{'name': 'Alaska', 'abbreviation': 'AK', 'area_codes': ['907']}
#...

for state in data['states']: print(state['name'], state['abbreviation'])
#Output
#Alabama AL
#Alaska AK
#...

#To create a json file and save it
for state in data['states']:del state['area_codes']
with open('new_states.json', 'w') as f:json.dump(data, f)
#Output in the file
#{"states": [{"name": "Alabama", "abbreviation": "AL"}, 
#{"name": "Alaska", "abbreviation": "AK"}, 
#{"name": "Arizona", "abbreviation": "AZ"},
#{"name": "Arkansas", "abbreviation": "AR"}, {"name": "California", "abbreviation": "CA"}, {"name": "Colorado", "abbreviation": "CO"}, {"name": "Connecticut", "abbreviation": "CT"}, {"name": "Delaware", "abbreviation": "DE"}, {"name": "Florida", "abbreviation": "FL"}, {"name": "Georgia", "abbreviation": "GA"}, {"name": "Hawaii", "abbreviation": "HI"}, {"name": "Idaho", "abbreviation": "ID"}, {"name": "Illinois", "abbreviation": "IL"}, {"name": "Indiana", "abbreviation": "IN"}, {"name": "Iowa", "abbreviation": "IA"}, {"name": "Kansas", "abbreviation": "KS"}, {"name": "Kentucky", "abbreviation": "KY"}, {"name": "Louisiana", "abbreviation": "LA"}, {"name": "Maine", "abbreviation": "ME"}, {"name": "Maryland", "abbreviation": "MD"}, {"name": "Massachusetts", "abbreviation": "MA"}, {"name": "Michigan", "abbreviation": "MI"}, {"name": "Minnesota", "abbreviation": "MN"}, {"name": "Mississippi", "abbreviation": "MS"}, {"name": "Missouri", "abbreviation": "MO"}, {"name": "Montana", "abbreviation": "MT"}, {"name": "Nebraska", "abbreviation": "NE"}, {"name": "Nevada", "abbreviation": "NV"}, {"name": "New Hampshire", "abbreviation": "NH"}, {"name": "New Jersey", "abbreviation": "NJ"}, {"name": "New Mexico", "abbreviation": "NM"}, {"name": "New York", "abbreviation": "NY"}, {"name": "North Carolina", "abbreviation": "NC"}, {"name": "North Dakota", "abbreviation": "ND"}, {"name": "Ohio", "abbreviation": "OH"}, {"name": "Oklahoma", "abbreviation": "OK"}, {"name": "Oregon", "abbreviation": "OR"}, {"name": "Pennsylvania", "abbreviation": "PA"}, {"name": "Rhode Island", "abbreviation": "RI"}, {"name": "South Carolina", "abbreviation": "SC"}, {"name": "South Dakota", "abbreviation": "SD"}, {"name": "Tennessee", "abbreviation": "TN"}, {"name": "Texas", "abbreviation": "TX"}, {"name": "Utah", "abbreviation": "UT"}, {"name": "Vermont", "abbreviation": "VT"}, {"name": "Virginia", "abbreviation": "VA"}, {"name": "Washington", "abbreviation": "WA"}, {"name": "West Virginia", "abbreviation": "WV"}, {"name": "Wisconsin", "abbreviation": "WI"}, {"name": "Wyoming", "abbreviation": "WY"}]}

#To create a json file and save it
for state in data['states']:del state['area_codes']
with open('new_statesindent.json', 'w') as f:json.dump(data, f, indent = 2)
#Output
#{
#  "states": [
#    {
#      "name": "Alabama",
#      "abbreviation": "AL"
#    },
#    {
#      "name": "Alaska",
#      "abbreviation": "AK"
#    },
#...