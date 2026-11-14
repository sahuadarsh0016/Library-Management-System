import json 
import os

#Load data
def load(f):
    return(
        json.load(open(f))
        if os.path.exists(f) and os.path.getsize(f) > 0
        else[]
    )

#Save data
def save(f,d):
    json.dump(d,open(f,"w"),indent=4)  

     
     
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        