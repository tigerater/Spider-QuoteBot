import pickle

mainfile = open("spiderman1.txt", 'r')
#yourResult = [line.split(',') for line in mainfile.readlines()]

total = mainfile.read()
final = total.split("\n\n");

complete = []

for x in final:
    complete.append(x.split("\n", 1))


with open("Spiderman1FULL.txt", "wb") as fp:
    pickle.dump(complete, fp)


