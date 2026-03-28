#include <string.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    for (int i = 0; i < strlen(strs[0]); i++) {
        for (int j = 0; j < strsSize; j++) {
            if (i == strlen(strs[j]) || strs[j][i] != strs[0][i]) {
                strs[j][i] = '\0';
                return strs[j];
            }
        }
    }

    return strs[0];
}