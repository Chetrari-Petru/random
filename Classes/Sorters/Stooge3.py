def stoogesort(arr, l, h, currstep, steps, show = True):
    if l >= h:
        return

    # If first element is smaller
    # than last, swap them
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    # If there are more than 2 elements in
    # the array
    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)

        # Recursively sort first 2 / 3 elements
        stoogesort(arr, l, (h - t), currstep + 1, steps, False)

        # Recursively sort last 2 / 3 elements
        stoogesort(arr, l + t, (h), currstep + 1, steps, False)

        # Recursively sort first 2 / 3 elements
        # again to confirm
        stoogesort(arr, l, (h - t), currstep + 1, steps, False)
        if currstep % steps == 0 and show:
            print(arr)