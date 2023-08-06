def readt(filename):
    with open(filename) as f:
        tests = iter([_.replace("\n", "") for _ in f.readlines()])
    return tests
