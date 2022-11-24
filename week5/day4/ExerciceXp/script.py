import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sampleJson = json.loads(sampleJson)
print(sampleJson['company']["employee"]['payable']['salary'])
sampleJson['company']['employee'].update({'birth_date':''})
print(sampleJson)

import json
jsonFile = 'fic.json'
with open(jsonFile,'w') as jF:
    json.dump(sampleJson,jF)