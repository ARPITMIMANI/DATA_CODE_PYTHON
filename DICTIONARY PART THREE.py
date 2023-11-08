 # LOOP THROUGH DICTIONARY KEYS USING for LOOP .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

for x in marks:
    print(x)

# LOOP THROUGH DICTIONARY VALUES USING for LOOP .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

for x in marks:
    print ( marks[x] ) 

# keys() FUNCTON IS USED TO RETURN KEYS OF THE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

for x in marks.keys():
    print(x)


# values() FUNCTON IS USED TO RETURN VALUES OF THE DICTIONARY .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

for x in marks.values():
    print(x)

# items() FUNCTON IS USED TO RETURN BOTH KEYS AND VALUES OF THE DICTIONARY .  

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

for x,y in marks.items():
    print(x,y)

# COPY THE DICTIONARY USING FUNCTION copy() .

marks = {
    "JIM":82 ,
    "TOM":74 ,
    "DAN":88 ,
    "FIN":92 ,
    "LEO":78 ,
    "REX":84 
    }

scores = marks.copy()
print(scores)

# COPY THE DICTIONARY USING BUILD IN METHOD dict() .

result = dict(marks)
print(result)

# NESTED DICTIONARY : IT IS A DICTIONARY THAT CONTAIN ANOTHER DICTIONARY IN IT .

# METHOD ONE

europe = {
    "country_1" : {
        "NAME" : "GERMANY" ,
        "CAPITAL" : "BERLIN" ,
        "LANGUAGE" : "GERMAN" ,
        "GDP_RANK" : 3
    } ,
    "country_2" : {
        "NAME" : "ITALY" ,
        "CAPITAL" : "ROME" ,
        "LANGUAGE" : "ITALIAN" ,
        "GDP_RANK" : 8
    } ,
    "country_3" : {
        "NAME" : "SPAIN" ,
        "CAPITAL" : "MADRID" ,
        "LANGUAGE" : "SPANISH" ,
        "GDP_RANK" : 15
    } ,
    "country_4" : {
        "NAME" : "DENMARK" ,
        "CAPITAL" : "COPENHAGEN" ,
        "LANGUAGE" : "DANISH" ,
        "GDP_RANK" : 37
    } ,
    "country_5" : {
        "NAME" : "FRANCE" ,
        "CAPITAL" : "PARIS" ,
        "LANGUAGE" : "FRENCH" ,
        "GDP_RANK" : 7
    } ,
    "country_6" : {
        "NAME" : "POLAND" ,
        "CAPITAL" : "POLISH" ,
        "LANGUAGE" : "WARSAW" ,
        "GDP_RANK" : 21
    }   }

print(europe)

# METHOD TWO

country_1 = {
    "NAME" : "GERMANY" ,
    "CAPITAL" : "BERLIN" ,
    "LANGUAGE" : "GERMAN" ,
    "GDP_RANK" : 3
    } 

country_2 = {
    "NAME" : "ITALY" ,
    "CAPITAL" : "ROME" ,
    "LANGUAGE" : "ITALIAN" ,
    "GDP_RANK" : 8
    } 

country_3 = {
        "NAME" : "SPAIN" ,
        "CAPITAL" : "MADRID" ,
        "LANGUAGE" : "SPANISH" ,
        "GDP_RANK" : 15
    }
 
country_4 = {
        "NAME" : "DENMARK" ,
        "CAPITAL" : "COPENHAGEN" ,
        "LANGUAGE" : "DANISH" ,
        "GDP_RANK" : 37
    }
 
country_5 = {
        "NAME" : "FRANCE" ,
        "CAPITAL" : "PARIS" ,
        "LANGUAGE" : "FRENCH" ,
        "GDP_RANK" : 7
    }

country_6 = {
        "NAME" : "POLAND" ,
        "CAPITAL" : "POLISH" ,
        "LANGUAGE" : "WARSAW" ,
        "GDP_RANK" : 21
    }

countries = {
    "country_1" : country_1 ,
    "country_2" : country_2 ,
    "country_3" : country_3 ,
    "country_4" : country_4 ,
    "country_5" : country_5 ,
    "country_6" : country_6 
}

print(countries)