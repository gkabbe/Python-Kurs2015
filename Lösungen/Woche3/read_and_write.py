def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()
        

def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            print >> f, line
