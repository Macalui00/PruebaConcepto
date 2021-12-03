from input_code import gen_primos

def get_test_cases():
    return {
        "CASO_SIMPLE": 3,
        "CASO_COMPLEJO": 7,
    }

def get_expected_outputs():
    return {
        "CASO_SIMPLE": [2,3,5],
        "CASO_COMPLEJO": [2,3,5,7,11,13,17]
    }

def test_code():
    test_cases = get_test_cases()
    expected = get_expected_outputs()
    test_cases_count = len(test_cases)
    passed_test_cases = 0
    failed_test_cases = []

    for label in test_cases.keys():
        code_result = gen_primos(test_cases[label])
        if code_result == expected[label]:
            passed_test_cases += 1
        else:
            failed_test_cases.append(label)

    print("Supero ", passed_test_cases, " de ", test_cases_count, " casos de prueba.")
    
    if len(failed_test_cases) > 0:
        print("Casos de prueba no superados:", ", ".join(failed_test_cases))

test_code()