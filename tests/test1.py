from changecode.code import Code

with open("test2.py", "r+") as file:
    code = Code(file=file)
    code.add_import_from("pathlib", "Path")
    code.append_in_lists("hi", "6, 7")
    code.save()
