Below is the **full Tech Interview Questions – Master Notes** for the problem *Reverse a String In-Place*.
All content is in clean **Markdown** exactly as requested.

---

# 🧵 Reverse a String (In-Place)

**Problem Statement:**
Given an array of characters `s`, reverse the array **in-place**.
You must do it with **O(1) extra space**.

Example:
Input: `['h','e','l','l','o']` → Output: `['o','l','l','e','h']`

---

# 👥 Roleplay: Interviewer ↔ Candidate

**Candidate:**
“Can I assume the input is mutable (i.e., a list/array, not an immutable string)?”

**Interviewer:**
“Yes. You receive a *character array*, and you must mutate it directly.”

---

**Candidate:**
“Is the input always ASCII? Or can it include Unicode combining characters?”

**Interviewer:**
“For interview purposes, treat each element as a single character in the array.”

---

**Candidate (thinking aloud):**
“Since the reversal is in-place with O(1) extra memory, I should avoid creating new arrays. The natural approach is using two pointers: swap front/back until they meet.”

---

# 🏷️ Important Keywords & Why They Matter

| Keyword               | Why it Matters                                                  |
| --------------------- | --------------------------------------------------------------- |
| **Two Pointers**      | Classic for in-place symmetric operations.                      |
| **In-Place Mutation** | Forces O(1) extra space; cannot allocate new arrays.            |
| **Swap Operation**    | Core mechanical step in reversing an array.                     |
| **Stack LIFO**        | Naturally reverses order; useful conceptual variant.            |
| **Queue FIFO**        | Helps compare directional operations.                           |
| **Deque**             | Provides O(1) front/back operations; shows structural symmetry. |

---

# 🧠 Human (Mechanical) Approach → Brute Force

A human reversing a word on paper would:

1. Look at the first and last letter.
2. Swap them.
3. Move inward.
4. Repeat until reaching the middle.

This is equivalent to using **two pointers**, but we classify this here as brute force because it is the most direct, mechanical method.

### Brute Force Logic

* Initialize `left = 0`, `right = len(s) - 1`.
* While `left < right`, swap `s[left]` with `s[right]`.
* Move both pointers inward.

### Pseudocode

```
left ← 0
right ← n - 1

while left < right:
    swap s[left], s[right]
    left ← left + 1
    right ← right - 1
```

---

# 🪓 Brute Force Implementations

### Python

```python
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]  # swap
        left += 1
        right -= 1
```

### Java

```java
public void reverseString(char[] s) {
    int left = 0;
    int right = s.length - 1;

    while (left < right) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }
}
```

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

# 🧭 Mapping Brute Force → CS Concepts

Brute force here is not inefficient—it's optimal.
But it teaches:

* **Symmetry exploitation:** Left/right pointer invariants.
* **Redundant work avoidance:** No unnecessary traversals or memory allocations.
* **Transformation of array structure:** In-place mutations vs. creating new arrays.

---

# ⚙️ Optimizations (5–8 Distinct Approaches)

Even though reversing is simple, we explore multiple variants to build interview mastery.

---

## 1️⃣ Two-Pointers (Optimal & Standard)

**Core Idea:**
Swap elements from both ends moving inward.

**Why Better:**
O(n) time, O(1) space — meets problem constraints directly.

**When It Works:**
Any mutable array-like structure.

**Pseudocode:** *(same as brute force)*

### Python

```python
def reverse_string_two_pointers(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

### Java

```java
public void reverseStringTwoPointers(char[] s) {
    int l = 0, r = s.length - 1;
    while (l < r) {
        char temp = s[l];
        s[l] = s[r];
        s[r] = temp;
        l++;
        r--;
    }
}
```

**Time:** O(n)
**Space:** O(1)
**Rationale:** Two-pointers eliminate unnecessary passes and memory.

---

## 2️⃣ Stack-Based Reversal (LIFO Structure)

**Core Idea:**
Push all characters onto a stack; pop back in reverse order.

**Why Better?**
Not better for constraints—uses extra memory—but shows conceptual reversing.

**When It Works:**
When extra memory is allowed or teaching stack behavior.

**Pseudocode:**

```
stack ← empty
for c in s:
    push(c)

for i from 0 to n-1:
    s[i] ← pop()
```

### Python

```python
def reverse_string_stack(s):
    stack = list(s)
    for i in range(len(s)):
        s[i] = stack.pop()
```

### Java

```java
public void reverseStringStack(char[] s) {
    java.util.Stack<Character> st = new java.util.Stack<>();
    for (char c : s) st.push(c);
    for (int i = 0; i < s.length; i++) s[i] = st.pop();
}
```

**Time:** O(n)
**Space:** O(n)
**Rationale:** Illustrates stack LIFO semantics.

---

## 3️⃣ Queue Method (Double Reversal Insight)

**Core Idea:**
Enqueue elements → Dequeue them while overwriting array.

**Why It's Interesting:**
Demonstrates FIFO vs. LIFO behavior.

### Pseudocode

```
queue ← empty
for c in s:
    enqueue(c)

for i from 0..n-1:
    s[n - 1 - i] ← dequeue()
```

### Python

```python
from collections import deque

def reverse_string_queue(s):
    q = deque(s)
    for i in range(len(s)):
        s[len(s) - 1 - i] = q.popleft()
```

### Java

```java
public void reverseStringQueue(char[] s) {
    java.util.Queue<Character> q = new java.util.LinkedList<>();
    for (char c : s) q.offer(c);
    for (int i = s.length - 1; i >= 0; i--) {
        s[i] = q.poll();
    }
}
```

**Time:** O(n)
**Space:** O(n)
**Rationale:** Demonstrates queue FIFO impact.

---

## 4️⃣ Deque Double-Ended Approach

**Core Idea:**
Use a deque to access front/back efficiently.

### Pseudocode

```
dq ← deque(s)
i ← 0
while dq not empty:
    s[i] ← dq.removeLast()
    i ← i + 1
```

### Python

```python
from collections import deque

def reverse_string_deque(s):
    dq = deque(s)
    i = 0
    while dq:
        s[i] = dq.pop()
        i += 1
```

### Java

```java
public void reverseStringDeque(char[] s) {
    java.util.Deque<Character> dq = new java.util.ArrayDeque<>();
    for (char c : s) dq.addLast(c);
    int i = 0;
    while (!dq.isEmpty()) {
        s[i++] = dq.removeLast();
    }
}
```

**Time:** O(n)
**Space:** O(n)

---

## 5️⃣ Recursion (Implicit Stack)

**Core Idea:**
Swap outer characters, recurse on substring.

**Why It’s Interesting:**
Teaches recursion and call stack behavior.

**Limits:**
Deep recursion risks stack overflow for very long arrays.

### Pseudocode

```
function helper(l, r):
    if l >= r: return
    swap s[l], s[r]
    helper(l+1, r-1)
```

### Python

```python
def reverse_string_recursive(s):

    def helper(l, r):
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        helper(l + 1, r - 1)

    helper(0, len(s) - 1)
```

### Java

```java
public void reverseStringRecursive(char[] s) {
    helper(s, 0, s.length - 1);
}

private void helper(char[] s, int l, int r) {
    if (l >= r) return;
    char temp = s[l];
    s[l] = s[r];
    s[r] = temp;
    helper(s, l + 1, r - 1);
}
```

**Time:** O(n)
**Space:** O(n) implicit stack.

---

## 6️⃣ XOR Swap Variant (Swap Without Temp Variable)

**Core Idea:**
Use XOR to swap two characters.

**Why It’s Interesting:**
Teaches memory-bitwise tricks.

**Caution:**
Avoid when characters might map to same memory location (l == r).

### Python

```python
def reverse_string_xor(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l] = chr(ord(s[l]) ^ ord(s[r]))
        s[r] = chr(ord(s[l]) ^ ord(s[r]))
        s[l] = chr(ord(s[l]) ^ ord(s[r]))
        l += 1
        r -= 1
```

### Java

```java
public void reverseStringXor(char[] s) {
    int l = 0, r = s.length - 1;
    while (l < r) {
        s[l] ^= s[r];
        s[r] ^= s[l];
        s[l] ^= s[r];
        l++; r--;
    }
}
```

**Time:** O(n)
**Space:** O(1)

---

## 7️⃣ In-Place Half Rotation Insight

**Core Idea:**
Reverse is conceptual rotation: swap symmetric pairs.

**Why It's Interesting:**
Relates reversing to array-rotation algorithms.

(Pseudocode identical to two pointers.)

---

# 🚫 Common Wrong / Naïve Algorithms

### ❌ Wrong Approach #1: Building a New Array (Violates Constraints)

**Plausible:**
Just make a reversed copy: `s = s[::-1]`.

**Counterexample:**
Input: `['a','b','c']`
Creates new array → violates “modify in-place with O(1) memory.”

---

### ❌ Wrong Approach #2: Sorting the Array

**Plausible:**
Sorting rearranges elements, right?

**Failure Example:**
`['c','a','b']` → Sort gives `['a','b','c']`, not reversed.

---

# 🧪 Edge Case Checklist

* ✔️ Empty array `[]` → return unchanged
* ✔️ One element `['a']` → unchanged
* ✔️ Even-length arrays
* ✔️ Odd-length arrays
* ✔️ Unicode characters (assume each entry is atomic)
* ✔️ Repetitive characters `['a','a','a']`
* ✔️ Very large arrays (recursion may fail)

---

# ⏱️ Complexity Summary

| Approach     | Idea                | Time | Space | Notes                     |
| ------------ | ------------------- | ---- | ----- | ------------------------- |
| Two Pointers | Swap ends inward    | O(n) | O(1)  | Optimal                   |
| Stack        | LIFO reversal       | O(n) | O(n)  | Conceptual                |
| Queue        | FIFO reversed       | O(n) | O(n)  | Educational               |
| Deque        | Pop from end        | O(n) | O(n)  | Structural symmetry       |
| Recursion    | Call stack reversal | O(n) | O(n)  | Elegant but stack-heavy   |
| XOR Swap     | Bitwise swap        | O(n) | O(1)  | Rarely used in production |

---

# 🧰 Why Optimization Works

* **Two Pointers:** Constant-space symmetric traversal avoids extra memory.
* **Stacks:** Reverse order emerges naturally from LIFO.
* **Queues:** FIFO makes you reconstruct in reverse index order.
* **Recursion:** Each recursive layer handles outer pair — essentially same as two pointers but with call stack.
* **XOR:** Removes temp variable, but not usually beneficial.

---

# 🧑‍💻 Final "Ready-to-Use" Functions (Recommended Solution)

## Python (with type hints)

```python
from typing import List

def reverse_string(s: List[str]) -> None:
    """
    Reverse the character array in-place using O(1) extra space.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

## Java (clean, function-only)

```java
public void reverseString(final char[] s) {
    int left = 0;
    int right = s.length - 1;

    while (left < right) {
        final char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }
}
```

---

# 📌 Quick Practice Plan

1. **Test tiny cases:**

   * `[]`
   * `['a']`
   * `['a','b']`
2. **Test typical cases:**

   * `['h','e','l','l','o']`
3. **Test Unicode:**
   `['你','好','啊']`
4. **Test random arrays and compare with Python `list(reversed(s))`** for correctness.
5. **Implement all approaches** and verify they match outputs.

