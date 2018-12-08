
import math

def countAtg(dnaString, n):
        i = 0
        ncount = 0
        lengde = len(dnaString)
        nCountOnePush = 0
        nCountTwoPush = 0

        count = 0
        for i in range(n-3, 3):
            try:
                if dnaString[i:i+3]=="ATG":
                    ncount += 1

                elif dnaString[i+1:i+4]=="ATG":
                    nCountOnePush += 1

                elif dnaString[i+2:i+5]=="ATG":
                    nCountTwoPush += 1
            except IndexError:
                continue


        if ncount>=n:
            return 0
        elif nCountOnePush>=n:
            return 1
        elif nCountTwoPush>=n:
            return 2

        blocks = 0
        minLetters = 0
        i = 0
        while i<lengde-3:

            if blocks>=n:
                return minLetters
            if dnaString[i:i+3]=="ATG":
                blocks += 1
                i+=3
            elif dnaString[i:i+2]=="AT":
                minLetters += 1
                i+=2
                dnaString = dnaString[:i+2] + "G" + dnaString[i+2:]
            elif dnaString[i:i+1]=="AG":
                i+=2
                minLetters += 1
                dnaString = dnaString[:i+1]+"T"+dnaString[i+1:]
            elif dnaString[i:i+1]=="TG":
                i+=2
                minLetters += 1
                dnaString = dnaString[:i]+"A"+dnaString[i]
            i += 1











def main():
    from sys import stdin

    blocks = int(stdin.readline())
    dnaString = stdin.readline()
    print(countAtg(dnaString, blocks))

main()
