import sys
def open_file(text):
    f_histogram = open('words.txt', 'r')

    file_content = []
    for line in f_histogram:
        file_content.extend(line.split())
    

    return file_content
def histogram(file_content):
    histogram = {}
    for word in file_content:
        if word in histogram:
            histogram[word]+=1
        else:
            histogram[word]=1  
    return histogram

def unique_words(histogram):
    unique_words = 0
    for value in histogram.values():

        if value == 1:
            unique_words += 1
    return unique_words
def frequency(word, histogram):
    frequency_of_word = 0
    for key,value in histogram.items():
        if word == key:
            frequency_of_word += value

    return frequency_of_word



if __name__ == "__main__":
    words = open_file("words.txt")
    histo = histogram(words)
    print(histo)
    print(unique_words(histo))
    print(frequency('mornings.',histo))
    
     
     
        
    