# Theory :D


## Cases
| Algorithm   | Best Case                                                  | Worst case              | Average Case                                                                                                      |
|-------------|------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Bubble Sort | The array is ascending <br/>or <br/>all elements are equal | The array is descending | The array is shuffled                                                                                             | 
| Stooge Sort | There is no best case                                      | There is no worst case  | All cases have the same time complexity if we ignore the check between the first and last element of the subarray |

## Time complexities

| Algorithm   | Best Case          | Best Case Explanation | Worst Case           | Worst Case Explanation                                                                                                                                                                                                                                                                      |
|-------------|--------------------|-----------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bubble Sort | $\theta (n) = n-1$ | NaN                   | $\theta(n) = n(n-1)$ | Let $k$ be the final index of $i$-th element of the array $a$ of size $n$<br/> it takes $k$ steps to move element $a_i$ to it's position, and then $(n-1)-k$ more steps to check if the rest of the array is sorted<br/>That is for each element; hence $O(n) =n^2$ or $\theta(n) = n(n-1)$ |
| Stooge Sort | $O(n) = $          |                       |                      |                                                                                                                                                                                                                                                                                             |
