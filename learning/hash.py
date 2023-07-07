names = ['mohammad', 'elham', 'saeed']
for name in names:
    hash = 0
    for c in name:
        hash += ord(c)

    print(name,hash%10)