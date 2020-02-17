if __name__ == '__main__':
    data = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())

        data[name] = score
    
    second_least = sorted(set(data.values()))[1]

    names = []

    for name in data:
        if data[name] == second_least:
            names.append(name)

    for i in sorted(names):
        print(i)

