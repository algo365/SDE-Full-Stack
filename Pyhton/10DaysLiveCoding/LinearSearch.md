Here is the comprehensive documentation for the **Linear Search** algorithm, designed for a GitHub repository.

# Linear Search Implementation in Multiple Languages

Linear Search is the simplest searching algorithm. It works by starting from the very first element of a data structure (like an array) and comparing it with the target value. If a match is found, the search is successful; otherwise, it continues until the end of the data is reached.

---

## 1. Logic Explained (Multilingual)

### **English**

1. **Initialization**: Start with a function that accepts an array `a`, its size `n`, and the `key` you want to find.
2. **Iteration**: Use a loop to traverse the array. Initialize a counter (index) at `0`.
3. **Boundary Condition**: Continue the loop as long as the index is less than `n`.
4. **Comparison**: In each step, access the element at the current index using `a[index]` and compare it with the `key` using the `==` operator.
5. **Match Found**: If they are equal, immediately return **True**.
6. **Termination**: If the loop finishes without a match, return **False**.

### **ಕನ್ನಡ (Kannada)**

1. **ಆರಂಭ**: ಅರೇ `a`, ಅದರ ಗಾತ್ರ `n`, ಮತ್ತು ಹುಡುಕಬೇಕಾದ ಸಂಖ್ಯೆ `key` ಅನ್ನು ಫಂಕ್ಷನ್‌ಗೆ ನೀಡಿ.
2. **ಪುನರಾವರ್ತನೆ (Loop)**: ಅರೇಯ ಪ್ರತಿಯೊಂದು ಎಲಿಮೆಂಟ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಲು ಒಂದು ಲೂಪ್ ಬಳಸಿ. ಇಂಡೆಕ್ಸ್ ಅನ್ನು `0` ರಿಂದ ಪ್ರಾರಂಭಿಸಿ.
3. **ಮಿತಿ**: ಇಂಡೆಕ್ಸ್ `n` ಗಿಂತ ಕಡಿಮೆ ಇರುವವರೆಗೆ ಲೂಪ್ ಮುಂದುವರಿಸಿ.
4. **ಹೋಲಿಕೆ**: ಪ್ರತಿ ಹಂತದಲ್ಲಿ `a[index]` ಅನ್ನು `key` ಜೊತೆಗೆ `==` ಬಳಸಿ ಹೋಲಿಸಿ.
5. **ದೊರೆತರೆ**: ಸಂಖ್ಯೆ ಸಿಕ್ಕಿದರೆ ತಕ್ಷಣ **True** ಎಂದು ರಿಟರ್ನ್ ಮಾಡಿ.
6. **ಸಿಗದಿದ್ದರೆ**: ಲೂಪ್ ಮುಗಿದರೂ ಸಂಖ್ಯೆ ಸಿಗದಿದ್ದರೆ **False** ಎಂದು ರಿಟರ್ನ್ ಮಾಡಿ.

### **हिन्दी (Hindi)**

1. **प्रारंभ**: एक फ़ंक्शन बनाएं जो ऐरे `a`, उसका आकार `n`, और `key` को इनपुट के रूप में ले।
2. **लूप**: ऐरे के हर तत्व पर जाने के लिए एक लूप का उपयोग करें। इंडेक्स को `0` से शुरू करें।
3. **शर्त**: जब तक इंडेक्स `n` से छोटा है, तब तक आगे बढ़ते रहें।
4. **तुलना**: हर बार `a[index]` की तुलना `key` से करें (जैसे `a[index] == key`)।
5. **परिणाम**: यदि वे बराबर हैं, तो **True** वापस करें। अन्यथा, अगले तत्व पर जाएं।
6. **अंत**: यदि पूरा ऐरे खोजने के बाद भी कुछ न मिले, तो **False** वापस करें।

### **தமிழ் (Tamil)**

1. **துவக்கம்**: ஒரு அணி (Array `a`), அதன் அளவு `n`, மற்றும் தேட வேண்டிய மதிப்பு `key` ஆகியவற்றை உள்ளீடாக வழங்கவும்.
2. **சுழற்சி (Loop)**: அணியின் ஒவ்வொரு உறுப்பையும் சரிபார்க்க ஒரு சுழற்சியைப் பயன்படுத்தவும். குறியீட்டை (Index) `0` இல் தொடங்கவும்.
3. **நிபந்தனை**: குறியீடு `n`-ஐ விடக் குறைவாக இருக்கும் வரை தேடலைத் தொடரவும்.
4. **ஒப்பிடுதல்**: ஒவ்வொரு முறையும் `a[index] == key` என்று ஒப்பிட்டுப் பார்க்கவும்.
5. **முடிவு**: மதிப்பு கிடைத்தால் **True** என அனுப்பவும். இல்லையெனில் அடுத்த உறுப்புக்குச் செல்லவும்.
6. **நிறைவு**: இறுதிவரை மதிப்பு கிடைக்கவில்லை என்றால் **False** என அனுப்பவும்.

### **తెలుగు (Telugu)**

1. **ప్రారంభం**: ఒక అర్రే `a`, దాని పరిమాణం `n`, మరియు వెతకాల్సిన `key`ని ఇన్‌పుట్‌గా తీసుకోండి.
2. **లూప్**: అర్రేలోని ప్రతి ఎలిమెంట్ ని చెక్ చేయడానికి ఒక లూప్ ఉపయోగించండి. ఇండెక్స్ ని `0` తో మొదలుపెట్టండి.
3. **పరిమితి**: ఇండెక్స్ `n` కంటే తక్కువ ఉన్నంత వరకు వెతకడం కొనసాగించండి.
4. **పోలిక**: ప్రతిసారి `a[index] == key` అని పోల్చి చూడండి.
5. **సమాధానం**: ఒకవేళ కీ దొరికితే **True** అని పంపండి.
6. **ముగింపు**: అర్రే మొత్తం వెతికినా దొరకకపోతే **False** అని పంపండి.

### **中文 (Chinese)**

1. **初始化**: 创建一个函数，接收数组 `a`、大小 `n` 和目标值 `key`。
2. **遍历**: 使用循环遍历数组。将索引（index）设为 `0`。
3. **边界条件**: 只要索引小于 `n`，就继续循环。
4. **比较**: 每一轮使用 `a[index] == key` 来比较当前元素与目标值。
5. **找到结果**: 如果相等，立即返回 **True**。
6. **结束**: 如果循环结束仍未找到，返回 **False**。

---

---

## 2. Code Implementations

### C++

```cpp
bool search(int a[], int n, int key) {
    for (int index = 0; index < n; index++) {
        if (a[index] == key) return true;
    }
    return false;
}

```

### Java

```java
public static boolean search(int[] a, int n, int key) {
    for (int index = 0; index < n; index++) {
        if (a[index] == key) return true;
    }
    return false;
}

```

### Python

```python
def search(a, n, key):
    for index in range(n):
        if a[index] == key:
            return True
    return False

```

### JavaScript

```javascript
function search(a, n, key) {
    for (let index = 0; index < n; index++) {
        if (a[index] === key) return true;
    }
    return false;
}

```

### Swift

```swift
func search(a: [Int], n: Int, key: Int) -> Bool {
    for index in 0..<n {
        if a[index] == key { return true }
    }
    return false
}

```

### C#

```csharp
public bool Search(int[] a, int n, int key) {
    for (int index = 0; index < n; index++) {
        if (a[index] == key) return true;
    }
    return false;
}

```

### Rust

```rust
fn search(a: &[i32], n: usize, key: i32) -> bool {
    for index in 0..n {
        if a[index] == key { return true; }
    }
    false
}

```

### Kotlin

```kotlin
fun search(a: IntArray, n: Int, key: Int): Boolean {
    for (index in 0 until n) {
        if (a[index] == key) return true
    }
    return false
}

```

### 8086 Assembly Language

```assembly
; Input: SI=Array Address, CX=n, AX=key
SEARCH_PROC:
    JCXZ NOT_FOUND   ; If size is 0, exit
L1:
    CMP AX, [SI]     ; Compare key with current element
    JE FOUND         ; Jump if equal
    ADD SI, 2        ; Move to next word (2 bytes)
    LOOP L1          ; Decrement CX and loop
NOT_FOUND:
    MOV AL, 0        ; False
    RET
FOUND:
    MOV AL, 1        ; True
    RET

```

### Binary (Opcode representation based on 8086)

*A conceptual look at the machine instructions:*

* `3B 04` (CMP AX, [SI])
* `74 02` (JE to FOUND label)
* `46 46` (INC SI twice)
* `E2 F8` (LOOP back to L1)

---

*Created for Algorithms Documentation 2026*

