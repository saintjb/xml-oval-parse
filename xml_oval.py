
from bs4 import BeautifulSoup

with open("scanoval1.xml", "r", encoding='utf8') as file:
    dataset = BeautifulSoup(file, 'lxml')
    result = dataset.findAll("definition")
    platforms = dataset.findAll("platform")
    product = dataset.findAll("product")
    mass1 = list()
    mass2 = list()
    for pl in platforms:
        mass1.append(str(pl))
    for pr in product:
        mass2.append(str(pr))
    res1 = set(mass1)
    res2 = set(mass2)

    with open('result.txt', 'w') as dest:
        for i in res1:
            dest.write(i)
            dest.write('\n')
        dest.write("-------------------------------------------------------------------------")
        dest.write('\n')
        for j in res2:
            dest.write(j)
            dest.write('\n')
