/*----------------------------------------------------------------------------------------
calc_groups.h

For use with method fss_score methods

Calc group - Stores an array of structs representing substrings

Each item in a CalcGroup represents a running substring whose relative order is common
between str1 and str2.

New potential character matches between one string and another are assessed against
each item in the CalcGroup, appending to an existing if both indices are higher
than the _calcitem representing that group.
----------------------------------------------------------------------------------------*/
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

/*========================================================================================
Helper functions
========================================================================================*/

// Finds the next power of 2 greater or equal to provided value
int next_pow2(unsigned int val)
{
    if (val == 0)
        return 1;
    
    if (val & (val - 1) == 0)
        return val;

    int num_shifts = 0;
    while(val > 1)
    {
        val = val>>1;
        num_shifts++;
    }
    return val<<(num_shifts + 1);
}


/*========================================================================================
Struct definition
========================================================================================*/

// "private" struct holding greatest indices of a substring
typedef struct CalcItem {
    int idx1;
    int idx2;
} _calcitem;

// Manager struct for CalcGroup
typedef struct CalcGroup {
    int idx2_min;           // Lowest idx2 of any _calcitem
    int length;             // Number of _calcitem elements in groups
    int matches;            // Total number of index matches found
    int offset_difference;  // Total difference in idx2 - idx1 offsets

    size_t _size;           // Internally-tracked size of array of _calcitem elems
    _calcitem* groups;      // Array of _calcitem elems representing substrings

} CalcGroup;


/*========================================================================================
Private Methods
========================================================================================*/

void _CalcGroup_resize(CalcGroup* self)
{
    while (self->length >= self->_size)
    {
        self->_size *= 2;
    }
    self->groups = (_calcitem*)realloc(self->groups, self->_size * sizeof(_calcitem));
}

/*========================================================================================
Public Methods
========================================================================================*/

// Add a new _calcitem to group at idx1, idx2
void CalcGroup_addNew(CalcGroup* self, int idx1, int idx2)
{
    if (self->length >= self->_size)
        _CalcGroup_resize(self);

    (*(self->groups + self->length)).idx1 = idx1;
    (*(self->groups + self->length)).idx2 = idx2;
    self->length++;

    if (idx2 < self->idx2_min)
        self->idx2_min = idx2;
}

// Attempts to add a new _calcitem with (idx1, idx2) at the best possible location by 
// minimizing offset difference by current indices idx1 and idx2 vs a _calcitem's
// idx1 and idx2.
// Returns a boolean flag indicating if placement was successful.
bool CalcGroup_addBest(CalcGroup* self, int idx1, int idx2)
{
    // If new item cannot be placed, return false
    if (idx2 < self->idx2_min || self->length == 0)
        return false;

   int loop_idx1;                   // idx1 on current item in loop
   int loop_idx2;                   // idx2 on current item in loop

   int loop_osdiff;                 // Offset difference in current loop

   int min_osdiff_found = INT_MAX;  // Lowest difference in offsets for idx1,idx2
   int secondmin_idx2 = INT_MAX;    // Second minimum idx2 in group
   int best_i = INT_MIN;
   _calcitem* best_item = NULL;     // Pointer to best candidate for placement
   _calcitem current;               // Current _calcitem under consideration

   for (int i = 0; i < self->length; i++)
   {
        current = *(self->groups + i);
        loop_idx1 = current.idx1;
        loop_idx2 = current.idx2;

        if (loop_idx2 > self->idx2_min && loop_idx2 < secondmin_idx2)
            secondmin_idx2 = loop_idx2;

        if (loop_idx2 > idx2)
            continue;

        loop_osdiff = abs((idx2 - loop_idx2) - (idx1 - loop_idx1));

        if (loop_osdiff < min_osdiff_found)
        {
            min_osdiff_found = loop_osdiff;
            best_i = i;
        }
   }

    // Didn't find any valid items - no placements
   if (best_i == INT_MIN)
        return false;

    // Need to update min_idx2 if its _calcitem replaced it
    if (self->groups[best_i].idx2 == self->idx2_min)
    {
        // Use replacement if it is smaller than second minimum idx2
        if (idx2 < secondmin_idx2)
            self->idx2_min = idx2;
        // Otherwise update to second minimum
        else 
            self->idx2_min = secondmin_idx2;
    }

    // Update with our found item
    self->matches++;
    self->offset_difference += min_osdiff_found;  // best_item should have lowest offset

    // Finally, update the element in question
    self->groups[best_i].idx1 = idx1;
    self->groups[best_i].idx2 = idx2;
    return true;
}

// Attempt to add a new _calcitem with (idx1, idx2) at the first possible placement
// location.
// Returns a boolean flag indicating if placement was successful.
bool CalcGroup_addFirst(CalcGroup* self, int idx1, int idx2)
{
    // If new item cannot be placed, return false
    if (idx2 < self->idx2_min || self->length == 0)
        return false;

   int loop_idx1;                   // idx1 on current item in loop
   int loop_idx2;                   // idx2 on current item in loop

   int secondmin_idx2 = INT_MAX;    // Second minimum idx2 in group
   _calcitem current;               // Current calcitem under consideration
   int best_i = INT_MIN;
   int osdiff_toadd = 0;            // Offset associated with best_item;

   for (int i = 0; i < self->length; i++)
   {
        current = *(self->groups + i);
        loop_idx1 = current.idx1;
        loop_idx2 = current.idx2;

        if (loop_idx2 > self->idx2_min && loop_idx2 < secondmin_idx2)
            secondmin_idx2 = loop_idx2;

        if (loop_idx2 > idx2)
            continue;

        if (best_i == INT_MIN)
        {
            osdiff_toadd = abs((idx2 - loop_idx2) - (idx1 - loop_idx1));
            best_i = i;
        }
   }

    // Didn't find any valid items - no placements
   if (best_i == INT_MIN)
        return false;

    // Need to update min_idx2 if its _calcitem replaced it
    if (self->groups[best_i].idx2 == self->idx2_min)
    {
        // Use replacement if it is smaller than second minimum idx2
        if (idx2 < secondmin_idx2)
            self->idx2_min = idx2;
        // Otherwise update to second minimum
        else 
            self->idx2_min = secondmin_idx2;
    }

    // Update with our found item
    self->matches++;
    self->offset_difference += osdiff_toadd;  // best_item should have lowest offset

    // Finally, update the element in question
    self->groups[best_i].idx1 = idx1;
    self->groups[best_i].idx2 = idx2;
    return true;
}

// Print out how CalcGroup currently looks
void CalcGroup_print(CalcGroup* self)
{
    printf("[");
    for (int i = 0; i < self->length; i++)
    {
        printf("(%d, %d)", (*(self->groups + i)).idx1, (*(self->groups + i)).idx2);
        if (i  != self->length - 1)
            printf(", ");
    }
    printf("]\n");
    // Now display properties
    printf("Length: %d\n", self->length);
    printf("Matches %d\n", self->matches);
    printf("Offset difference %d\n", self->offset_difference);
    printf("Min Idx2 %d\n", self->idx2_min);
}


void CalcGroup_deconstruct(CalcGroup* self)
{
    free(self->groups);
}


/*========================================================================================
API Macros
========================================================================================*/

// Use this to initialize when using one
#define CalcGroup_init(size) (CalcGroup) {\
    .idx2_min = INT_MAX,\
    .length = 0,\
    .matches = 0,\
    .offset_difference = 0,\
    ._size = (size > 4 ? next_pow2(size): 4),\
    .groups = (_calcitem*)malloc((size > 4 ? next_pow2(size) : 4) * sizeof(_calcitem))\
}


