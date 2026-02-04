from typing import List


# =========================================================
# Candidate Stub (INTENTIONALLY WRONG / INCOMPLETE)
# ---------------------------------------------------------
# Interview Question:
# Find the SECOND LARGEST number in an integer array.
#
# Rules (state clearly in interview):
# - Array must have at least 2 distinct elements
# - If second largest does NOT exist, return None
#
# Candidate will implement logic.
# Currently returns None so most tests FAIL.
# =========================================================
def get_second_largest(arr: List[int]):
    """
    Return the second largest DISTINCT number in the array.
    If it does not exist, return None.
    """
    # TODO: Candidate implements logic
    return None  # intentional stub


# =========================================================
# Tiny Test Harness
# =========================================================
def _assert_equal(test_name: str, arr: List[int], expected) -> bool:
    got = get_second_largest(arr)
    if got != expected:
        print(f"[FAIL] {test_name}")
        print(f"  input    = {arr}")
        print(f"  expected = {expected}")
        print(f"  got      = {got}")
        print("-" * 60)
        return False
    print(f"[PASS] {test_name}")
    return True


# =========================================================
# Individual Test Cases (ONE FUNCTION EACH)
# =========================================================
def test_case_01_normal_array() -> bool:
    arr = [10, 20, 30, 40]
    expected = 30
    return _assert_equal("test_case_01_normal_array", arr, expected)


def test_case_02_unsorted_array() -> bool:
    arr = [4, 1, 9, 2, 7]
    expected = 7
    return _assert_equal("test_case_02_unsorted_array", arr, expected)


def test_case_03_duplicates_present() -> bool:
    arr = [10, 10, 9, 8]
    expected = 9
    return _assert_equal("test_case_03_duplicates_present", arr, expected)


def test_case_04_all_elements_same() -> bool:
    arr = [5, 5, 5, 5]
    expected = None
    return _assert_equal("test_case_04_all_elements_same", arr, expected)


def test_case_05_two_elements_valid() -> bool:
    arr = [1, 2]
    expected = 1
    return _assert_equal("test_case_05_two_elements_valid", arr, expected)


def test_case_06_two_elements_same() -> bool:
    arr = [7, 7]
    expected = None
    return _assert_equal("test_case_06_two_elements_same", arr, expected)


def test_case_07_negative_numbers() -> bool:
    arr = [-10, -3, -20, -1]
    expected = -3
    return _assert_equal("test_case_07_negative_numbers", arr, expected)


def test_case_08_mixed_positive_negative() -> bool:
    arr = [-1, 0, 5, 3, 2]
    expected = 3
    return _assert_equal("test_case_08_mixed_positive_negative", arr, expected)


def test_case_09_single_element() -> bool:
    arr = [100]
    expected = None
    return _assert_equal("test_case_09_single_element", arr, expected)


def test_case_10_large_values() -> bool:
    arr = [100000, 99999, 123456, 50000]
    expected = 100000
    return _assert_equal("test_case_10_large_values", arr, expected)


# =========================================================
# Driver Function
# =========================================================
def run_all_tests() -> None:
    tests = [
        test_case_01_normal_array,
        test_case_02_unsorted_array,
        test_case_03_duplicates_present,
        test_case_04_all_elements_same,
        test_case_05_two_elements_valid,
        test_case_06_two_elements_same,
        test_case_07_negative_numbers,
        test_case_08_mixed_positive_negative,
        test_case_09_single_element,
        test_case_10_large_values,
    ]

    passed = 0
    for test in tests:
        if test():
            passed += 1

    total = len(tests)
    print(f"\nSummary: {passed}/{total} tests passed.")
    if passed != total:
        print("Implement get_second_largest(arr) to make all tests pass.")


if __name__ == "__main__":
    run_all_tests()
