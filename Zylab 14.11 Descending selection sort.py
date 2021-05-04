# Srijana Shrestha
# 1918305

def selection_sort_descend_trace(numbers):

    for i in range(len(numbers) - 1):
        num = i

        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[num]:
                num = j

        numbers[i], numbers[num] = numbers[num], numbers[i]

        for k in numbers:
            print(k, end=' ')
        print()
    return numbers


if __name__ == '__main__':

    user_input = input().split()
    numbers = []
    for x in user_input:
        numbers.append(int(x))

    selection_sort_descend_trace(numbers)
