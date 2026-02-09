#include <stdio.h>
#include <string.h>

void compressString(char* str) {
    int n = strlen(str);
    if (n == 0) return;

    int writeIndex = 0; // ಔಟ್‌ಪುಟ್ ಬರೆಯಲು
    int readIndex = 0;  // ಸ್ಟ್ರಿಂಗ್ ಓದಲು

    while (readIndex < n) {
        char currentChar = str[readIndex];
        int count = 0;

        // ಒಂದೇ ರೀತಿಯ ಅಕ್ಷರಗಳನ್ನು ಎಣಿಕೆ ಮಾಡಿ (Count occurrences)
        while (readIndex < n && str[readIndex] == currentChar) {
            count++;
            readIndex++;
        }

        // ಅಕ್ಷರವನ್ನು writeIndex ಸ್ಥಾನಕ್ಕೆ ಕಾಪಿ ಮಾಡಿ
        str[writeIndex++] = currentChar;

        // ಎಣಿಕೆ 1ಕ್ಕಿಂತ ಹೆಚ್ಚಿದ್ದರೆ ಮಾತ್ರ ಸಂಖ್ಯೆಯನ್ನು ಬರೆಯಿರಿ
        if (count > 1) {
            // ಸಂಖ್ಯೆಯನ್ನು ಸ್ಟ್ರಿಂಗ್ ಆಗಿ ಪರಿವರ್ತಿಸಿ (e.g., 12 becomes "12")
            char countStr[10];
            int len = sprintf(countStr, "%d", count);
            
            for (int i = 0; i < len; i++) {
                str[writeIndex++] = countStr[i];
            }
        }
    }

    // ಕೊನೆಯಲ್ಲಿ Null character ಸೇರಿಸಿ ಸ್ಟ್ರಿಂಗ್ ಮುಕ್ತಾಯಗೊಳಿಸಿ
    str[writeIndex] = '\0';
}

int main() {
    char data[100] = "aaabbccccdddeeeeeeeeeeee"; // Example input
    
    printf("Original String: %s\n", data);
    
    compressString(data);
    
    printf("Compressed String: %s\n", data);
    
    return 0;
}