import random
import sys
file = []
tile = ['zz', 'kk', 'cc', 'dd', 'ee']
with open("/usr/share/dict/words", "r") as f:
    for line in f:
        file.append(line.strip())
# print(file)
def random_sentence(word_list, length):
    choosen_words = []

    for _ in range(length):
        random_index = random.randint(0, len(word_list)-1)
        choosen_words.append(word_list[random_index])
        # print(choosen_words)
        word_list.remove(word_list[random_index])
    print(" ".join(choosen_words))

# random_sentence(file, 10)


if __name__ == "__main__":
    params = sys.argv[1:]
    number = int(params[0])
    if number < 2:
        print("Not enough for sentence")
    elif number == None:
        print("not correct")
    else:
        random_sentence(file, number)







# nums = [1,2,3,4,5]

# for num in nums:
#     if num == 3:
#         print('Found')
#         continue
#     print(num)
# for num in nums:
#     for letter in 'abce':
#         print(num, letter)
# x = 0 

# while x < 10:
#     if x == 5:
#         print('found')
#     print(x)
#     x = x + 1
    