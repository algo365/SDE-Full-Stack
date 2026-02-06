from typing import List


# =========================================================
# Candidate Stub (INTENTIONALLY WRONG / INCOMPLETE)
# ---------------------------------------------------------
# Candidate: implement the correct logic here.
# For now, it returns -1 so ALL tests will FAIL.
# =========================================================
def max_profit_one_transaction(prices: List[int]) -> int:
    """
    Return the maximum profit possible with at most ONE buy and ONE sell.
    - You must buy before you sell.
    - If no profit is possible, return 0.
    """
    min_price = prices[0]
    max_profit = 0 
    length = len(prices)
    
    for index in range(1, length):
        if prices[index] < min_price:
            min_price = prices[index]
            continue

        current_profit = prices[index] - min_price
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit


# =========================================================
# Tiny Test Harness
# ---------------------------------------------------------
# Each test is one function.
# Driver calls all tests.
# On failure, prints: input, expected, got
# =========================================================
def _assert_equal(test_name: str, prices: List[int], expected: int) -> bool:
    got = max_profit_one_transaction(prices)
    if got != expected:
        print(f"[FAIL] {test_name}")
        print(f"  input    = {prices}")
        print(f"  expected = {expected}")
        print(f"  got      = {got}")
        print("-" * 60)
        return False
    print(f"[PASS] {test_name}")
    return True


def test_case_01_classic_mixed() -> bool:
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
    return _assert_equal("test_case_01_classic_mixed", prices, expected)


def test_case_02_always_decreasing() -> bool:
    prices = [7, 6, 4, 3, 1]
    expected = 0
    return _assert_equal("test_case_02_always_decreasing", prices, expected)


def test_case_03_always_increasing() -> bool:
    prices = [1, 2, 3, 4, 5]
    expected = 4
    return _assert_equal("test_case_03_always_increasing", prices, expected)


def test_case_04_big_dip_then_rise() -> bool:
    prices = [10, 8, 2, 5, 7, 1, 9]
    expected = 8
    return _assert_equal("test_case_04_big_dip_then_rise", prices, expected)


def test_case_05_all_equal() -> bool:
    prices = [5, 5, 5, 5, 5]
    expected = 0
    return _assert_equal("test_case_05_all_equal", prices, expected)


def test_case_06_early_peak_later_bigger_peak() -> bool:
    prices = [3, 8, 2, 5, 1, 7, 9]
    expected = 8
    return _assert_equal("test_case_06_early_peak_later_bigger_peak", prices, expected)


def test_case_07_profit_only_if_wait() -> bool:
    prices = [9, 7, 4, 1, 6]
    expected = 5
    return _assert_equal("test_case_07_profit_only_if_wait", prices, expected)


def test_case_08_two_elements() -> bool:
    prices = [2, 1]
    expected = 0
    return _assert_equal("test_case_08_two_elements", prices, expected)


def test_case_09_single_element() -> bool:
    prices = [5]
    expected = 0
    return _assert_equal("test_case_09_single_element", prices, expected)


def test_case_10_volatile_large_values() -> bool:
    prices = [100, 180, 260, 310, 40, 535, 695]
    expected = 655
    return _assert_equal("test_case_10_volatile_large_values", prices, expected)


def run_all_tests() -> None:
    tests = [
        test_case_01_classic_mixed,
        test_case_02_always_decreasing,
        test_case_03_always_increasing,
        test_case_04_big_dip_then_rise,
        test_case_05_all_equal,
        test_case_06_early_peak_later_bigger_peak,
        test_case_07_profit_only_if_wait,
        test_case_08_two_elements,
        test_case_09_single_element,
        test_case_10_volatile_large_values,
    ]

    passed = 0
    for t in tests:
        if t():
            passed += 1

    total = len(tests)
    print(f"\nSummary: {passed}/{total} tests passed.")
    if passed != total:
        print("Implement max_profit_one_transaction(prices) to make all tests pass.")


if __name__ == "__main__":
    run_all_tests()
