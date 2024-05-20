data_file = open("DataFile.txt", "r")
sum = 0
sum_num_pow = 0
count_all_nums = 0
while True:
    line = data_file.readline()
    if not line:
        break
    stringNum = line.split()
    for num in stringNum:
        if count_all_nums == 0:
            min = int(num)
            max = int(num)
        sum += int(num)
        count_all_nums += 1
        if min > int(num):
            min = int(num)
        if max < int(num):
            max = int(num)
        num_pow = pow(int(num), 2)
        sum_num_pow += num_pow

average = float(sum)/count_all_nums
averagePow = pow(average, 2)
variance = float(sum_num_pow - (count_all_nums * averagePow))/count_all_nums

print("The average is:", average)
print("The variance is:", variance)
print("The maximum number is:", max)
print("The minimum number is:", min)

data_file.close()


def binary_search(left, right):
    if right - left <= 0.005:
        return right
    mid = float(left + right)/2
    count_smaller_eq_mid = 0
    with open("DataFile.txt", "r") as data_file:
        line = data_file.readline()
        for line in data_file:
            string_num = line.split()
            for num in string_num:
                if mid >= int(num):
                    count_smaller_eq_mid += 1
        if float(count_smaller_eq_mid)/count_all_nums >= 0.6:
            return binary_search(left, mid)
        else:
            return binary_search(mid, right)


percentile60 = binary_search(min, max)
print("The 60 percentile number is:", percentile60)





