Here are **Master LeetCode Notes** for **Problem 26: Remove Duplicates from Sorted Array** — optimized for interviews, pattern recognition, edge-case mastery, and clean intuition.

---

# 🚀 **LeetCode 26 — Remove Duplicates From Sorted Array (Master Notes)**

**Category:** Two Pointers
**Difficulty:** Easy
**Key Pattern:** Fast & Slow Pointer (a.k.a Write Pointer / Read Pointer)

---

# ✅ **1. Core Idea**

Since the array is **sorted in non-decreasing order**, duplicates always appear *next to each other*.
We want to **compress the array in-place** so that the first `k` elements contain unique values.

We use:

* **slow pointer (`i`)** → position to write the next unique element
* **fast pointer (`j`)** → scans through array reading elements

Whenever `nums[j] != nums[i]`, we found a **new unique element**, so:

```
i++
nums[i] = nums[j]
```

At the end, the number of unique elements is:

```
k = i + 1
```

---

# 🧠 **2. Why Two Pointers Works**

* Sorted = duplicates are consecutive
* Slow pointer tracks the **final compacted array**
* Fast pointer does the scanning
* Everything is done **in-place**, O(1) extra memory

This is one of the best examples of classic two-pointer array compression.

---

# ✨ **3. Algorithm**

```
Initialize i = 0
Loop j from 1 to n-1:
    If nums[j] != nums[i]:
        i++
        nums[i] = nums[j]
Return i + 1
```

---

# 📦 **4. Example Walkthrough**

### Example:

`nums = [0,0,1,1,1,2,2,3,3,4]`

| j | nums[j] | nums[i] | Action                      | Result Array      |
| - | ------- | ------- | --------------------------- | ----------------- |
| 1 | 0       | 0       | skip                        | same              |
| 2 | 1       | 0       | new unique → i=1, nums[1]=1 | `[0,1,...]`       |
| 3 | 1       | 1       | skip                        | same              |
| 5 | 2       | 1       | new unique → i=2, nums[2]=2 | `[0,1,2,...]`     |
| 7 | 3       | 2       | new unique → i=3            | `[0,1,2,3,...]`   |
| 9 | 4       | 3       | new unique → i=4            | `[0,1,2,3,4,...]` |

Return `k = 5`.

---

# 🧩 **5. Final Code (Clean Interview Version)**

### **Python**

```python
def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
```

### **Java**

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}
```

---

# ⚙️ **6. Time & Space Complexity**

| Complexity | Value              |
| ---------- | ------------------ |
| **Time**   | O(n) — single pass |
| **Space**  | O(1) — in-place    |

---

# 🎯 **7. Edge Cases**

| Input          | Result      |
| -------------- | ----------- |
| `[]`           | return `0`  |
| `[1]`          | return `1`  |
| All unique     | returns `n` |
| All duplicates | returns `1` |

---

# 🏆 **8. Common Interview Mistakes**

❌ Trying to delete elements → shifting costs O(n²).
❌ Using a Set → violates in-place requirement.
❌ Returning wrong index (`i` instead of `i + 1`).
❌ Overwriting incorrectly by advancing slow pointer too early.

---

# 🔑 **9. Pattern Recognition**

This problem teaches the **Two Pointers: Overwrite / Filter Pattern**, used in:

* LeetCode 27: Remove Element
* LeetCode 80: Remove Duplicates II
* LeetCode 283: Move Zeroes
* LeetCode 977: Squares of Sorted Array (different flavor)

If you master this base problem, harder ones become intuitive.

---

# 🧠 **10. Interviewer-Ready Summary (Say This Out Loud)**

> “Since the array is sorted, duplicates must be consecutive. I use two pointers: one pointer tracks the position to write the next unique value, and the other scans the array. Whenever I find a new value, I write it forward. This gives O(n) time and O(1) space in-place.”

