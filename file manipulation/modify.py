#Steven Bishop Feb 3, 2020 - CSIS 354 Spring
import os
import os.path
import sys

#general flag for any program errors
errors = False
error_message = ""

#test for a valid file in directory
if not(os.path.exists(sys.argv[1])):
    errors = True
    error_message ="\n\n Given file cannot be found!\n\n"

#test for a valid argument in  quantity
if(len(sys.argv) != 4):
    errors = True
    error_message ="\n\n Improper number of arguments given!\n\n"

#run main logic given no program errors
if not(errors):

    filepath = sys.argv[1] 
    filepath_temp = filepath + '.temp' #path name for temp working file

    in_file = open(filepath, 'r') #open read only file
    temp_file = open(filepath_temp, 'a') #create temp file to write/append to

    find_this = sys.argv[2] 
    replace_with_that = sys.argv[3]
    lines_updated = [] #line strings being updated
    line_numbers_affected = [] #line numbers being updated 

    line_number = 0
    for each_line in in_file:

        line_number += 1
        line = each_line
        
        #if the target text finds a match, then write line update to temp file
        #otherwise copy original line directly from the read file to the temp file
        if(find_this in line):
            line = line.replace(find_this,replace_with_that)
            temp_file.write(line)
            lines_updated.append(line)
            line_numbers_affected.append(line_number)
        else:
            temp_file.write(line)

    #close connection to the files
    in_file.close()
    temp_file.close()

    #if an update is performed, the original file becomes backup file .bak
    #the temp file is then renamed as the orignial
    #if a .bak already exists, it is overwritten
    #if no updates were performed. the orignal file is deleted,
    #the temp file becomes the new original 
    if(len(lines_updated) > 0):

        backup_file = os.path.splitext(in_file.name)[0]

        if(os.path.exists(backup_file + ".bak")):
            os.remove(backup_file + ".bak")

        os.rename(in_file.name, backup_file + ".bak")
        os.rename(temp_file.name,filepath)

        print("\n")

        i = 0
        for each_line in lines_updated:
            print(f"line {line_numbers_affected[i]}: {each_line}")
            i += 1
            
        print(f"\n\n Modify script run success, lines updated: {len(lines_updated)}\n\n")
    
    else:
        os.remove(in_file.name)
        os.rename(temp_file.name,filepath)

        print(f"\n\n Modify script run success, no match found!\n\n")


else:
    print(error_message) #print error message if main logic is not run
