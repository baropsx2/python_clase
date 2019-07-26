# High level function


def my_open(path):
    return open(path)


def process_file(path, x, y, z = 1):
    return resultado


def check_file(lista_ext, funcion):
    def p_file(p, *args, **kargs):
        ext = p.split(".")[-1]
        if ext in lista_ext:
            r = funcion(p, *args, **kargs)
            return r
        return None
    return p_file


open_pdf = check_file(["txt", "texto"], my_open)
open_pdf(p)
p = "hola.pdf"
open_pdf(p)


process_sps = check_file((["csv", "xls", "xlsx"], process_file))

