from code_listing_9_2_9_3 import process_line

def get_dict():
    word_count_dict = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_count_dict)
    return word_count_dict

import numpy
import pylab
def bar_graph(word_count_dict):
    '''bar graph of word-frequency, x-axis labeled with words'''
    # collect key and value list for plotting
    word_list = []
    for key, val in word_count_dict.items():
        if val > 2 and len(key) > 3:
            word_list.append((key, val))
    word_list.sort()
    key_list = [key for key, val in word_list]
    value_list = [val for key, val in word_list]
    # get ticks as the keys/words
    bar_width = 0.5
    x_values = numpy.arange(len(key_list))
    pylab.xticks(x_values, key_list, rotation=45)
    # create the bar graph
    pylab.bar(x_values, value_list, width=bar_width, color='r')
    pylab.show()

bar_graph(get_dict())