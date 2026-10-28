## dictionaries 
## key and vlaues ni store cheskuntadi 
## ordered , allow multiple data types , { } curly bracket uses keys >> unique always the value is mutuable  but key remaing unique 
## key value pairss gaa store cheskuntundi 
## example 


students={"vishal":100,
          "syam": 200,
          "bruhan":1000}

max_marks=0

for name ,mark in students.items():
    if mark>max_marks:
        max_marks=mark
        topper=name
print(topper)
print(max_marks)