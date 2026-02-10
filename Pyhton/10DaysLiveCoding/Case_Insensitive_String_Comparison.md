# Case-Insensitive String Comparison

## Question

Given two strings, they can contain both **upper-case** and **lower-case** characters.  
We need to check and compare the two strings in a **case-insensitive** manner.

---

## Algorithm / Logic (English Explanation)

1. **Check if lengths are the same**  
   - If the lengths are not the same, return `false`.

2. **Check for null or empty strings**  
   - If either string is `null` or empty, return `false`.

3. **Traverse both strings together**  
   - Write a loop to go over each character in both strings at the same time.
   - Compare the characters in a case-insensitive way.
   - If they are different at any point, return `false`.
   - Otherwise, continue the loop until the end of the string is reached.
   - The end of the string can be identified using the null character `\0`.

4. **Case-insensitive comparison using ASCII values**  
   - Before comparison, check whether the character is an upper-case or lower-case letter.
   - Based on that:
     - Subtract the ASCII value of base letter `'a'` for lower-case letters.
     - Subtract the ASCII value of base letter `'A'` for upper-case letters.

5. **Example**  

```
c - 'a' = 2
C - 'A' = 2
```

- Both give the same value.
- Compare these values to check if the characters are equal.
- If they are equal, continue.
- Otherwise, return `false` from the function.

6. **Final result**
- If the end of the string is reached and all characters match,
  return `true`.

---

## C Implementation

```c
#include <stdbool.h>
#include <stddef.h>

/*
 * Compares two strings in a case-insensitive manner
 * using ASCII value calculations.
 */
bool areStringsEqualIgnoreCase(const char *str1, const char *str2)
{
    int index = 0;

    /* Check for null strings */
    if (str1 == NULL || str2 == NULL) {
        return false;
    }

    /* Check for empty strings */
    if (str1[0] == '\0' || str2[0] == '\0') {
        return false;
    }

    /* Compare characters one by one */
    while (str1[index] != '\0' && str2[index] != '\0') {

        char char1 = str1[index];
        char char2 = str2[index];

        int value1;
        int value2;

        /* Normalize first character */
        if (char1 >= 'a' && char1 <= 'z') {
            value1 = char1 - 'a';
        } else if (char1 >= 'A' && char1 <= 'Z') {
            value1 = char1 - 'A';
        } else {
            return false;
        }

        /* Normalize second character */
        if (char2 >= 'a' && char2 <= 'z') {
            value2 = char2 - 'a';
        } else if (char2 >= 'A' && char2 <= 'Z') {
            value2 = char2 - 'A';
        } else {
            return false;
        }

        /* Compare normalized values */
        if (value1 != value2) {
            return false;
        }

        index++;
    }

    /* Check if both strings ended together */
    if (str1[index] != '\0' || str2[index] != '\0') {
        return false;
    }

    return true;
}
```

---

## Python Implementation

```python
def are_strings_equal_ignore_case(string1, string2):
    """
    Compares two strings in a case-insensitive manner
    using ASCII value calculations.
    """

    # Check for null (None) strings
    if string1 is None or string2 is None:
        return False

    # Check for empty strings
    if len(string1) == 0 or len(string2) == 0:
        return False

    # Check if lengths are equal
    if len(string1) != len(string2):
        return False

    # Compare characters one by one
    for index in range(len(string1)):
        char1 = string1[index]
        char2 = string2[index]

        # Normalize first character
        if 'a' <= char1 <= 'z':
            value1 = ord(char1) - ord('a')
        elif 'A' <= char1 <= 'Z':
            value1 = ord(char1) - ord('A')
        else:
            return False

        # Normalize second character
        if 'a' <= char2 <= 'z':
            value2 = ord(char2) - ord('a')
        elif 'A' <= char2 <= 'Z':
            value2 = ord(char2) - ord('A')
        else:
            return False

        # Compare normalized values
        if value1 != value2:
            return False

    return True
```

---

## Java Implementation

```java
public class StringComparator {

    /*
     * Compares two strings in a case-insensitive manner
     * using ASCII value calculations.
     */
    public static boolean areStringsEqualIgnoreCase(String str1, String str2) {

        // Check for null strings
        if (str1 == null || str2 == null) {
            return false;
        }

        // Check for empty strings
        if (str1.length() == 0 || str2.length() == 0) {
            return false;
        }

        // Check if lengths are equal
        if (str1.length() != str2.length()) {
            return false;
        }

        // Compare characters one by one
        for (int index = 0; index < str1.length(); index++) {

            char char1 = str1.charAt(index);
            char char2 = str2.charAt(index);

            int value1;
            int value2;

            // Normalize first character
            if (char1 >= 'a' && char1 <= 'z') {
                value1 = char1 - 'a';
            } else if (char1 >= 'A' && char1 <= 'Z') {
                value1 = char1 - 'A';
            } else {
                return false;
            }

            // Normalize second character
            if (char2 >= 'a' && char2 <= 'z') {
                value2 = char2 - 'a';
            } else if (char2 >= 'A' && char2 <= 'Z') {
                value2 = char2 - 'A';
            } else {
                return false;
            }

            // Compare normalized values
            if (value1 != value2) {
                return false;
            }
        }

        return true;
    }
}
```

---

## Summary

- Works with upper-case and lower-case characters  
- Uses ASCII-based normalization  
- Avoids built-in case-insensitive functions  
- Same logic implemented in **C**, **Python**, and **Java**  
- Ideal for **interviews**, **exams**, and **low-level understanding**
