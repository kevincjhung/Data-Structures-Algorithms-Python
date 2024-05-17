static void SelectionSort(int[] arr)
{
    for (int i = 0; i < arr.Length - 1; i++)
    {
        int minIndex = i; // index of the smallest element

        for (int j = i + 1; j < arr.Length; j++)
        {
            if (arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }

        if (minIndex != i)
        {
            // Swap elements
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}


int[] testArray = { 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 1, 2, 3, 4, 5, 6, 7 };
SelectionSort(testArray);
Console.WriteLine("Sorted Array:");

foreach (int num in testArray)
{
    Console.Write(num + " ");
}