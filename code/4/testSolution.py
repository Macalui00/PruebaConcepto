from input_code import gen_primos
import sys

def test_code_from_student():
    code = sys.argv[1]
    input = list(code.split(','))
    input2 = []
    for i in input:
      input2.append(int(i))
    code_result = gen_primos(input2[0])
    print(code_result)

test_code_from_student()