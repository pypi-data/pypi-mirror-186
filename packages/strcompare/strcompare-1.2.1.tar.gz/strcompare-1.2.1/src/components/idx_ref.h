/*=======================================================================================
idx_ref.h

Framework for tracking the indices (by character) for characters in a given model string

Basic struct consists of three parts:
    1. chr_counts
        A 0-255 indexed array representing the number of instances per character
        in a modeled string. (index corresponds to chr code of a character, i.e. 'A' - 65)
    2. ptr_ref
        A 0-255 indexed arry reprsenting pointer-offsets where a particular character
        is referenced in idx_arr (3.). Value corresponding to character represents
        where to look in idx_arr to find what indices a character appears at in the
        modeled string. Defaults to 0, indicating an invalid reference.
    3. idx_arr
        An array of all indices from modeled string for each character. One contiguous
        block, identified by referencing ptr_ref. Note that space allocated is one
        greater than string, as index 0 is "blocked off" as invalid.

Example:
string 'lava' results in the following (non-represented characters excluded, will be 0)
l a v a
0 1 2 3 
chr_counts              ptr_ref             idx_arr
    IDX         VAL     IDX         VAL     IDX     VAL
     97 ('a')   2        97 ('a')    2      0       N/A
    108 ('l')   1       108 ('l')    1      1       0       (l, FIRST IDX)       
    118 ('v')   1       118 ('v')    4      2       1       (a, FIRST IDX)
                                            3       3       (a, SECOND_IDX)    
                                            4       2       (v, FIRST_IDX)      
========================================================================================*/
#ifndef INCLUDE_GUARD_IDXREF
#define INCLUDE_GUARD_IDXREF
#include <stdlib.h>


/*=======================================================================================
Structure Definition
========================================================================================*/

typedef struct {
    int* chr_counts;        // Array of counts per character
    int* ptr_ref;           // Array of pointer offsets per character to look into idx_arr
    int* idx_arr;           // Array of all indices found for a provided string
} IdxRef;


/*=======================================================================================
Public methods
========================================================================================*/

// Build an index reference based on a provided string. Also required to pass
// two 256-sized arrays, initialized to 0 chr_counts and ptr_ref
void IdxRef_build(IdxRef* self, const char* str, int* chr_counts, int* ptr_ref)
{
    int i;
    unsigned char chri;
    int current_offset;
    int total_size = 0;
    int min_idx[256] = {0};

    // Point IdxRef tracking arrays to those passed
    self->chr_counts = chr_counts;
    self->ptr_ref = ptr_ref;

    // Gather information about str before building
    for (i = 0; *(str + i) != '\0'; i++)
    {
        chri = (unsigned char)(*(str + i));
        total_size++;
        self->chr_counts[chri]++;
    }

    // One malloc
    // pointer ref 0 used as invalid, reserve index 0 for N/A.
    self->idx_arr = (int*)malloc((1 + total_size) * sizeof(int));
    current_offset = 1;

    for (i = 0; *(str + i) != '\0'; i++)
    {
        chri = (unsigned char)(*(str + i));
        // If still 0 (from allocation), we haven't pointed this char to a block yet
        if (self->ptr_ref[chri] == 0)
        // if (*(self->ptr_ref + chri) == 0)
        {
            // Assign next available block to current character (at current_offset)
            self->ptr_ref[chri] = current_offset;
            // Set current_offset to start of next available block
            // current_offset += *(self->chr_counts +chri);
            current_offset += self->chr_counts[chri];
        }

        *(self->idx_arr + self->ptr_ref[chri] + min_idx[chri]) = i;
        min_idx[chri]++;
    }
}

// Retrieve ith index for a given character from idx_ref 
int IdxRef_getIndex(IdxRef* self, unsigned char chr, int chr_num)
{
    return *(self->idx_arr + self->ptr_ref[chr] + chr_num);
}

// Set the ith index for a given character in idx_ref to a new value
void IdxRef_updateIndex(
    IdxRef* self, unsigned char chr, int chr_num, int new_val
)
{
    *(self->idx_arr + self->ptr_ref[chr] + chr_num) = new_val;
}

int IdxRef_getChrCount(IdxRef* self, unsigned char chr)
{
    return self->chr_counts[chr];
}

void IdxRef_deconstruct(IdxRef* self)
{
    free(self->idx_arr);
}

#endif