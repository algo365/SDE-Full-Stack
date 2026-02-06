from typing import List


# =========================================================
# Candidate Stub (INTENTIONALLY WRONG / INCOMPLETE)
# ---------------------------------------------------------
# Interview Question:
# Find the MAXIMUM SUBARRAY SUM in an integer array.
#
# Rules (define clearly in interview):
# - Subarray must be contiguous
# - Array can contain negative numbers
# - If array is empty, return None
#
# Candidate will implement logic (Kadane / other).
# Currently returns None so MOST tests FAIL.
# =========================================================
def max_subarray_sum(arr: List[int]):
    """
    Return the maximum sum of any contiguous subarray.
    If array is empty, return None.
    """
   
    
# =========================================================
# Tiny Test Harness
# =========================================================
def _assert_equal(test_name: str, arr: List[int], expected) -> bool:
    got = max_subarray_sum(arr)
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
def test_case_01_classic_example() -> bool:
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6  # [4, -1, 2, 1]
    return _assert_equal("test_case_01_classic_example", arr, expected)


def test_case_02_all_positive() -> bool:
    arr = [1, 2, 3, 4]
    expected = 10
    return _assert_equal("test_case_02_all_positive", arr, expected)


def test_case_03_all_negative() -> bool:
    arr = [-8, -3, -6, -2, -5, -4]
    expected = -2
    return _assert_equal("test_case_03_all_negative", arr, expected)


def test_case_04_single_element() -> bool:
    arr = [5]
    expected = 5
    return _assert_equal("test_case_04_single_element", arr, expected)


def test_case_05_single_negative_element() -> bool:
    arr = [-7]
    expected = -7
    return _assert_equal("test_case_05_single_negative_element", arr, expected)


def test_case_06_mixed_small() -> bool:
    arr = [3, -2, 5, -1]
    expected = 6
    return _assert_equal("test_case_06_mixed_small", arr, expected)


def test_case_07_zeroes_present() -> bool:
    arr = [0, -3, 1, 1]
    expected = 2
    return _assert_equal("test_case_07_zeroes_present", arr, expected)


def test_case_08_large_drop_then_rise() -> bool:
    arr = [10, -20, 30, -5, 40]
    expected = 65
    return _assert_equal("test_case_08_large_drop_then_rise", arr, expected)


def test_case_09_empty_array() -> bool:
    arr = []
    expected = None
    return _assert_equal("test_case_09_empty_array", arr, expected)


def test_case_10_all_zeroes() -> bool:
    arr = [0, 0, 0, 0]
    expected = 0
    return _assert_equal("test_case_10_all_zeroes", arr, expected)


# =========================================================
# Driver Function
# =========================================================
def run_all_tests() -> None:
    tests = [
        test_case_01_classic_example,
        test_case_02_all_positive,
        test_case_03_all_negative,
        test_case_04_single_element,
        test_case_05_single_negative_element,
        test_case_06_mixed_small,
        test_case_07_zeroes_present,
        test_case_08_large_drop_then_rise,
        test_case_09_empty_array,
        test_case_10_all_zeroes,
    ]

    passed = 0
    for test in tests:
        if test():
            passed += 1

    total = len(tests)
    print(f"\nSummary: {passed}/{total} tests passed.")
    if passed != total:
        print("Implement max_subarray_sum(arr) to make all tests pass.")


if __name__ == "__main__":
    run_all_tests()
