def check_file(funcion):
    def process_file(*args, **kargs):
        file_name = args[0]
        ext = file_name.rsplit(".", 1)[-1]
        support_extensions = funcion.__name__.split("_")[1:]
        if ext in support_extensions:
            return funcion(*args, **kargs)
        return None
    return process_file

@check_file
def process_py(file_name, x, y, z):
    return open(file_name)


f = process_py("generadores.py", 1, 2, "Hi")
print(f.read())
