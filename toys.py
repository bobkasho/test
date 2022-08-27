full = False

donations = []
full_load = 45

toys = ['robot', 'doll', 'ball', 'wolfer']

while not full:
    for toy in toys:
        donations.append(toy)
        size = len(donations)
        if (size >= full_load):
            full = True

print('Full', len(donations), 'toys') #Full 48 toys

print(donations) #['robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer', 'robot', 'doll', 'ball', 'wolfer']


# я чомусь не зрозумів поки, як так, у фулл_лоад значення 45, а коли робиш Прінт лен(донатіонс) їх стає 48... хм...
# розібрався - він не по одній уграшці брав і тулив в донатіонс, а весь список до тих пір поки не = або більше. отакого
# буду вважати місію завершеною
