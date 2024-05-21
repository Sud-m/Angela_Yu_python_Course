names = ["Angela", "Beth", "Caronline", "Nanda", "Avni", "Elanor", "Freddie"]
newname = [name.upper() for name in names if len(name) > 4]
print(newname)