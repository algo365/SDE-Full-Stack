#include <stdio.h>
#include <stdbool.h>

int getStringLength(char str[]);

#include <stdio.h>

/*
 * Compresses a string in-place using run-length encoding.
 *
 * Example:
 *   Input : "aaabbcdddd"
 *   Output: "a3b2cd4"
 *
 * Rules:
 *   - Count consecutive characters
 *   - Write character followed by count (only if count > 1)
 *   - Handle multi-digit counts
 */
void compressString(char str[])
{
    int readIndex  = 1;   // Used to read characters from input
    int writeIndex = 0;   // Used to write compressed output
    int count      = 1;   // Count of current character

    char prevChar = str[0];  // Store previous character

    // Traverse the string starting from second character
    while (str[readIndex] != '\0')
    {
        if (str[readIndex] == prevChar)
        {
            // Same character found, increase count
            count++;
        }
        else
        {
            // Different character found, write previous result
            str[writeIndex++] = prevChar;

            // Write count only if greater than 1
            if (count > 1)
            {
                // Convert count to characters (handles multi-digit counts)
                int temp = count;
                char digits[10];
                int digitCount = 0;

                while (temp > 0)
                {
                    digits[digitCount++] = (temp % 10) + '0';
                    temp /= 10;
                }

                // Digits are in reverse order, write them correctly
                for (int i = digitCount - 1; i >= 0; i--)
                {
                    str[writeIndex++] = digits[i];
                }
            }

            // Reset for new character
            prevChar = str[readIndex];
            count = 1;
        }

        readIndex++;
    }

    // Handle the last character group
    str[writeIndex++] = prevChar;

    if (count > 1)
    {
        int temp = count;
        char digits[10];
        int digitCount = 0;

        while (temp > 0)
        {
            digits[digitCount++] = (temp % 10) + '0';
            temp /= 10;
        }

        for (int i = digitCount - 1; i >= 0; i--)
        {
            str[writeIndex++] = digits[i];
        }
    }

    // Null-terminate the compressed string
    str[writeIndex] = '\0';
}

#include <stdio.h>

/*
 * Writes a character and its count into the string.
 * Count is written only if it is greater than 1.
 *
 * Returns updated write index.
 */
int writeCharAndCount(char str[], int writeIndex, char character, int count)
{
    // Write the character
    str[writeIndex++] = character;

    // Write the count only if greater than 1
    if (count > 1)
    {
        char countBuffer[12];  // Enough to hold large integers
        int length = sprintf(countBuffer, "%d", count);

        for (int i = 0; i < length; i++)
        {
            str[writeIndex++] = countBuffer[i];
        }
    }

    return writeIndex;
}

/*
 * Compresses the given string in-place using run-length encoding.
 *
 * Example:
 *   Input : "aaabbcdddd"
 *   Output: "a3b2cd4"
 */
void compressStringV2(char str[])
{
    if (str[0] == '\0')
    {
        return; // Empty string
    }

    int readIndex  = 1;
    int writeIndex = 0;
    int count      = 1;

    char prevChar = str[0];

    // Traverse the string
    while (str[readIndex] != '\0')
    {
        if (str[readIndex] == prevChar)
        {
            count++;
        }
        else
        {
            // Write previous character and its count
            writeIndex = writeCharAndCount(str, writeIndex, prevChar, count);

            // Reset for new character
            prevChar = str[readIndex];
            count = 1;
        }

        readIndex++;
    }

    // Handle the last character group
    writeIndex = writeCharAndCount(str, writeIndex, prevChar, count);

    // Null-terminate the compressed string
    str[writeIndex] = '\0';
}


bool isPalindrome(char str[])
{
    int length = getStringLength(str);
    int leftIndex = 0;
    int rightIndex = length-1;
    bool result = true;

    while (leftIndex < rightIndex)
    {
        if (str[leftIndex] != str[rightIndex])
        {
            result = false;
            break;
        }
        leftIndex++;
        rightIndex--;
    }

    return result;
}

void rev(char s[])
{
    int l = strlen(s);
    int i=0;
    int j = l-1;

    while(i<j)
    {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        i++;
        j--;
    }
}

void reverseString(char str[])
{
    int length = getStringLength(str);
    int leftIndex = 0;
    int rightIndex = length-1;

    while (leftIndex < rightIndex)
    {
        char temp = str[leftIndex];
        str[leftIndex] = str[rightIndex];
        str[rightIndex] = temp;
        leftIndex++;
        rightIndex--;
    }
}


int getStringLength(char str[])
{
    int index = 0;
    int count = 0;

    while (str[index] != '\0')
    {
        count++;
        //str[index] = 'z';
        //printf("\n %d -> %c", index, str[index]);
        index++;
    }
    return count;
}

int main() {
    char str[] = "mahesh";
    int length = getStringLength(str);
    printf("\n length of the string is %d", length);

    reverseString(str);
    printf("\n String after reversing is %s", str);

    char pal[] = "abccba";
    bool result = isPalindrome(pal);
    if (result)
    {
        printf("\n String is palindrome");
    }
    else
    {
        printf("\n String is not palindrome");
    }
}
