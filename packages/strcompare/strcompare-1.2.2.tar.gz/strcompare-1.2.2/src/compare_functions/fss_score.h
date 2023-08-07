/*----------------------------------------------------------------------------------------
fcs_score.h

Fragmented Substring Score

"Fractured Substring"
    A series of character matches between two strings where characters are in the same
    relative order, i.e. for AGREE vs EAGER, fractured substrings would be:
        AGREE vs EAGER
        __R_E vs E___R => AGE
        ____E vs E____ => R
        _____ vs _____ => E
    Note that fractured substrings work "without replacement", and the total combinations
    of all characters between fractured substrings should match the total distribution
    of matching characters between str1 and str2

Behavior types:
---------------------------------------
SCORING - how points are assessed
    normal - considers each character match 1 point
    adjusted - corrects each character match down by difference in idx1 & idx2 offsets 

PLACEMENT - how to decide which running substr (calc group) a match is placed onto
    first - adds to the first discovered substring in calc group
    best - considers each calc group and places on the one with minimum offset difference

fcs_score
    SCORING = normal
    PLACEMENT = first

adjusted_fss_score
    SCORING = adjusted
    PLACEMENT = best


        

----------------------------------------------------------------------------------------*/
#ifndef INCLUDE_GUARD_FSS_SCORE
#define INCLUDE_GUARD_FSS_SCORE

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#include "../components/calc_groups.h"
#include "../components/utility_functions.h"

#include "../components/idx_ref.h"

// Scores two strings based on the number of substring matches between the two

// Assigns a point per character-to-character match within each fractured substring
// between str1 and str2. Score is calculated as the ratio of total points to the maximum
// number of possible points (i.e. length of shorter string - 1)
double fss_score(const char* str1, const char* str2)
{

    // General variables
    int idx1, idx2;                 // indices for accessing str1 and str2
    int len1, len2;                 // lengths of str1 and str2
    CalcGroup cg;                   // CalcGroup struct for tracking results

    IdxRef iref;                    // string index tracking struct for str2
    int chr_counts[256] = {0};      // character count array for iref
    int ptr_ref[256] = {0};         // pointer ref array fo iref

    // Loop tracking variables
    unsigned char chr1;             // Current character from str1 being considered
    int num_indices;                // Number of idx2 matching this chr1
    int i;                          // Current index accessing idx_ref for current chr1
    bool valid_found;               // Whether idx_ref at this chr1 has something to place
    bool match_placed;              // Whether idx2 was placed into a calc group for chr1
    int valid_i;                    // i within idx_ref to use if no matches found


    // Swap str1 and str2 if str1 is chosen as the basis 
    int basis_code = choose_fss_basis(str1, str2);
    if (basis_code == 0)
    {
        const char* temp = str1;
        str1 = str2;
        str2 = temp;
    }

    len1 = strlen(str1);
    len2 = strlen(str2);

    // Due to how score is calculated, cannot perform regular algorithm on lengths
    // less than 2

    // Both empty - 100% equal
    if (len1 == 0 && len2 == 0)
        return (double)1;
    // Exactly 1 empty - 0% equal
    else if ((len1 == 0) != (len2 == 0))
        return (double)0;
    // 1 is either empty or has one character. Check if str2 has its matching char
    else if (len1 < 2)
    {
        for (idx2 = 0; idx2 < len2; idx2++)
        {
            if (*str1 == *(str2 + idx2))
                return (double)1;
        }
        return (double)0;
    }

    // Begin score calculation
    cg = CalcGroup_init(len1/2);  // Initialize size to roughly half of len1
    IdxRef_build(&iref, str2, chr_counts, ptr_ref);

    // Consider each character in str1
    for (idx1 = 0; idx1 < len1; idx1++)
    {
        chr1 = (unsigned char)(*(str1 + idx1));
        num_indices = IdxRef_getChrCount(&iref, chr1);

        // Now decide if we can place on existing or have to create a item in calc group
        valid_found = false;
        match_placed = false;
        for (i = 0; i < num_indices; i++)
        {
            idx2 = IdxRef_getIndex(&iref, chr1, i);

            if (!valid_found && idx2 >= 0)
            {
                valid_found = true;
                valid_i = i;
            }

            // Cannot place, go to next idx2
            if (idx2 <= cg.idx2_min)
                continue;

            // By getting here, idx2 should be able to be placed. Check just in case
            match_placed = CalcGroup_addFirst(&cg, idx1, idx2);
            if (match_placed)
            {
                // Mark as considered
                IdxRef_updateIndex(&iref, chr1, i, -1);
                break;
            }
        }

        // If we didn't place a match, need to add a new item to calc group
        // Use the first valid (> -1) idx2 encountered, if one exists (otherwise none
        // to place)
        if (!match_placed && valid_found)
        {
            idx2 = IdxRef_getIndex(&iref, chr1, valid_i);
            CalcGroup_addNew(&cg, idx1, idx2);
            // Also mark this idx2 as already used
            IdxRef_updateIndex(&iref, chr1, valid_i, -1);
        }
    }

    double to_return = cg.matches / (double)(len1 - 1);

    // Free allocated memory
    IdxRef_deconstruct(&iref);
    CalcGroup_deconstruct(&cg);

    return to_return;
}


// Assigns x points per character-to-character match within each fractured substring,
// where x = len(longer string) - 2.
// Assesses a penalty of y, where
// y = |(difference in str2 indices) - (difference in str1 indices)|
// Giving the points per character match = x - y.
// Tabulated score is then divided by the maximum possible score z, where
// z = (len(longer_string) - 2) * (len(shorter_string) - 1)
// The adjusted_fss_score is then calculated as sum(x - y) / z
double adjusted_fss_score(const char* str1, const char* str2)
{
    // General variables
    int idx1, idx2;                 // indices for accessing str1 and str2
    int len1, len2;                 // lengths of str1 and str2
    CalcGroup cg;                  // CalcGroup struct for tracking results

    IdxRef iref;                    // string index tracking struct for str2
    int chr_counts[256] = {0};      // character count arry for iref
    int ptr_ref[256] = {0};         // pointer ref array for iref

    // Loop tracking variables
    char chr1;                      // Current character from str1 being considered
    int num_indices;                // Number of idx2 matching this chr1
    int i;                          // Current index accessing idx_ref for current chr1
    bool valid_found;               // Whether idx_ref at this chr1 has something to place
    bool match_placed;              // Whether idx2 was placed into a calc group for chr1
    int valid_i;                    // i within idx_ref to use if no matches found



    // Identify which to use as basis. Swap if needed (str2 will be basis)
    int basis_code = choose_fss_basis(str1, str2);
    if (basis_code == 0)
    {
        const char* temp = str1;
        str1 = str2;
        str2 = temp;
    }

    // Calculate lengths & build reference for str2
    len1 = strlen(str1);
    len2 = strlen(str2);

    // Due to how score is calculated, cannot perform regular algorithm on strings
    // where len1 < 2 or len2 < 3

    // Both empty - 100% equal
    if (len1 == 0 && len2 == 0)
        return (double)1;
    // Exactly 1 empty - 0% equal
    else if ((len1 == 0) != (len2 == 0))
        return (double)0;
    // len1 too short - check if chr2 has a match
    else if (len1 == 1)
    {
        for (idx2 = 0; idx2 < len2; idx2++)
        {
            if (*str1 == *(str2 + idx2))
                return (double)1;
        }
        return (double)0;
    }
    // len2 is too short, manually handle edge cases
    else if (len2 < 3)
    {
        // here len1 == 2 and len2 == 2, all other possibilities are accounted for above
        // simply return the # of matching idx/chars / 2
        int shortscore = 0;
        shortscore += (*(str1 + 1) == *(str2 + 1));
        shortscore += (*str2 == *str1);
        return (double)shortscore/2;
    }

    // Begin score calculation
    cg = CalcGroup_init(len1/2);  // Begin with size roughly equal to half of len1
    IdxRef_build(&iref, str2, chr_counts, ptr_ref);

    // Consider each character in str1
    for (idx1 = 0; idx1 < len1; idx1++)
    {
        chr1 = (unsigned char)(*(str1 + idx1));
        num_indices = IdxRef_getChrCount(&iref, chr1);
        // num_indices = char_counts[chr1];

        // Now decide if we can place on existing or have to create a new calc group
        valid_found = false;
        match_placed = false;
        // Consider each matched idx2
        for (i = 0; i < num_indices; i++)
        {
            idx2 = IdxRef_getIndex(&iref, chr1, i);

            // Flag that at least one idx2 at this character is valid
            if (!valid_found && idx2 >= 0)
            {
                valid_found = true;
                valid_i = i;
            }

            // Cannot place idx2 on an existing group, skip
            if (idx2 <= cg.idx2_min)
                continue;

            // By getting here, idx2 should be able to be placed. Check just in case
            match_placed = CalcGroup_addBest(&cg, idx1, idx2);
            if (match_placed)
            {
                // Mark as considered
                IdxRef_updateIndex(&iref, chr1, i, -1);
                break;
            }
        }

        // If we didn't place a match, need to add a new element
        // If valid_found == false, then there are no more idx2 for this char1 to place
        if (!match_placed && valid_found)
        {
            idx2 = IdxRef_getIndex(&iref, chr1, valid_i);
            CalcGroup_addNew(&cg, idx1, idx2);
            // Also mark this idx2 as already used
            IdxRef_updateIndex(&iref, chr1, valid_i, -1);
        }
    }

    // Have to math it out, as CalcGroup tabulates the total index difference
    // but doesn't know len2. Can use algebra to simplify to something calculable
    double to_return = (
        ( ((len2 - 2) * cg.matches) - cg.offset_difference ) 
        /
        (double)( (len2 - 2) * (len1 - 1) )
    );

    // Free allocated memory
    CalcGroup_deconstruct(&cg);
    IdxRef_deconstruct(&iref);

    return to_return;
}

// Utilizes naive method to identify fractured substring matches. Score as fss_score
// does with a different algorithm (On3)
double naive_fss_score(const char* str1, const char* str2)
{
    int idx1, idx2;
    int sub_idx1, sub_idx2;
    int len1, len2;

    int total_score = 0;
    bool firstpass;

    // Swap strings to ensure proper order
    if (choose_fss_basis(str1, str2) == 0)
    {
        const char* temp = str1;
        str1 = str2;
        str2 = temp;
    }

    len1 = strlen(str1);
    len2 = strlen(str2);

    // Early exit conditions based on edge cases
    if (len1 == 0 && len2 == 0)
        return 1;
    else if ((len1 == 0) != (len2 == 0))
        return 0;
    // No fragmented substrings when one string is one long
    else if (len1 == 1)
    {
        for (idx2 = 0; idx2 < len2; idx2++)
            if (*str1 == *(str2 + idx2)) return 1;
        return 0;
    }
    else if (len2 == 1)
    {
        for (idx1 = 0; idx1 < len1; idx1++)
            if (*(str1 + idx1) == *str2) return 1;
        return 0;
    }

    char* copy1 = (char*)malloc((len1 + 1) * sizeof(char));
    char* copy2 = (char*)malloc((len2 + 1) * sizeof(char));

    // Make copies since we'll be "crossing off" characters by overwriting them with '\0'
    strcpy(copy1, str1);
    strcpy(copy2, str2);

    idx1 = 0;
    idx2 = 0;
    do
    {
        idx1 = 0;
        idx2 = 0;
        firstpass = true;

        // Initialize idx1 and idx2 to the first non-crossed-off character
        while (*(copy1 + idx1) == '\0' && idx1 < len1)
            idx1++;

        while (*(copy2 + idx2) == '\0' && idx2 < len2)
            idx2++;

        sub_idx1 = idx1;
        sub_idx2 = idx2;

        while (sub_idx1 < len1)
        {
            if (idx2 == len2)  // Shortcut if we've matched to the final str2 character
                break;
            else if (sub_idx2 == len2)
            {
                // Set str1 index to next available character (or end of string)
                do {sub_idx1++;} while (*(copy1 + sub_idx1) == '\0' && sub_idx1 < len1);
                sub_idx2 = idx2;
            }
            else if (*(copy1 + sub_idx1) == *(copy2 + sub_idx2))
            {
                // Don't add a point if this is the first char match in this pass
                total_score += !firstpass;
                firstpass = false;

                // Cross off these characters since we've used them
                *(copy1 + sub_idx1) = '\0';
                *(copy2 + sub_idx2) = '\0';

                // Set indices to next available character (or end of string)
                do {sub_idx1++;} while (*(copy1 + sub_idx1) == '\0' && sub_idx1 < len1);
                do {sub_idx2++;} while (*(copy2 + sub_idx2) == '\0' && sub_idx2 < len2);

                // Move our reference indices to match
                idx1 = sub_idx1;
                idx2 = sub_idx2;

            } else
            {
                do {sub_idx2++;} while (*(copy2 + sub_idx2) == '\0' && sub_idx2 < len2);
            }
        }

        // Exit if we've traversed all of str1 without a match
    } while (!firstpass);

    free(copy1);
    free(copy2);
    return total_score / (double)(len1 - 1);
}


// Applies the scoring method from adjusted_fss_score and the fragmented substring
// finding algorithm from naive_fss_score.
double adjusted_naive_fss_score(const char* str1, const char* str2)
{
    int idx1, idx2;
    int sub_idx1, sub_idx2;
    int len1, len2;

    int osdiff;
    int total_score = 0;
    bool firstpass;

    // Swap strings to ensure proper order
    if (choose_fss_basis(str1, str2) == 0)
    {
        const char* temp = str1;
        str1 = str2;
        str2 = temp;
    }

    len1 = strlen(str1);
    len2 = strlen(str2);

    // Early exit conditions based on edge cases
    if (len1 == 0 && len2 == 0)
        return 1;
    else if ((len1 == 0) != (len2 == 0))
        return 0;
    // No fragmented substrings when one string is one long
    else if (len1 == 1)
    {
        for (idx2 = 0; idx2 < len2; idx2++)
            if (*str1 == *(str2 + idx2)) return 1;
        return 0;
    }
    else if (len2 == 1)
    {
        for (idx1 = 0; idx1 < len1; idx1++)
            if (*(str1 + idx1) == *str2) return 1;
        return 0;
    }
    else if (len2 < 3)
    {
        // Only encountered here when len1 == len2 == 2, all others are accounted for
        int shortscore = 0;
        shortscore += (*(str1 + 1) == *(str2 + 1));
        shortscore += (*str2 == *str1);
        return (double)shortscore/2;
    }

    char* copy1 = (char*)malloc((len1 + 1) * sizeof(char));
    char* copy2 = (char*)malloc((len2 + 1) * sizeof(char));

    // Make copies since we'll be "crossing off" characters by overwriting them with '\0'
    strcpy(copy1, str1);
    strcpy(copy2, str2);

    idx1 = 0;
    idx2 = 0;
    do
    {
        idx1 = 0;
        idx2 = 0;
        firstpass = true;

        // Initialize idx1 and idx2 to the first non-crossed-off character
        while (*(copy1 + idx1) == '\0' && idx1 < len1)
            idx1++;

        while (*(copy2 + idx2) == '\0' && idx2 < len2)
            idx2++;

        sub_idx1 = idx1;
        sub_idx2 = idx2;

        while (sub_idx1 < len1)
        {
            if (sub_idx2 == len2)
            {
                // Set str1 index to next available character (or end of string)
                do {sub_idx1++;} while (*(copy1 + sub_idx1) == '\0' && sub_idx1 < len1);
                sub_idx2 = idx2;
            }
            else if (*(copy1 + sub_idx1) == *(copy2 + sub_idx2))
            {
                // Don't add points if this is our first match
                if (!firstpass)
                {
                    osdiff = abs( (sub_idx2 - idx2) - (sub_idx1 - idx1) );
                    total_score += ( (len2 - 2) - osdiff);
                }
                else
                    firstpass = false;

                // Cross off these characters since we've used them
                *(copy1 + sub_idx1) = '\0';
                *(copy2 + sub_idx2) = '\0';

                // Move basis indices to remember last found match
                idx1 = sub_idx1;
                idx2 = sub_idx2;

                // Set indices to next available character (or end of string)
                do {sub_idx1++;} while (*(copy1 + sub_idx1) == '\0' && sub_idx1 < len1);
                do {sub_idx2++;} while (*(copy2 + sub_idx2) == '\0' && sub_idx2 < len2);


            } else
            {
                do {sub_idx2++;} while (*(copy2 + sub_idx2) == '\0' && sub_idx2 < len2);
            }
        }

        // Exit if we've traversed all of str1 without a match
    } while (!firstpass);

    free(copy1);
    free(copy2);
    return total_score / (double)( (len2 - 2) * (len1 - 1) );
}

#endif