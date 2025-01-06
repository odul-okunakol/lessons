from io import UnsupportedOperation
#from sys import excepthook


def sayi(a):
    try:
      return 10/a
    except ZeroDivisionError:
        return "0'a bolunmez"
    except UnsupportedOperation:
        return "sayi giriniz"

print(sayi(0))