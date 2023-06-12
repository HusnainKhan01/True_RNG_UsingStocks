#!/usr/bin/env python3

"""FIPS 140-2: RNG Power-Up Tests"""

# Asses the quality of your TRNG by running the statistical random
# number generator tests from Chapter 4.9.1 (Power-Up Tests) of "FIPS
# PUB 140-2 - SECURITY REQUIREMENTS FOR CRYPTOGRAPHIC MODULES". The
# document is available on the handout server.

FILENAME='random.dat'
#FILENAME='random_radio_noise.dat'

import functools
import pdb

def readRandomBits(filename):
    """Read file and return it as list of bits."""
    rn = []
    rnFile = open(filename, 'rb')
    rn = rnFile.read()
    rnFile.close()
    return(functools.reduce(lambda x,y: x+int2bin(y,8), rn, []))

def int2bin(x, n):
    """Convert integer to array of bits.
    x : integer
    n : length of bit array"""
    b = list(map(lambda x: ord(x)-ord('0'), list(bin(x)[2:])))
    return([0]*(n-len(b)) + b)

def bin2int(b):
    """Convert array of bits to integer."""
    return(int("".join(map(lambda x: chr(x+ord('0')), b)), 2))

def testRandomNumbers(randomBits):
    print('Monobit Test:   %s' % repr(monobitTest(randomBits)))
    print('Poker Test:     %s' % repr(pokerTest(randomBits)))
    print('Runs Test:      %s' % repr(runsTest(randomBits)))
    print('Long Runs Test: %s' % repr(longRunsTest(randomBits)))

def monobitTest(randomBits):
    """FIPS 140-2 monobit test"""
    # Count the number of ones in the 20,000 bit stream. Denote this
    # quantity by x.
    #
    # The test is passed if 9725 < x < 10275
    # pass
##################
    count = 0
    for i in range(len(randomBits)):
        if randomBits[i] == 1:
            count += 1
    count
    result = False
    if count < 10275 & count > 9725:
        result = True
    assert (result == True)

def pokerTest(randomBits):
    """FIPS 140-2 poker test"""
    # Divide the 20000 bit stream into 5000 contiguous 4 bit
    # segments. Count and store the number of occurrences of the 16
    # possible 4 bit values. Denote f[i] as the number of each 4 bit
    # value i where 0 < i < 15.
    #
    # Evaluate the following:
    #                   15
    #                   --
    # x = (16/5000) * ( \  f[i]^2 ) - 5000
    #                   /
    #                   --
    #                  i=0
    #
    # The test is passed if 2.16 < x < 46.17
    #
    # See fips_140_2.pdf, page 39-40
    pass

def runsTest(randomBits):
    """FIPS 140-2 runs test"""
    # A run is defined as a maximal sequence of consecutive bits of
    # either all ones or all zeros that is part of the 20000 bit
    # sample stream. The incidences of runs (for both consecutive
    # zeros and consecutive ones) of all lengths (>= 1) in the
    # sample stream should be counted and stored.
    #
    # The test is passed if the runs that occur (of lengths 1 through
    # 6) are each within the corresponding interval specified in the
    # table below. This must hold for both the zeros and ones (i.e.,
    # all 12 counts must lie in the specified interval). For the
    # purposes of this test, runs of greater than 6 are considered to
    # be of length 6.
    #
    # Length      Required Interval
    # of Run 
    # 1           2343 - 2657
    # 2           1135 - 1365
    # 3            542 -  708
    # 4            251 -  373
    # 5            111 -  201
    # 6+           111 -  201
    #
    # See fips_140_2.pdf, page 40

    # count runs of 1,
    count1 = countRunOf1(randomBits)
    # count runs of 2,
    count2 = countRunOf2(randomBits)
    # count runs of 3,
    count3 = countRunOf3(randomBits)
    # count runs of 4,
    count4 = countRunOf4(randomBits)
    # count runs of 5,
    count5 = countRunOf5(randomBits)
    # count runs of 6,
    count6 = countRunOf6(randomBits, 6)
    result = False
    # 1           2343 - 2657
    if count1 < 2657 & count1 > 2342:
        if count2 < 1365 & count2 > 1135:
            if count3 < 708 & count3 > 542:
                if count4 < 373 & count > 251:
                    if count5 < 201 & count5 > 111:
                        if count6 < 201 & count6 > 111:
                            result = True
    assert (result == True)
##################
    
def longRunsTest(randomBits):
    """FIPS 140-2 long runs test"""
    # A long run is defined to be a run of length 26 or more (of
    # either zeros or ones). On the sample of 20000 bits, the test is
    # passed if there are no long runs.
    #
    # See fips_140_2.pdf, page 40

##################
# YOUR CODE HERE #
    result = False
    count = countRunOf6(randomBits, 26)
    print(count)
    if count == 0:
        result = True

    assert (result == True)
##################
def countRunOf6(randomBits, number):
    count1 = 0
    count = 0
    prevValue = randomBits[0]
    i = 0
    while i < len(randomBits) - 1:
        while i < len(randomBits) - 1:

            i += 1
            if prevValue == randomBits[i]:
                count1 += 1
            else:
                prevValue = randomBits[i]
                break
            prevValue = randomBits[i]

        if count1 >= number-1:
            count += 1
        count1 = 0

    return count

def countRunOf5(randomBits):
    count = 0
    prevValue = randomBits[0]
    prevValue2 = randomBits[1]
    prevValue3 = randomBits[2]
    prevValue4 = randomBits[3]
    flag = False
    value = 0
    prevIdx = 0
    for i in range(len(randomBits)):
        if i > 3:
            if flag:
                if randomBits[prevIdx + 1] != value:
                    if (prevIdx - 5) < 0:
                        count += 1
                    elif randomBits[prevIdx - 5] != value:
                        count += 1
                flag = False
            if prevValue == prevValue2:
                if prevValue == prevValue3:
                    if prevValue == prevValue4:
                        if prevValue == randomBits[i]:
                            flag = True
                            value = prevValue
                            prevIdx = i

            prevValue = randomBits[i - 3]
            prevValue2 = randomBits[i - 2]
            prevValue3 = randomBits[i - 1]
            prevValue4 = randomBits[i]

    if randomBits[len(randomBits) - 1] == randomBits[len(randomBits) - 2]:
        if randomBits[len(randomBits) - 3] == randomBits[len(randomBits) - 1]:
            if randomBits[len(randomBits) - 4] == randomBits[len(randomBits) - 1]:
                if randomBits[len(randomBits) - 5] == randomBits[len(randomBits) - 1]:
                    if randomBits[len(randomBits) - 1] != randomBits[len(randomBits) - 6]:
                        count += 1
    return count


def countRunOf4(randomBits):
    count = 0
    prevValue = randomBits[0]
    prevValue2 = randomBits[1]
    prevValue3 = randomBits[2]
    flag = False
    value = 0
    prevIdx = 0
    for i in range(len(randomBits)):
        if i > 2:
            if flag:
                if randomBits[prevIdx + 1] != value:
                    if (prevIdx - 4) < 0:
                        count += 1
                    elif randomBits[prevIdx - 4] != value:
                        count += 1
                flag = False
            if prevValue == prevValue2:
                if prevValue == prevValue3:
                    if prevValue == randomBits[i]:
                        flag = True
                        value = prevValue
                        prevIdx = i

            prevValue = randomBits[i - 2]
            prevValue2 = randomBits[i - 1]
            prevValue3 = randomBits[i]

    if randomBits[len(randomBits) - 1] == randomBits[len(randomBits) - 2]:
        if randomBits[len(randomBits) - 3] == randomBits[len(randomBits) - 1]:
            if randomBits[len(randomBits) - 4] == randomBits[len(randomBits) - 1]:
                if randomBits[len(randomBits) - 1] != randomBits[len(randomBits) - 5]:
                    count += 1
    return count


def countRunOf3(randomBits):
    count = 0
    prevValue = randomBits[0]
    prevValue2 = randomBits[1]
    flag = False
    value = 0
    prevIdx = 0
    for i in range(len(randomBits)):
        if i > 1:
            if flag:
                if randomBits[prevIdx + 1] != value:
                    if (prevIdx - 3) < 0:
                        count += 1
                    elif randomBits[prevIdx - 3] != value:
                        count += 1
                flag = False
            if prevValue == prevValue2:
                if prevValue == randomBits[i]:
                    flag = True
                    value = prevValue
                    prevIdx = i

            prevValue = randomBits[i-1]
            prevValue2 = randomBits[i]

    if randomBits[len(randomBits) - 1] == randomBits[len(randomBits) - 2]:
        if randomBits[len(randomBits) - 3] == randomBits[len(randomBits) - 1]:
            if randomBits[len(randomBits) - 1] != randomBits[len(randomBits) - 4]:
                count += 1

    return count


def countRunOf2(randomBits):
    # count runs of 2,
    count = 0
    prevValue = randomBits[0]
    flag = False
    value = 0
    prevIdx = 0
    for i in range(len(randomBits)):
        if i != 0:
            if flag:
               if randomBits[prevIdx + 1] != value:
                   if (prevIdx - 2) < 0:
                       count += 1
                   elif randomBits[prevIdx - 2] != value:
                       count += 1
               flag = False
            if prevValue == randomBits[i]:
                flag = True
                value = prevValue
                prevIdx = i
            prevValue = randomBits[i]

    if randomBits[len(randomBits)-1] == randomBits[len(randomBits)-2]:
        if randomBits[len(randomBits)-1] != randomBits[len(randomBits)-3]:
            count += 1

    return count


def countRunOf1(randomBits):
    # count runs of 1,
    count = 0
    prevValue = randomBits[0]
    middleValue = randomBits[1]
    futureValue = randomBits[2]
    j = 0
    # 0100100101100001110001
    # 0101
    for i in range(len(randomBits)):
        if j == 0:
            if prevValue != middleValue:
                count += 1
        elif j == 1:
            if prevValue != middleValue & middleValue != futureValue:
                count += 1
        elif j+1 != len(randomBits):
            prevValue = randomBits[j-1]
            middleValue = randomBits[j]
            futureValue = randomBits[j+1]

            if middleValue != prevValue:
                if middleValue != futureValue:
                    count += 1
        j += 1

    if randomBits[len(randomBits)-1] != randomBits[len(randomBits)-2]:
        count += 1
    return count

if __name__ == "__main__":
    randomBits = readRandomBits(filename=FILENAME)
    testRandomNumbers(randomBits=randomBits)
