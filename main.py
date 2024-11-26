# Programmers:  Paige Ronan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/20
# Assignment:  pa04
# Problem Statement:
# Data In: name of the headline file
# Data Out:
# Credits:
from operator import length_hint

from os import path

# Purpose:
# Parameters:
# Return:

def read_file_to_table(filename):
    table = []

    with open(filename, 'r') as file_data:  # Automatically handles file closing
        for line in file_data:
            line = line.split()


    return table


def count_specific_word(table):
    count = 0
    user_word = input("What word do you want to search for? ")
    while user_word != 'exit':
        for row in table:
            if user_word in row:
                count += 1
    print(f'The word {user_word} is in the headline {count} times')
    user_word = input("What word do you want to search for? \n"
                        "type 'exit' to exit the search ")

def write_headlines_with_word(table):
    word = input("What word do you want to use?")
    write_table = []
    for row in table:
        if word in row:
            write_table.append(row)
    output_file = input("What file do you want to use?")
    output_file = open(output_file, 'w')
    for row in write_table:
        output_file.write(row)
    output_file.close()
    return output_file

def average_headline_character(table):
    row_length = len(table[0])
    total_length = len(table)
    for row in table:
        total_length += row_length
    average = total_length / len(table)
    print(f'The average characters in each headline is {average}')

def longest_shortest_headline(table):
    long_length = 0
    short_length = 0
    longest_headline = ''
    shortest_headline = ''
    for row in table:
        row_length += len(row)
        if row_length > long_length:
            long_length = row_length
            longest_headline = row
        elif row_length < short_length:
            short_length = row_length
            shortest_headline = row_length
    print(f'The longest headline is {longest_headline}')
    print(f'The shortest headline is {shortest_headline}')


def main():
    user_input = input("What file do you want to analyze:")
    while not path.isfile(user_input):
        print("Invalid input")
        user_input = input("What file do you want to use?")
    headline_table = read_file_to_table(user_input)
    print('These are your options for analyze:\n'
        '1. Determine how many headlines have a particular word in it\n'
        '2. Write headlines containing a specific word to a new file\n'
        '3. Determine the average number of characters per headline\n'
        '4. Print the longest and shortest headline\n'
        '5. Read in a new file to analyze\n'
        'Type "exit" to quit')
    user_choice = input("What type of analysis do you want to do?")
    while user_choice != '1' and user_choice != '2' and user_choice != '3'\
            and user_choice != '4' and user_choice != '5':
        print("Invalid input")
        user_choice = input("What type of analysis do you want to do?")
    while user_choice != 'exit':
        if user_choice == '1':
            count_specific_word(headline_table)
        elif user_choice == '2':
            write_headlines_with_word(headline_table)
        elif user_choice == '3':
            average_headline_character(headline_table)
        elif user_choice == '4':
            longest_shortest_headline(headline_table)
        elif user_choice == '5':
            main()

print('Purpose: This program analyzes headlines from the Australian Broadcasting Company (ABC).\n'
      'You get to choose what type of analysis do you want to do.')
main()





