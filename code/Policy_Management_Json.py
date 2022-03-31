import pandas as pd
import json
import sys

if __name__=="__main__":
    d={}
    df=pd.read_excel(sys.argv[1])
    for k,g in df.groupby("Cat nbr"):
        d[k]=g['Resource ']
    for key, value in d.items():    
        name="pn:promo:LIVE:"+ str(key).zfill(3)
        description="Policy for "+str(key).zfill(3) +" in LIVE dataset. These are just sample resources and actions. This is not a complete list"
        subject="gn:promo:LIVE:"+str(key).zfill(3)
        effect="allow"
        resources=[]
        for resource in  d[key]:
            resources.append("rn:promo:LIVE:subcategory:"+str(resource)+":*")
        
        data={
            "name":name,
            "description":description,
            "subjects":[subject],
            "effect":effect,
            "resources":resources,
            "actions": [
                "an:promo:LIVE:dummy:state:0:all:NA"
            ],
            "conditions": {},
            "meta": 'NULL'


        }
        
        with open(sys.argv[2]+'pn-promo-live-'+str(key)+'.json', 'w') as outfile:
            json.dump(data, outfile,separators=(',\n', ': '))
