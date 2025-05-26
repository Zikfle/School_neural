alldots = [[2,3,'A'] , [6,7,'A'] , [3,2,'A'] , [14,2,'A'], [30,5,'A'] , [3,10,'B'] , [5,60,'B'] , [9,20,'B'] ,[14,80,'B'] , [30,61,'B']]

for dot in alldots:
    rest = (-8 * dot[0]) + (-10 * dot[1]) - 80
    if rest > 0:
        pred = 'A'
    else:
        pred = 'B'
    if pred != dot[2]:
        print('error********************************')
    print(f'label : {dot[2]}')
    print(f'pred  : {pred}')
    print('')
