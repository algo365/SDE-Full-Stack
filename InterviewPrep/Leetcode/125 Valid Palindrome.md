# 📝 **LeetCode Notes — Problem 125: Valid Palindrome**

*(Using the “leetcode notes” Master Template)*

---

# 1. **Title Section**

## **Valid Palindrome (LeetCode 125)**

**Problem Statement:**
Given a string `s`, determine if it is a **palindrome**, considering **only alphanumeric characters** and ignoring **case**.
A palindrome reads the same forwards and backwards.

**Constraints:**

* `1 ≤ len(s) ≤ 2 * 10^5`
* Characters may include spaces, punctuation, Unicode symbols.

**Examples**

* `"A man, a plan, a canal: Panama"` → `true`
* `"race a car"` → `false`
* `" "` → `true`

---

# 2. 👥 **Roleplay: Interviewer ↔ Candidate**

### **Candidate asking clarifying questions**

**Q1:** Should I ignore all characters that are *not* letters or digits?
**Interviewer:** Yes.

**Q2:** Should uppercase and lowercase be treated the same?
**Interviewer:** Yes, convert everything to lowercase.

**Q3:** Is an empty processed string considered a palindrome?
**Interviewer:** Yes, it's valid.

**Q4:** Do we need to preserve the original positions of characters?
**Interviewer:** No, just use the cleaned version.

---

### **Candidate (thinking aloud)**

* First, filter to alphanumeric and lowercase.
* Then compare left/right characters using a **two-pointer** strategy.
* Several alternatives exist: reverse-string comparison, regex filtering, ASCII checks, stack-based attempts (for teaching), etc.

---

# 3. 🏷️ **Important Keywords & Why They Matter**

| Keyword                    | Why It Matters                                                      |
| -------------------------- | ------------------------------------------------------------------- |
| **Two pointers**           | Natural for checking symmetry efficiently in O(n).                  |
| **Alphanumeric filtering** | Core requirement; ensures irrelevant characters don’t break logic.  |
| **Case folding**           | Must standardize case to compare correctly.                         |
| **String reverse**         | Simple approach for verifying palindrome, though duplicates memory. |
| **Stack**                  | Useful for educational contrast (LIFO symmetry).                    |
| **Regex**                  | Makes filtering concise in some languages.                          |

---

# 4. 🧠 **Human (Mechanical) Approach → Brute Force**

### **Human logic:**

1. Remove all non-alphanumeric characters.
2. Convert remaining characters to lowercase.
3. Compare the cleaned string with its reverse.

### **Brute Force Pseudocode**

```
clean = ""
for char in s:
    if char is alphanumeric:
        clean += lowercase(char)

return clean == reverse(clean)
```

---

# 5. 🪓 **Brute Force Implementations**

### **Python**

```python
def is_palindrome_bruteforce(s: str) -> bool:
    clean = []
    for ch in s:
        if ch.isalnum():
            clean.append(ch.lower())
    cleaned = "".join(clean)
    return cleaned == cleaned[::-1]
```

### **Java**

```java
public static boolean isPalindromeBruteforce(final String s) {
    StringBuilder clean = new StringBuilder();
    for (char ch : s.toCharArray()) {
        if (Character.isLetterOrDigit(ch)) {
            clean.append(Character.toLowerCase(ch));
        }
    }
    String cleaned = clean.toString();
    return cleaned.equals(new StringBuilder(cleaned).reverse().toString());
}
```

**Time Complexity:** O(n)
**Space Complexity:** O(n) for cleaned string

---

# 6. 🧭 **Mapping Brute Force → CS Concepts**

Brute force here = **construct full transformed string**, then do **reverse comparison**.

Signals that improvement is possible:

* Creating a new string costs O(n) extra memory.
* Reverse operation duplicates memory.
* We can avoid storing all characters by checking *in-place* with two pointers.

---

# 7. ⚙️ **Optimizations (8 Approaches)**

---

## **Approach A: Two Pointers (Optimal, Most Common)**

### **Core Idea**

Use pointers at left & right ends and move inward, skipping non-alphanumeric characters.

### **Why It's Better**

* Avoids building a second string.
* Uses O(1) extra space.

### **When It Works**

Always; string scanning does not modify original input.

---

### **Pseudocode**

```
l = 0
r = len(s) - 1
while l < r:
    while l < r and not s[l] is alphanumeric: l++
    while l < r and not s[r] is alphanumeric: r--
    if lowercase(s[l]) != lowercase(s[r]):
        return false
    l++, r--
return true
```

---

### **Python**

```python
def is_palindrome_two_pointers(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True
```

### **Java**

```java
public static boolean isPalindromeTwoPointers(final String s) {
    int l = 0, r = s.length() - 1;

    while (l < r) {
        while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
        while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;

        char left = Character.toLowerCase(s.charAt(l));
        char right = Character.toLowerCase(s.charAt(r));

        if (left != right) return false;

        l++; 
        r--;
    }
    return true;
}
```

### **Complexity:** O(n) time, O(1) space

### **Rationale:** Two-pointer symmetry check is optimal for palindrome problems.

---

## **Approach B: Build Filtered + Two Pointers**

### Idea

Filter and lowercase everything first, then run a two-pointer check.
Useful for clarity and debugging.

### Python / Java: same as brute force but without reverse comparison.

**Complexity:** O(n) time, O(n) space
**Rationale:** Simple but not optimal memory-wise.

---

## **Approach C: Filter + Reverse Compare**

### Idea

Construct cleaned string, compare with reversed version.

**Python**

```python
def is_palindrome_reverse(s: str) -> bool:
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]
```

**Java**
Similar to brute-force version.

**Complexity:** O(n) time, O(n) space
**Rationale:** Cleanest code but more memory.

---

## **Approach D: Regular Expression (Python / Java Pattern)**

### Idea

Use regex to strip non-alphanumeric characters.

**Python**

```python
import re

def is_palindrome_regex(s: str) -> bool:
    filtered = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return filtered == filtered[::-1]
```

**Java**
Uses `Pattern` & `Matcher`.

**Complexity:** O(n) time, O(n) space
**Rationale:** Very concise but less performant.

---

## **Approach E: Stack + Queue Symmetry Check**

### Idea

Push filtered chars onto a stack and a queue.
Pop and dequeue to compare symmetry.

**Python**

```python
from collections import deque

def is_palindrome_stack_queue(s: str) -> bool:
    stack, queue = [], deque()
    for ch in s:
        if ch.isalnum():
            ch = ch.lower()
            stack.append(ch)
            queue.append(ch)

    while stack:
        if stack.pop() != queue.popleft():
            return False
    return True
```

**Complexity:** O(n), uses O(n) space
**Rationale:** Educational DS-based approach.

---

## **Approach F: Generator-based Streaming Check (Python)**

### Idea

Use a generator to stream characters, reducing intermediate storage.

**Python**

```python
def is_palindrome_streaming(s: str) -> bool:
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return all(filtered[i] == filtered[~i] for i in range(len(filtered)//2))
```

**Complexity:** O(n) time, O(n) space
**Rationale:** Clean, Pythonic, avoids explicit reverse.

---

## **Approach G: Unicode-aware Alphanumeric Check**

### Idea

Some interviews allow Unicode alphanumeric. Use `char.isalnum()` or `Character.isLetterOrDigit`.

**Same logic as Approach A**, but emphasizing Unicode correctness.

---

## **Approach H: Deque Two-Pointer Simulation**

### Idea

Append cleaned characters to a deque, then pop from left/right.

**Python**

```python
from collections import deque

def is_palindrome_deque(s: str) -> bool:
    dq = deque(ch.lower() for ch in s if ch.isalnum())
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
```

**Complexity:** O(n) time, O(n) space
**Rationale:** Symmetric operations without index arithmetic.

---

# 8. 🚫 **Common Wrong/Naïve Algorithms**

### ❌ **Wrong Approach A: Only Compare First and Last Non-Symbol Characters**

Seems plausible because palindrome symmetry starts at ends.

**Counterexample:**
`"ab@#a"` → valid
`"ab@#c"` → fails only at middle; naive stop-too-soon fails.

---

### ❌ **Wrong Approach B: Treat Non-Alphanumeric as 'ignore but keep position'**

Some mistakenly move pointers blindly.

**Counterexample:**
`s = "A,bc!!B,a"`
Filtered = `"abcba"`
If pointer skipping doesn’t check correctly, mismatch occurs.

---

# 9. 🧪 **Edge Case Checklist**

* ✔️ Empty string → palindrome
* ✔️ Single character → palindrome
* ✔️ Only symbols (`"!!!"`) → becomes empty → palindrome
* ✔️ Mixed case (`"AbBa"`) → valid
* ✔️ Numeric sequences (`"1221"`) → valid
* ✔️ Unicode letters/digits → depends on language; `.isalnum()` handles correctly in Python
* ✔️ Very long strings (up to 200k) → must be O(n)

---

# 10. ⏱️ **Complexity Summary**

| Approach                | Time     | Space    | Notes                  |
| ----------------------- | -------- | -------- | ---------------------- |
| Two Pointers (Optimal)  | **O(n)** | **O(1)** | Best overall           |
| Build + Reverse Compare | O(n)     | O(n)     | Clean but memory-heavy |
| Regex Clean             | O(n)     | O(n)     | Short code             |
| Stack + Queue           | O(n)     | O(n)     | Educational            |
| Streaming Check         | O(n)     | O(n)     | Pythonic               |
| Deque                   | O(n)     | O(n)     | Symmetric DS           |
| Unicode-aware           | O(n)     | O(1)     | Same as two pointers   |

---

# 11. 🧰 **Why Optimization Works**

* **Two-pointers** avoid building new strings → O(1) memory.
* Skipping non-alphanumeric characters reduces unnecessary comparisons.
* Reverse comparison requires a full copy → avoid if space-sensitive.
* Streams & generator checks illustrate functional approaches but still linear.

---

# 12. 🧑‍💻 **Final “Ready-to-Use” Functions**

## ⭐ **Recommended Python Solution**

```python
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True
```

## ⭐ **Recommended Java Solution**

```java
public static boolean isPalindrome(final String s) {
    int l = 0, r = s.length() - 1;

    while (l < r) {
        while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
        while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;

        char left = Character.toLowerCase(s.charAt(l));
        char right = Character.toLowerCase(s.charAt(r));
        if (left != right) return false;

        l++;
        r--;
    }
    return true;
}
```

---

# 13. 📌 **Quick Practice Plan**

### **Minimal test set**

```
"A man, a plan, a canal: Panama" → true
"race a car" → false
" " → true
"ab@a" → true
"0P" → false
```

### **Self-made tests**

* Random alphanumeric strings; compare against brute force version.
* Test long strings of size 1e5 to confirm performance.

### **Useful exercises**

* Implement both optimal and brute force to see performance difference.
* Modify the problem to treat Unicode combining characters properly.

