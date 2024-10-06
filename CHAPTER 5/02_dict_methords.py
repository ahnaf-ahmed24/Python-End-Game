d = {} # Empty Dictionary
marks = {
    "Ahnaf" : 100,
    "Miha" : 56,
    "Konok" : 23,
    0 : "Ahnaf"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ahnaf":99 , "Nolok":67})
print(marks)
print(marks.get("Ahnaf"))
