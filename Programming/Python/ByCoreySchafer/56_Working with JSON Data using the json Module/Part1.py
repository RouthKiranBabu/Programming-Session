'''JavaScript object Notation'''
import json5 as json

#Dont place space at the value of the phone number
people_string = '''
{
"people":[
        {
            "Name": "Routh Kiran",
            "Phone": 7077435454,
            "Email": ["firstlast123@gmail.com", "FIRSTLAST456@gmail.com"],
            "has_license": false
        },
        {
            "Name": "rOUTH kIRAN",
            "Phone": 1234567890,
            "Email": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

print(data)
#Output
#{'people': [{'Name': 'Routh Kiran', 'Phone': 7077435454, 
#             'Email': ['firstlast123@gmail.com', 'FIRSTLAST456@gmail.com'], 
#             'has_license': False}, 
#             {'Name': 'rOUTH kIRAN', 'Phone': 1234567890, 
#              'Email': None, 
#              'has_license': True}]}

#To check the type
print(type(data))
#Output
#<class 'dict'>

#https://docs.python.org/3/library/json.html#encoders-and-decoders
#false -> False

print(type(data['people']))
#Output
#<class 'list'>

for people in data['people']: print(people)
#Output
#{'Name': 'Routh Kiran', 'Phone': 7077435454, 'Email': ['firstlast123@gmail.com', 'FIRSTLAST456@gmail.com'], 'has_license': False}
#{'Name': 'rOUTH kIRAN', 'Phone': 1234567890, 'Email': None, 'has_license': True}

for people in data['people']: print(people['Name'])
#Output
#Routh Kiran
#rOUTH kIRAN

for people in data['people']: del people['Phone']
new_string = json.dumps(data)
print(new_string)
#Output
#{people: [{Name: "Routh Kiran", Email: ["firstlast123@gmail.com", 
#"FIRSTLAST456@gmail.com"], has_license: false}, {Name: "rOUTH kIRAN", 
#Email: null, has_license: true}]}

new_string = json.dumps(data, indent = 2)
print(new_string)
#Output
#{
#  people: [
#    {
#      Name: "Routh Kiran",
#      Email: [
#        "firstlast123@gmail.com",
#        "FIRSTLAST456@gmail.com",
#      ],
#      has_license: false,
#    },
#    {
#      Name: "rOUTH kIRAN",
#      Email: null,
#      has_license: true,
#    },
#  ],
#}

new_string = json.dumps(data, indent = 2, sort_keys = True)
print(new_string)
#Output
#{
#  people: [
#    {
#      Email: [
#        "firstlast123@gmail.com",
#        "FIRSTLAST456@gmail.com",
#      ],
#      Name: "Routh Kiran",
#      has_license: false,
#    },
#    {
#      Email: null,
#      Name: "rOUTH kIRAN",
#      has_license: true,
#    },
#  ],
#}