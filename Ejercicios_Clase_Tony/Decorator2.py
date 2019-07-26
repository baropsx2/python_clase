import os


def deco_file(timeout):
    def wraper(funcion):
        def process_file(*args, **kargs):
            ips = args[0]
            file_name = args[1]
            for ip in ips:
                if is_alive(ip):
                    kargs["ips_alive"].append(ip)
            if kargs["ips_alive"]:
                return funcion(*args, **kargs)
            return None
        return process_file()
    return wraper


@deco_file(5)
def open_py_c(ips, file_name, ips_alive = []):
    for ip in ips_alive:
        r = get_file(ip, file_name)
        if r:
            return r
    return None


