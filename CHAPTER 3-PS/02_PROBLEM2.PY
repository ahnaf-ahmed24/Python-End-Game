letter = ''' Dear <|Name|> ,
             You are selected !
<|Date|> '''

print(letter.replace("<|Name|>" , "Ahnaf Ahmed").replace(
    "<|Date|>", "3 September 2024"
))