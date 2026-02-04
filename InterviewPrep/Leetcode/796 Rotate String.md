Below are **Master LeetCode Notes** for **LeetCode 796 — Rotate String (Easy)**.
They follow a **high–yield, interview-oriented, structured** format ideal for fast revision and deep understanding.

---

# **🔥 LeetCode 796 — Rotate String (Master Notes)**

**Difficulty:** Easy
**Topics:** String, Simulation
**Pattern:** *Rotation via Concatenation*

---

# **1. 🚀 Problem Summary**

You are given two strings **s** and **goal**.
You can perform *shifts* on **s**, where one shift moves the **first character to the end**.

Return **true** if and only if **s can become goal** after some number of shifts.

### Examples

| s         | goal      | Output  | Explanation                       |
| --------- | --------- | ------- | --------------------------------- |
| `"abcde"` | `"cdeab"` | `true`  | `"abcde"` → `"bcdea"` → `"cdeab"` |
| `"abcde"` | `"abced"` | `false` | Not achievable via rotation       |

---

# **2. 💡 Key Insight**

String rotation can be checked without simulation.

### **🎯 Trick: A rotated string must be a substring of `s + s`.**

Because any rotation of `s` will appear inside the doubled string.

Example:
`s = "abcde"`
`s + s = "abcdeabcde"` contains:
`bcdea`, `cdeab`, `deabc`, `eabcd`, etc.

So:

```
return goal in (s + s)
```

But only after verifying both strings have equal length.

---

# **3. ✅ Algorithm**

1. If lengths differ → `false`
2. Otherwise check:

   ```
   goal is a substring of s + s
   ```

---

# **4. ⏱ Complexity**

| Operation                   | Time         | Space                              |
| --------------------------- | ------------ | ---------------------------------- |
| Substring search in `s + s` | O(n) average | O(1) or O(n) depending on language |

---

# **5. ✔️ Optimal Code (Python)**

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Lengths must match
        if len(s) != len(goal):
            return False
        
        # goal must be a substring of s doubled
        return goal in (s + s)
```

---

# **6. 🧠 Why This Works (Interview Explanation)**

If you imagine rotating `s`, every possible rotation is represented linearly somewhere in `s + s`.

Example: `"abc"`
Double: `"abcabc"`
Possible rotations: `"abc"`, `"bca"`, `"cab"` — all appear inside `"abcabc"`.

Thus, checking rotation becomes a **substring check**, avoiding actual repeated rotations.

---

# **7. 🔍 Edge Cases**

| Case              | Example            | Output  | Reason                                  |
| ----------------- | ------------------ | ------- | --------------------------------------- |
| Same string       | `"aaa"`, `"aaa"`   | `true`  | Rotating identical letters does nothing |
| Different lengths | `"ab"`, `"a"`      | `false` | Impossible                              |
| Single char       | `"a"`, `"a"`       | `true`  | Valid rotation                          |
| Non-rotatable     | `"abcd"`, `"acbd"` | `false` | Wrong order                             |

---

# **8. 🏢 Companies Asking This**

(Without violating any premium lock info; known from public interview reports)

* Amazon
* Google
* Microsoft
* Facebook / Meta
* Apple
* Bloomberg
* Adobe

This is a common **screening question** because it tests:

* String intuition
* Ability to spot conciseness
* Avoiding brute-force rotation loops

---

# **9. 🧩 Common Pitfalls**

❌ Trying to rotate the string manually in a loop → O(n²)
❌ Forgetting to check equal lengths
❌ Missing that identical strings are always valid rotations

---

# **10. ⭐ Extra: Brute Force Version (for understanding)**

```python
def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    for _ in range(len(s)):
        s = s[1:] + s[0]  # rotate left
        if s == goal:
            return True
    return False
```

Not used in practice, but helps illustrate the concept.

---

If you'd like, I can generate:
✅ A flashcard version
✅ Pattern summary for rotation-related questions
✅ C++ / Java / JavaScript solutions
✅ More practice problems that use the same trick

Would you like those?
