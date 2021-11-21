from input_code import solution
import sys

def test_code_from_student():
    #test_cases = get_test_cases()
    #expected = get_expected_outputs()
    code = sys.argv[0]
    code_result = solution(code)

    print(code_result)
    return code_result

test_code_from_student()