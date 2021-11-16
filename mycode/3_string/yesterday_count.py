# yesterday.txt 파일을 열기

"""
open mode

r : read, w : write
rb : read binary, wb : write binary
"""
def file_read(file_name):
    with open(file_name, "r") as file:
        lyric = file.read()
        return lyric


read = file_read("yesterday.txt")
print(read)
num_of_yesterday = read.upper().count("YESTERDAY")
print(f'Number of a word "YESTERDAY" {num_of_yesterday}')

num_of_yesterday = read.count("Yesterday")
print(f'Number of a word "Yesterday" {num_of_yesterday}')

num_of_yesterday = read.lower().count("yesterday")
print(f'Number of a word "yesterday" {num_of_yesterday}')
