# program for printing a list of WOs for kittening

import sys

file1 = open(sys.argv[1],"r+")

print('opening: ', str(sys.argv[1]))

all_lines = file1.readlines()
line1= all_lines[0]


for i in range(0, len(all_lines)):
    print(all_lines[i])


wo_edit = []
wo_edit = [0 for i in range(len(all_lines))]

#delete the first line 
#all_lines[0] = ''

for i in range(0, len(all_lines)):

    line = all_lines[i]

    # check if first char is a number
    if line == '':
        break
    else:
        line_first_char = line[0]
        if line_first_char.isnumeric() == False:
            all_lines[i] = ''
            line = all_lines[i]

    # how to iterate through finding the WO number 

    # take out frist dash and text before it

    dashes_1 = line.find('-')

    line_edit = line[dashes_1+1:len(line)]

    # take out 2nd dash and text before it

    dashes_2 = line_edit.find('-')

    line_edit_2 = line_edit[dashes_2+1:len(line_edit)]

    # sku variation stays 3 digits so it's safe to print chars 4-9 of updated WO line

    WO_number = line_edit_2[4:9]

    wo_edit[i] = WO_number


wo_edit = list(filter(None, wo_edit))


# add verificaiton order to each line
print('WOs for kittening: ')
for i in range(0, len(wo_edit)):
    wo_edit[i] = str(i+1) + '. ' + wo_edit[i]
    print(wo_edit[i])



file1.close()


