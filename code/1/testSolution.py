from input_code import solution
import sys

def test_code_from_student():
    code = sys.argv[1]
    input1 = list(code.split(','))
    input2 = []
    for i in input1:
      input2.append(int(i))
    code_result = solution(input2)
    print(code_result)

test_code_from_student()