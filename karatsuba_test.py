def karatsuba(numA, numB):# функция, реализующая алгоритм Карацубы
    s_numA = str(numA); s_numB = str(numB)
    l_A = len(s_numA)//2; l_B = len(s_numB)//2
    L = min([l_A,l_B])
    l_A -= L;l_B -= L
    
    if l_A>1 and l_B > 1:
        a = int(s_numA[:l_A]); b = int(s_numA[l_A:])
        c = int(s_numB[:l_B]); d = int(s_numB[l_B:])
        p = a + b; q = c + d
        pq = karatsuba(p, q)
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        adbc = pq - ac - bd
        return ac * 10 ** (2*L) + adbc * 10 ** L + bd
    else:
        return numA * numB
# тест, задание 1.6 (Т.Рафгарден "Сов.алгоритм. Т.1")
print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
print(3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627)
