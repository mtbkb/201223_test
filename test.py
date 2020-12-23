if __name__ == '__main__':
    keys = []
    values = []
    with open("input.txt", mode='r') as f:
        for line in f:
            i = line.find(':')
            if i != -1:
                keys.append(int(line[:i]))
                values.append(line[i + 1:-1])
            else:
                target = int(line[:-1])
                d = dict(zip(keys, values))
                keys.sort()
                ans = ""
                for key in keys:
                    if target % key == 0:
                        ans += d[key]
                
                if(len(ans) == 0):
                    print(target)
                else:
                    print(ans)