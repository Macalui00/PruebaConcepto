from input_code import sumar
import sys

def test_code_from_student():
    code = sys.argv[1]
    input = list(code.split(','))
    input2 = []
    for i in input:
      input2.append(int(i))
    code_result = sumar(input2[0], input2[1])
    print(code_result)

test_code_from_student()