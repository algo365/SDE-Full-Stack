#include <stdio.h>
#include <stdbool.h>

int getStringLength(char str[]);

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
