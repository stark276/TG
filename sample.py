import random
from histogram import open_file, histogram, frequency

histogram = (histogram(open_file('words.txt')))

histogram1 = histogram(open_file())

print(frequency("the", histogram1)    

#histogram(open_file())))
# print(frequency("of", histogram(open_file())))
# print(total_words(histogram(open_file())))
# total_words = total_words(histogram)