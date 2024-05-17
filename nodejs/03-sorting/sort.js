let testArray = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 1, 2, 3, 4, 5, 6, 7]

function selectionSort(arr){


  for(let i = 0; i < arr.length - 1; i++){
    let min_index = i; // index of the smallest element

    for(let j = i + 1; j < arr.length; j++){
      if (arr[j] < arr[min_index]){
        min_index = j;
      }
    }

    if (min_index != i){
      [arr[i], arr[min_index]] = [arr[min_index], arr[i]];
    }
  }
}



