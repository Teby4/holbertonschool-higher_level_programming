#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            a = my_list_1
            b = my_list_2
            if isinstance(a[i], (int, float)) and isinstance(b[i], (int, float)):
                result.append(a[i] / b[i])
            else:
                print("wrong type")
                result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
