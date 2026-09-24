from tools import scan_vulnerabilities

def test_eval_detection():
    code = """
user_input = input()
eval(user_input)
"""

    result = scan_vulnerabilities(code)

    assert len(result["findings"]) > 0


def test_clean_code():
    code = """
print("Hello")
"""

    result = scan_vulnerabilities(code)

    assert len(result["findings"]) == 0