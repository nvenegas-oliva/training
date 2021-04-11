
mapping = {
    '1': ['A', 'B', 'C'],
    '2': ['D', 'E', 'F']
}

digits = '12'

result = []
for d in digits:  # 1, 2
    print(mapping[d])
    temp = []
    for i in mapping[d]:  # ['A', 'B', 'C'], ['D', 'E', 'F']
        print(i)
        temp.append(i)  # 'A', 'B', 'C'  // 'D', 'E', 'F'



['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
