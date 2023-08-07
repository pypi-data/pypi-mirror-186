/*----------------------------------------------------------------------------------------
cdist_score.h

cdist_score
Calculates the difference in character distributions between two strings
----------------------------------------------------------------------------------------*/
#ifndef INCLUDE_GUARD_CDIST_SCORE
#define INCLUDE_GUARD_CDIST_SCORE

#include <stdlib.h>

double cdist_score(const char* str1, const char* str2)
{
    int total_len = 0;
    int total_diff = 0;
    int i;
    unsigned char chri;
    // int i1, i2, idist;

    int cdist[256] = {0};

    for (i = 0; *(str1 + i) != '\0'; i++)
    {
        chri = (unsigned char)(*(str1 + i));
        cdist[chri]++;
        total_len++;
    }

    for (i = 0; *(str2 + i) != '\0'; i++)
    {
        chri = (unsigned char)(*(str2 + i));
        cdist[chri]--;
        total_len++;
    }

    for (i = 0; i < 256; i++)
    {
        total_diff += abs(cdist[i]);
    }
    double final_score = (total_len - total_diff) / (double)total_len;
    return final_score;
}

#endif