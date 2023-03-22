# code.py
# vamos fazer um "adicionador" de todos os nums recebidos pela linha de comandos

def adder(
    p_list_of_numbers:list,
    p_b_show_errors:bool=True
)->float:
    the_sum:float=0
    for thing in p_list_of_numbers:
        try:
            n = float(thing)
            the_sum+=n
        except Exception as e:
            if(p_b_show_errors):
                print(str(e))
            # if
        # try-except
    # for
    return the_sum
# def adder

import sys

b_being_called_from_cli:bool = __name__ == "__main__"
if (b_being_called_from_cli):
    i_how_many_things:int = len(sys.argv)
    if (i_how_many_things>1):
        the_things_to_sum = sys.argv[1:]
        result = adder(the_things_to_sum)
        msg:str = f"The sum of {the_things_to_sum} = {result}"
        print(msg)
    # if
    else:
        msg:str = "Please provide some numbers"
        print(msg)
    # if-else
# if