from input_code import solution


def get_test_cases():
    return {
        "SMALL_INPUT": [1, 2, 3,5],
        "LARGE_INPUT": [1, 2, 3] * 1000 + [4] * 20 + [5] + [6],
        "LARGE_INPUT_2": [1, 2, 3] * 1000 + [4] * 20 + [5] + [7],
        
    }

def get_expected_outputs():
    return {
        "SMALL_INPUT": 5,
        "LARGE_INPUT": 6,
        "LARGE_INPUT_2": 7,
    }

def test_code():
    test_cases = get_test_cases()
    expected = get_expected_outputs()
    test_cases_count = len(test_cases)
    passed_test_cases = 0
    failed_test_cases = []

    for label in test_cases.keys():
        code_result = solution(test_cases[label])
        if code_result == expected[label]:
            passed_test_cases += 1
        else:
            failed_test_cases.append(label)

    print("Supero ", passed_test_cases, " de ", test_cases_count, " casos de prueba.")
    
    if len(failed_test_cases) > 0:
        print("Casos de prueba no superados:", ", ".join(failed_test_cases))

test_code()