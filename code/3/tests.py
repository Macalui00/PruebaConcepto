from input_code import factorial
#, doblar, sumar, es_par

def get_test_cases():
    return {
        "CERO": 0,
        "UNO": 1,
        "CUATRO": 4,
        "DIEZ": 10,
    }

def get_expected_outputs():
    return {
        "CERO": 1,
        "UNO": 1,
        "CUATRO": 24,
        "DIEZ": 3628800,
    }

def test_code():
    test_cases = get_test_cases()
    expected = get_expected_outputs()
    test_cases_count = len(test_cases)
    passed_test_cases = 0
    failed_test_cases = []

    for label in test_cases.keys():
        code_result = factorial(test_cases[label])
        if code_result == expected[label]:
            passed_test_cases += 1
        else:
            failed_test_cases.append(label)

    print("Passed", passed_test_cases, "out of", test_cases_count, "test cases.")
    
    if len(failed_test_cases) > 0:
        print("Test cases not passed:", ", ".join(failed_test_cases))

test_code()