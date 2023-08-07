/*----------------------------------------------------------------------------------------
levenshtein_score.h

Calculates a string similarity score based on the Levenshtein Distance
between two strings.

Final score is
(length of longest string - levenshtein distance) / (length of longest string)
----------------------------------------------------------------------------------------*/
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define MIN_OF_TWO(a, b)        (a > b ? b : a)
#define MIN_OF_THREE(a, b, c)   MIN_OF_TWO(MIN_OF_TWO(a, b), c)

// Kept for debugging - prints a score matrix of dimensions matrix[len1][len2]
void print_score_matrix(int *matrix, int len1, int len2)
{
    int idx1;
    int idx2;
    for (idx1 = 0; idx1 < len1; idx1++)
    {
        for (idx2 = 0; idx2 < len2; idx2++)
        {
            printf("%d ", *((matrix + idx1 * len2) + idx2));
        }
        printf("\n");
    }

}

double levenshtein_score(const char* str1, const char* str2)
{
    // Index/length for arrays stored separately from those of strings to avoid confusion
    int str_len1, str_len2;     // Length of strings
    int arr_len1, arr_len2;     // Length of matrix dimensions (as arrays)

    int str_idx1, str_idx2;     // For accessing string1 and string2
    int arr_idx1, arr_idx2;     // For accessing array x-dim and array y-dim

    int cost;

    str_len1 = strlen(str1);
    str_len2 = strlen(str2);

    arr_len1 = str_len1 + 1;    // Length of array in x dimension
    arr_len2 = str_len2 + 1;    // Length of array in y dimension


    // Dynamically allocated 2d array
    // reference i, j by: *(score_matrix + i*arr_len2 + j)
    int* score_matrix = (int*)malloc(arr_len1 * arr_len2 * sizeof(int));
    // int score_matrix[arr_len1][arr_len2];

    for (arr_idx1 = 0; arr_idx1 < arr_len1; arr_idx1++)
        *(score_matrix + arr_len2 * arr_idx1) = arr_idx1;
        // score_matrix[arr_idx1][0] = arr_idx1;

    for (arr_idx2 = 0; arr_idx2 < arr_len2; arr_idx2++)
        *(score_matrix + arr_idx2) = arr_idx2;
        // score_matrix[0][arr_idx2] = arr_idx2;

    for (arr_idx1 = 1; arr_idx1 < arr_len1; arr_idx1++)
    {
        for (arr_idx2 = 1; arr_idx2 < arr_len2; arr_idx2++)
        {
            str_idx1 = arr_idx1 - 1;
            str_idx2 = arr_idx2 - 1;

            cost = (*(str1 + str_idx1) != *(str2 + str_idx2));

            // Identify the lowest cost transformation for this cell
            *(score_matrix + arr_len2 * arr_idx1 + arr_idx2) = MIN_OF_THREE(
                1 + *(score_matrix + arr_len2 * arr_idx1 + (arr_idx2 - 1)),
                1 + *(score_matrix + arr_len2 * (arr_idx1 - 1) + arr_idx2),
                cost + *(score_matrix + arr_len2 * (arr_idx1 - 1) + (arr_idx2 - 1))
            );

            /* score_matrix[idx1][idx2] = min(
                1 + score_matrix[idx1][idx2-1],
                1 + score_matrix[idx1 - 1][idx2],
                cost + score_matrix[idx1 - 1][idx2 - 1]
            ) */
        }
    }

    // Levenshtein distance is final element in array 
    int distance = *(score_matrix + (arr_len2 * str_len1) + str_len2);
    free(score_matrix);

    // Correct/adjust score based on the longest string
    if (str_len1 > str_len2)
        return (str_len1 - distance) / (double)str_len1;
    else
        return (str_len2 - distance) / (double)str_len2;
}