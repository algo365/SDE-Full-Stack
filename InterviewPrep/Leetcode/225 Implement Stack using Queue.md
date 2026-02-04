Here are **Master LeetCode Notes** for **225. Implement Stack Using Queues** — optimized for interview readiness, clarity, and memorization.

---

# 🚀 **LeetCode 225 — Implement Stack Using Queues (Master Notes)**

**Difficulty:** Easy
**Pattern:** Queue Simulation, Data Structure Design
**Core Idea:** Use queue operations to simulate LIFO behavior.

---

# 📌 **1. Problem Summary**

You must implement a **stack (LIFO)** using only **queues**, which allow:

* enqueue at back
* dequeue from front
* peek front
* size
* isEmpty

Required stack operations:

* `push(x)`
* `pop()`
* `top()`
* `empty()`

---

# 🧠 **2. Key Insight**

A queue is **FIFO**, but a stack is **LIFO**.
To simulate a stack, we must ensure the **most recently pushed element appears at front**.

There are **two classic solutions**:

---

# ✅ **3. Solution A (Most Common): Using ONE Queue (Efficient & Elegant)**

### 👉 Idea

When pushing a new element, rotate the queue so that the new element becomes the **first element**, mimicking a stack top.

### Steps

`push(x)`:

1. Enqueue `x`
2. Rotate the queue (size−1 times), moving old elements behind `x`

`pop()`:

* Dequeue front element.

`top()`:

* Peek front element.

`empty()`:

* `queue.isEmpty()`

### ⏱️ Time Complexity

| Operation | Time |
| --------- | ---- |
| push      | O(n) |
| pop       | O(1) |
| top       | O(1) |
| empty     | O(1) |

### ⭐ Why This Works

The queue is always kept in "stack order," with the most recent element at the front.

---

## ✔️ **One-Queue Implementation (Java-like pseudocode)**

```java
class MyStack {
    Queue<Integer> q = new LinkedList<>();

    public void push(int x) {
        q.offer(x);
        int size = q.size();
        // Rotate previous elements behind x
        while (size-- > 1)
            q.offer(q.poll());
    }

    public int pop() {
        return q.poll();
    }

    public int top() {
        return q.peek();
    }

    public boolean empty() {
        return q.isEmpty();
    }
}
```

---

# ✅ **4. Solution B: Using TWO Queues (More Intuitive)**

### 👉 Idea

Use `q2` as temporary holding when pushing new element.

Steps for `push(x)`:

1. Enqueue `x` into q2
2. Move all elements from q1 → q2
3. Swap q1 and q2
   => Ensures `x` is always the front element

### ⏱️ Time Complexity

Same as solution A.

### Two-queue version:

```java
class MyStack {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();

    public void push(int x) {
        q2.offer(x);
        while (!q1.isEmpty()) {
            q2.offer(q1.poll());
        }
        // Swap
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }

    public int pop() {
        return q1.poll();
    }

    public int top() {
        return q1.peek();
    }

    public boolean empty() {
        return q1.isEmpty();
    }
}
```

---

# 📝 **5. Which Approach Should You Use?**

| Approach               | Pros                                        | Cons               |
| ---------------------- | ------------------------------------------- | ------------------ |
| **One Queue (rotate)** | Short, elegant, commonly seen in interviews | Push is O(n)       |
| **Two Queues**         | Clear logic, easy to explain                | Slightly more code |

Both are valid for LeetCode and interviews.

---

# 🎤 **6. Interview Talking Points**

If asked *"How do you simulate a stack using queues?"*, say:

> "I maintain the queue so that the newest element is always at the front.
> For every push, I rotate all older elements behind the new one.
> That allows pop and top to be O(1), matching stack behavior."

If asked *"Why is push O(n)?"*:

> "Because each push requires reordering all existing elements to maintain LIFO ordering."

If asked *"Can we make push O(1) instead?"*:

> "Yes, but pop would become O(n) instead. One operation must cost O(n) because queues are FIFO."

---

# 🧩 **7. Edge Cases**

* Multiple pushes
* Stack with 1 element
* Popping until empty
* Validity guaranteed → no need for error checks

---

# 🏁 **8. Final Takeaways**

* This problem demonstrates **data structure transformation**
* Understand *queue rotation*
* One queue solution is most elegant
* Two queue solution is most intuitive
