str = "У меня ассиметрия лица"
 
for w in str.split(): 
    if(w.startswith("а") or w.endswith("я")): 
        print(w) 