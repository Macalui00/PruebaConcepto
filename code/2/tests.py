from input_code import sumar

def get_test_cases():
    return {
        "CASE_1": [1, 2],
        "CASE_2": [23,-23],
    }

def get_expected_outputs():
    return {
        "CASE_1": 3,
        "CASE_2": 0,
    }

def test_code():
    test_cases = get_test_cases()
    expected = get_expected_outputs()
    test_cases_count = len(test_cases)
    passed_test_cases = 0
    failed_test_cases = []

    for label in test_cases.keys():
        code_result = sumar(test_cases[label][0],test_cases[label][1])
        if code_result == expected[label]:
            passed_test_cases += 1
        else:
            failed_test_cases.append(label)

    print("Supero ", passed_test_cases, " de ", test_cases_count, " casos de prueba.")
    
    if len(failed_test_cases) > 0:
        print("Casos de prueba no superados:", ", ".join(failed_test_cases))

test_code()