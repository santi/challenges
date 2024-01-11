#include<iostream>
using namespace std;
// function prototypes
void selection_sort(int input_array[], int input_size);
void display_array(int input_array[], int input_size);
int main()
{
  int nums[25] = {2.345, 6.8245, 7.623467, 2345.6543, 7625.33, 24365.672,
                 2435.23454, 717689.651, 87984, 656.41654, 0.8546, -95654.121,
                 564.6541321, 12.12, 1546.4500, 0.5496, 0.123, 984.456, 2184.456,
                 551.5465, 555.1234, 666.4567, 777.6512, 0.0004, 0.1200};
  int length = 25;
  cout << "The array before the sort:\n";
  display_array(nums, length);
  selection_sort(nums, length);
  cout << "The array after the sort:\n";
  display_array(nums, length);
  cin.get();
  return 0;
}
// Selection sort procedure. Sorts an array of ints in descending order.
void selection_sort(int input_array[], int input_size)
{
  int i, j;
  int small, temp;

  for (i = input_size - 1; i > 0; i--)
   {
    small = 0;  // Initialize small to first element.

    // Find the smallest element between the positions 1 and i.
    for (j = 1; j <= i; j++)
     {
      if (input_array[j] < input_array[small])
       {
        small = j;
       }
     }
    // Swap the smallest element found with element in position i.
    temp = input_array[small];
    input_array[small] = input_array[i];
    input_array[i] = temp;
   }
}
// Function that simply displays each element of input_array.
void display_array(int input_array[], int input_size)
{
  int i;

  for (i = 0; i < input_size; i++)
   {
    cout << input_array[i] << ' ';
   }
  cout << "\n\n";
}
