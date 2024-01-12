import os

def get_lines(line_numbers):
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    file_path = os.path.join(script_directory, 'datfile.dat')
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    with open(file_path, 'r') as cp:
        all_lines = cp.readlines()
        lines = [row for i, row in enumerate(all_lines) if i+1 in line_numbers]
        
    return lines


def paste_lines(allrows, copied_values):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, 'system', 'blockMeshDict')  # Update the path to include 'system'

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    # Read the lines from the file
    with open(file_path, 'r') as wp:
        all_lines = wp.readlines()

    j = 0

    # Modify the lines based on line numbers
    for i, rows in enumerate(all_lines):
        if i + 1 in allrows:
            all_lines[i] = copied_values[j] + '\n'
            j = j + 1 

    # Write the modified lines back to the file
    with open(file_path, 'w') as wp:
        wp.writelines(all_lines)



def editlines(lines,rlast,add):
    singlular_rows = []

    if rlast == 1:
        for i,row in enumerate(lines):
            split_lines = lines[i].split()
            del split_lines[1]
            singlular_rows.append(split_lines)
    else: 
        singlular_rows = lines

    combined_lines = []

    for i,row in enumerate(singlular_rows):
        added_lines = str(singlular_rows[i]).strip("[]'"'\n') + ' ' + add[i]
        combined_lines.append(added_lines)
    
    finalrow = []

    for i,row in enumerate(combined_lines):
        modified_row = '(' + combined_lines[i] + ')'
        finalrow.append(modified_row)
    return finalrow




#------------------VERTICES--------------------#

paste_lines([26],editlines(get_lines([91]),1,['-12.5 0']))    #   line 26
paste_lines([30],editlines(get_lines([594]),0,['0']))     #   line 30
paste_lines([31],editlines(get_lines([510]),0,['0']))    #   line 31
paste_lines([36],editlines(get_lines([91]),1,['12.5 0']))   #   line 36
paste_lines([37],editlines(get_lines([91]),0,['0']))    #   line 37
paste_lines([38],editlines(get_lines([7]),0,['0']))     #   line 38


paste_lines([44],editlines(get_lines([91]),1,['-12.5 0.1']))    #   line 44
paste_lines([48],editlines(get_lines([594]),0,['0.1']))     #   line 48
paste_lines([49],editlines(get_lines([510]),0,['0.1']))    #   line 49
paste_lines([54],editlines(get_lines([91]),1,['12.5 0.1']))   #   line 54
paste_lines([55],editlines(get_lines([91]),0,['0.1']))    #   line 55
paste_lines([56],editlines(get_lines([7]),0,['0.1']))     #   line 56



#------------------SPLINE--------------------#

    #   lines 152 to 158
lines_594_600 = get_lines(list(range(594,601)))
value3_594_600 = ['0'] * 7
erows_594_600 = editlines(lines_594_600,0,value3_594_600)
paste_lines(list(range(152,159)),erows_594_600)

    #   lines 159 to 164
lines_2_7 = get_lines(list(range(2,8)))
value3_2_7 = ['0'] * 6
erows_2_7 = editlines(lines_2_7,0,value3_2_7)
paste_lines(list(range(159,165)),erows_2_7)


   #   lines 169 to 175
lines_594_600 = get_lines(list(range(594,601)))
value3_594_600 = ['0.1'] * 7
erows_594_600 = editlines(lines_594_600,0,value3_594_600)
paste_lines(list(range(169,176)),erows_594_600)

    #   lines 176 to 181
lines_2_7 = get_lines(list(range(2,8)))
value3_2_7 = ['0.1'] * 6
erows_2_7 = editlines(lines_2_7,0,value3_2_7)
paste_lines(list(range(176,182)),erows_2_7)



#------------------POLYLINE--------------------#

    # polyline 12 -> 7 (dat lines: 91 to 300) (blockmesh lines: 188 to 397)
lines_91_300 = get_lines(list(range(91,301)))
value3_91_300 = ['0'] * 210
erows_91_300 = editlines(lines_91_300,0,value3_91_300)
paste_lines(list(range(188,398)),erows_91_300)

    # polyline 13 -> 12 (dat lines: 7 to 91) (blockmesh lines: 403 to 487)
lines_7_91 = get_lines(list(range(7,92)))
value3_7_91 = ['0'] * 85
erows_7_91 = editlines(lines_7_91,0,value3_7_91)
paste_lines(list(range(403,488)),erows_7_91)

    # polyline 27 -> 22 //same as 12->7 execpt 0.1// (dat lines: 91 to 300) (blockmesh lines: 492 to 701)
lines_91_300 = get_lines(list(range(91,301)))
value3_91_300 = ['0.1'] * 210
erows_91_300 = editlines(lines_91_300,0,value3_91_300)
paste_lines(list(range(492,702)),erows_91_300)

    # polyline 28 -> 27 //same as 13->12 execpt 0.1// (dat lines: 7 to 91) (blockmesh lines: 707 to 791)
lines_7_91 = get_lines(list(range(7,92)))
value3_7_91 = ['0.1'] * 85
erows_7_91 = editlines(lines_7_91,0,value3_7_91)
paste_lines(list(range(707,792)),erows_7_91)

    # polyline 22 -> 21 (dat lines: 301 to 510) (blockmesh lines: 796 to 1005)
lines_301_510 = get_lines(list(range(301,511)))
value3_301_510 = ['0.1'] * 210
erows_301_510 = editlines(lines_301_510,0,value3_301_510)
paste_lines(list(range(796,1006)),erows_301_510)

    # polyline 21 -> 20 (dat lines: 510 to 594) (blockmesh lines: 1010 to 1094)
lines_510_594 = get_lines(list(range(510,595)))
value3_510_594 = ['0.1'] * 85
erows_510_594 = editlines(lines_510_594,0,value3_510_594)
paste_lines(list(range(1010,1095)),erows_510_594)

    # polyline 7 -> 6 //same as 22->21 execpt 0// (dat lines: 301 to 510) (blockmesh lines: 1099 to 1308)
lines_301_510 = get_lines(list(range(301,511)))
value3_301_510 = ['0'] * 210
erows_301_510 = editlines(lines_301_510,0,value3_301_510)
paste_lines(list(range(1099,1309)),erows_301_510)

    # polyline 6 -> 5 //same as 21->20 execpt 0// (dat lines: 510 to 594) (blockmesh lines: 1313 to 1397)
lines_510_594 = get_lines(list(range(510,595)))
value3_510_594 = ['0'] * 85
erows_510_594 = editlines(lines_510_594,0,value3_510_594)
paste_lines(list(range(1313,1398)),erows_510_594)