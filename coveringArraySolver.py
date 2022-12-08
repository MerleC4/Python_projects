# Merle Crutchfield
# 11/29/2022
# CSC436 HW5 Q2
# This solves the following prompt:
# "Suppose that a system can be configured by setting four binary-valued factors, and that
# you want to test all 2-way interactions between factors. Create no more than 5 tests to 
# test all 2-way interactions.
# 
# Used for solving covering arrays of length 4 for 2 way interactions. Yields 24 unique answers.
# *Note* This is a NP problem, which is why this solution only determines arrays of length 4
# and not all lengths.

def testOFFOFF(test1, test2, test3, test4, test5):
    # test 00
    f = 0

    if (test1[0] == 0 and test1[1] == 0) or (test2[0] == 0 and test2[1] == 0) \
        or (test3[0] == 0 and test3[1] == 0) or (test4[0] == 0 and test4[1] == 0) \
        or (test5[0] == 0 and test5[1] == 0):
            f += 1

    if (test1[0] == 0 and test1[2] == 0) or (test2[0] == 0 and test2[2] == 0) \
        or (test3[0] == 0 and test3[2] == 0) or (test4[0] == 0 and test4[2] == 0) \
        or (test5[0] == 0 and test5[2] == 0):
            f += 1

    if (test1[0] == 0 and test1[3] == 0) or (test2[0] == 0 and test2[3] == 0) \
        or (test3[0] == 0 and test3[3] == 0) or (test4[0] == 0 and test4[3] == 0) \
        or (test5[0] == 0 and test5[3] == 0):
            f += 1

    if (test1[1] == 0 and test1[2] == 0) or (test2[1] == 0 and test2[2] == 0) \
        or (test3[1] == 0 and test3[2] == 0) or (test4[1] == 0 and test4[2] == 0) \
        or (test5[1] == 0 and test5[2] == 0):
            f += 1

    if (test1[1] == 0 and test1[3] == 0) or (test2[1] == 0 and test2[3] == 0) \
        or (test3[1] == 0 and test3[3] == 0) or (test4[1] == 0 and test4[3] == 0) \
        or (test5[1] == 0 and test5[3] == 0):
            f += 1

    if (test1[2] == 0 and test1[3] == 0) or (test2[2] == 0 and test2[3] == 0) \
        or (test3[2] == 0 and test3[3] == 0) or (test4[2] == 0 and test4[3] == 0) \
        or (test5[2] == 0 and test5[3] == 0):
            f += 1

    return f

def testOFFON(test1, test2, test3, test4, test5):
    # test 01
    f = 0

    if (test1[0] == 0 and test1[1] == 1) or (test2[0] == 0 and test2[1] == 1) \
        or (test3[0] == 0 and test3[1] == 1) or (test4[0] == 0 and test4[1] == 1) \
        or (test5[0] == 0 and test5[1] == 1):
            f += 1

    if (test1[0] == 0 and test1[2] == 1) or (test2[0] == 0 and test2[2] == 1) \
        or (test3[0] == 0 and test3[2] == 1) or (test4[0] == 0 and test4[2] == 1) \
        or (test5[0] == 0 and test5[2] == 1):
            f += 1

    if (test1[0] == 0 and test1[3] == 1) or (test2[0] == 0 and test2[3] == 1) \
        or (test3[0] == 0 and test3[3] == 1) or (test4[0] == 0 and test4[3] == 1) \
        or (test5[0] == 0 and test5[3] == 1):
            f += 1

    if (test1[1] == 0 and test1[2] == 1) or (test2[1] == 0 and test2[2] == 1) \
        or (test3[1] == 0 and test3[2] == 1) or (test4[1] == 0 and test4[2] == 1) \
        or (test5[1] == 0 and test5[2] == 1):
            f += 1

    if (test1[1] == 0 and test1[3] == 1) or (test2[1] == 0 and test2[3] == 1) \
        or (test3[1] == 0 and test3[3] == 1) or (test4[1] == 0 and test4[3] == 1) \
        or (test5[1] == 0 and test5[3] == 1):
            f += 1

    if (test1[2] == 0 and test1[3] == 1) or (test2[2] == 0 and test2[3] == 1) \
        or (test3[2] == 0 and test3[3] == 1) or (test4[2] == 0 and test4[3] == 1) \
        or (test5[2] == 0 and test5[3] == 1):
            f += 1

    return f

def testONOFF(test1, test2, test3, test4, test5):
    # test 10
    f = 0

    if (test1[0] == 1 and test1[1] == 0) or (test2[0] == 1 and test2[1] == 0) \
        or (test3[0] == 1 and test3[1] == 0) or (test4[0] == 1 and test4[1] == 0) \
        or (test5[0] == 1 and test5[1] == 0):
            f += 1

    if (test1[0] == 1 and test1[2] == 0) or (test2[0] == 1 and test2[2] == 0) \
        or (test3[0] == 1 and test3[2] == 0) or (test4[0] == 1 and test4[2] == 0) \
        or (test5[0] == 1 and test5[2] == 0):
            f += 1

    if (test1[0] == 1 and test1[3] == 0) or (test2[0] == 1 and test2[3] == 0) \
        or (test3[0] == 1 and test3[3] == 0) or (test4[0] == 1 and test4[3] == 0) \
        or (test5[0] == 1 and test5[3] == 0):
            f += 1

    if (test1[1] == 1 and test1[2] == 0) or (test2[1] == 1 and test2[2] == 0) \
        or (test3[1] == 1 and test3[2] == 0) or (test4[1] == 1 and test4[2] == 0) \
        or (test5[1] == 1 and test5[2] == 0):
            f += 1

    if (test1[1] == 1 and test1[3] == 0) or (test2[1] == 1 and test2[3] == 0) \
        or (test3[1] == 1 and test3[3] == 0) or (test4[1] == 1 and test4[3] == 0) \
        or (test5[0] == 1 and test5[3] == 0):
            f += 1

    if (test1[2] == 1 and test1[3] == 0) or (test2[2] == 1 and test2[3] == 0) \
        or (test3[2] == 1 and test3[3] == 0) or (test4[2] == 1 and test4[3] == 0) \
        or (test5[2] == 1 and test5[3] == 0):
            f += 1

    return f

def testONON(test1, test2, test3, test4, test5):
    # test 00
    f = 0

    if (test1[0] == 1 and test1[1] == 1) or (test2[0] == 1 and test2[1] == 1) \
        or (test3[0] == 1 and test3[1] == 1) or (test4[0] == 1 and test4[1] == 1) \
        or (test5[0] == 1 and test5[1] == 1):
            f += 1

    if (test1[0] == 1 and test1[2] == 1) or (test2[0] == 1 and test2[2] == 1) \
        or (test3[0] == 1 and test3[2] == 1) or (test4[0] == 1 and test4[2] == 1) \
        or (test5[0] == 1 and test5[2] == 1):
            f += 1

    if (test1[0] == 1 and test1[3] == 1) or (test2[0] == 1 and test2[3] == 1) \
        or (test3[0] == 1 and test3[3] == 1) or (test4[0] == 1 and test4[3] == 1) \
        or (test5[0] == 1 and test5[3] == 1):
            f += 1

    if (test1[1] == 1 and test1[2] == 1) or (test2[1] == 1 and test2[2] == 1) \
        or (test3[1] == 1 and test3[2] == 1) or (test4[1] == 1 and test4[2] == 1) \
        or (test5[1] == 1 and test5[2] == 1):
            f += 1

    if (test1[1] == 1 and test1[3] == 1) or (test2[1] == 1 and test2[3] == 1) \
        or (test3[1] == 1 and test3[3] == 1) or (test4[1] == 1 and test4[3] == 1) \
        or (test5[1] == 1 and test5[3] == 1):
            f += 1

    if (test1[2] == 1 and test1[3] == 1) or (test2[2] == 1 and test2[3] == 1) \
        or (test3[2] == 1 and test3[3] == 1) or (test4[2] == 1 and test4[3] == 1) \
        or (test5[2] == 1 and test5[3] == 1):
            f += 1

    return f

def arrays():
    arr = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1],
        [0,1,0,0], [0,1,0,1], [0,1,1,0], [0,1,1,1],
        [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1],
        [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]
    ans = []
    for i in range(16):
        for j in range(16):
            for k in range(16):
                for l in range(16):
                    for m in range(16):
                        f = 0
                        test1 = arr[i]
                        test2 = arr[j]
                        test3 = arr[k]
                        test4 = arr[l]
                        test5 = arr[m]

                        final = [test1, test2, test3, test4, test5]


                        if testOFFOFF(test1, test2, test3, test4, test5) == 6:
                            f += 1

                        if testOFFON(test1, test2, test3, test4, test5) == 6:
                            f += 1

                        if testONOFF(test1, test2, test3, test4, test5) == 6:
                            f += 1

                        if testONON(test1, test2, test3, test4, test5) == 6:
                            f += 1

                        if f == 4:
                            if not sorted(final) in ans:
                                ans.append(sorted(final))
                                print(test1, end=' ')
                                print(test2, end=' ')
                                print(test3, end=' ')
                                print(test4, end=' ')
                                print(test5, end=' ')
                                print()

    print("total: " + str(len(ans)))


arrays()