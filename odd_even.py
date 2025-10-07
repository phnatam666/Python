class OddStream:
    def __init__(self):
        self.current = -1  # start before the first odd number

    def next(self):
        self.current += 2
        return self.current


class EvenStream:
    def __init__(self):
        self.current = -2  # start before the first even number

    def next(self):
        self.current += 2
        return self.current


def print_from_stream(n, stream):
    for _ in range(n):
        print(stream.next())


def main():
    q = 5
    for _ in range(q):
        line = input().strip().split()
        typ, n = line[0], int(line[1])

        if typ == "odd":
            stream = OddStream()
        elif typ == "even":
            stream = EvenStream()
        else:
            continue  # skip invalid input or raise error

        print_from_stream(n, stream)


if __name__ == "__main__":
    main()
