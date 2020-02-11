first_row = list(map(float, input('Введіть матричний запис СЛР\n').split(' ')))
matrix = []
odds = [[]]
matrix.append(first_row)

for _ in range(len(first_row) - 2):
    matrix.append(list(map(float, input().split(' '))))
    odds.append([])

print('\nВведіть точність обчислення ε')
while True:
    try:
        e = float(input())
        if e < 0:
            raise Exception
    except:
        print('Введіть коректне значення ε')
        continue
    else:
        break

for i in range(len(first_row) - 1):
    if matrix[i][i] != max(matrix[i], key=abs):
        print('Перша умова не виконується, використайте інший метод')
        exit(0)
print('\nПерша умова виконується')

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
print('\nПереведемо систему до зручного для ітерації вигляду:')
for i in range(len(first_row) - 1):
    print('x' + str(i + 1).translate(SUB), end=' = ')
    x = matrix[i][i]
    matrix[i].pop(i)
    odds[i] = [round(y/-x, 5) for y in matrix[i][:-1]]
    odds[i].insert(0, round(matrix[i][-1]/x, 5))
    matrix[i] = odds[i]
    print(matrix[i][0], end=' ')
    for j in range(1, len(odds[i])):
        print('+' if matrix[i][j] > 0 else '-', end=' ')
        print(abs(matrix[i][j]), end='')
        print('x' + str(j if i >= j else j + 1).translate(SUB), end=' ')
    print()
print()

for i in odds: 
    sum = 0
    print(*['|' + str(y) + '|' for y in i[1:]], sep=" + ", end=' ')
    for j in i[1:]:
        sum += abs(j)
    sum = round(sum, 5)
    print('=', sum, '(< 1)' if sum < 1 else '(!< 1, умова не виконується)')

res = []
print('\nЗа нульові наближення коренів системи приймемо:')
for i in range(0, len(odds)):
    print('x0'.translate(SUP), end='')
    print(str(i + 1).translate(SUB), '=', odds[i][0])
    res.append(odds[i][0])

def iteration(text):
    global res
    print(text)
    temp = []
    for j in range(len(first_row)):
        sum = matrix[j][0]
        print('x' + str(j + 1).translate(SUB) + str(i).translate(SUP), end=' = ')
        print(matrix[j][0], end=' ')
        for k in range(1, len(matrix[j])):
            sum += matrix[j][k]*res[k-1 if j >= k else k]
            print('+' if matrix[j][k] > 0 else '-', end=' ')
            print(abs(matrix[j][k]), end=' ')
            print('*', round(res[k-1 if j >= k else k], 5), end=' ')
        print('=', round(sum, 5))
        temp.append(sum)
    res = temp

i = 1
iteration('\nПідставимо ці значення в праві частини рівнянь:')
prev = res
while True:
    check = True
    i += 1
    prev = res
    iteration('\nПідставимо ці наближення у систему та отримаємо наступні наближення коренів')
    new = res
    print()
    for j in range(len(first_row)):
        print('Δ' + str(j + 1).translate(SUB) + str(i-1).translate(SUP), end=' = ')
        print('|' + 'x' + str(j + 1).translate(SUB) + str(i - 1).translate(SUP), end=' - ')
        print('x' + str(j + 1).translate(SUB) + str(i).translate(SUP) + '|', end=' = ')
        print('|' +  str(round(prev[j], 5)) + ' - ' + str(round(new[j], 5)) + '|', end=' = ')
        diff = abs(round(prev[j], 5) - round(new[j], 5))
        print('{0:.5f}'.format(diff))
        if diff > e:
            check = False
    if check:
        break
print('Ітерацій зроблено:', i)

