# -lenscalculator.py *- coding: utf-8 -*-
"""
Created on Fri Apr  3 09:45:13 2020
@author: Bartek Dell
Script calculating lens magnification
"""

option = [[1, 0.64], [2, 1], [3, 1.3], [4, 1.5], [5, 1.6], [6, 2.0],
          [7, 2.7], [8, 4.55], [9, 5.62]]


def calcul(matrix):
    fmin = int(input("Input minimum focal length of your lens: "))
    fmax = int(input("Input maximum focal length of your lens: "))
    print()

    x = 43.3

#calculating min focal length

    closemin = float(fmin * matrix / x)

#calculating max focal length

    closemax = float(fmax * matrix / x)

    print("Your lens closes objects from ", round(
        closemin, 2), "x to ", round(closemax, 2), "x")

    print()
    again = input("Do you want to try again? Y/N - ")
    if again.lower() == ("y"):
        lens()
    else:
        return True


def lens():
    """ Find out what the user wants to do next. """
    print("Choose your matrix size")
    print("   1) Medium Format  x 0.64")
    print("   2) Full Format    x 1.0")
    print("   3) APS-H          x 1.3")
    print("   4) APS-C Nikon    x 1.5")
    print("   5) APS-C Canon    x 1.6")
    print("   6) 4/3            x 2.0")
    print("   7) 1\"             x 2.7")
    print("   8) 1/1.7\"         x 4.55")
    print("   9) 1/2.3\"         x 5.62")
    print("   0) Quit Calculator")

    m = input("Choice: ")
    if m.isdigit():
        m = int(m)
        if m == 0:
            return True
        elif m in range(1,10):
            m -= m
            matrix = option[m][1]
            calcul(matrix)
        else:
            print("Incorrect input, try again")
            lens()
    else:
        print("Incorrect input, try again")
        lens()


print("This is the program calculating how many times your lens closes \
      objects up")
lens()
# if lens() == matrix:
#     calcul(matrix)

print("Good bye then...")


# if __name__ == '__main__':
#      lens()
