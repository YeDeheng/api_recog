

line_sel = []
with open('problist', 'r') as f:
    for index, line in enumerate(f):
        p = float(line)
        if p > 0.8:
            line_sel.append(index)

fout = open('bs_sel.txt', 'w')

with open('bootstrap.txt', 'r') as f:
    for index, line in enumerate(f):
        if index in line_sel:
            fout.write(line)

fout.close()
