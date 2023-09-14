def fetch_lines(filename):
    with open(filename,'r',encoding='utf-8') as file:
        lines=[]
        for line in file:
            lines.append(line)
        return lines

zen=fetch_lines('hikaye.txt')
print(zen)