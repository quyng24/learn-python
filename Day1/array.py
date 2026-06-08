arr = [1, 2, 3]
arr.append(4)   # [1, 2, 3, 4]
arr.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
arr.insert(2, 99)   # [1, 2, 99, 3, 4, 5, 6]
arr.remove(99)   # [1, 2, 3, 4, 5, 6]
arr.pop()   # trả về 6, arr còn [1, 2, 3, 4, 5]
arr.sort()       # [1, 2, 3, 4, 5]
arr.reverse()    # [5, 4, 3, 2, 1]


arr = [10, 20, 30, 40, 50]

arr[1:4]     # [20, 30, 40]   (từ index 1 đến 3)
arr[:3]      # [10, 20, 30]   (từ đầu đến index 2)
arr[::2]     # [10, 30, 50]   (lấy cách 2 phần tử)
arr[::-1]    # [50, 40, 30, 20, 10] (đảo ngược list)
arr[::1]     # [10, 20, 30, 40, 50]
