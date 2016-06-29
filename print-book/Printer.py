#!python
import sys

from TextManager import TextManager

def store_result(filename, result_lines):
    output_file = open(filename, 'w')
    for i in range(len(result_lines)):
        if i != len(result_lines) - 1:
            output_file.write(result_lines[i] + '\n')
        else:
            output_file.write(result_lines[i])

if (len(sys.argv) < 4):
    print("Missing arguments. Please pass the <input_file> <output_file> <paper_type: A3 or A4>")
    exit()
if (sys.argv[3] not in ["A3", "A4"]):
    print("Incorrect paper_type. Please use either A3 or A4")
    exit()
try:
    input_file = open(sys.argv[1], 'r')
except (OSError, IOError) as e:
    print("Input file not found.")
    exit()
page_type = sys.argv[3]
char_width = 2
char_height = 3
width = (210 / char_width) + 1
height = (297 / char_height) + 1
if (page_type == "A3"):
    width = (297 / char_width) + 1
    height = (420 / char_height) + 1

text_manager = TextManager(input_file.read(), width, height)
result = text_manager.process_text()
store_result(sys.argv[2], result)
