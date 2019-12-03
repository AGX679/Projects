import shutil
import os
import os.path

# number 1 returns a list of all the 'parts.txt' file including path
def list_files_walk():
    """Returns a list of the paths of all 'parts.txt' files using os.walk generator
    
    Position Input Parameter:

            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(list_files_walk())

    """
    parts_txt_list = []
    search_pattern = 'parts.txt'
    top_dir = 'CarItems'
    for dir_path, dir_names, file_names in os.walk(top_dir): #using walk generator to navigate directory tree
        if search_pattern in file_names:
            file_path = os.path.join(dir_path, search_pattern) #combining names
            parts_txt_list.append(file_path)
    return parts_txt_list


# looping through the output to print out result
rtn_list = list_files_walk()
print("number 1 return a list of all the 'parts.txt' with path by using 'list_files_walk()'")
for i in range(len(rtn_list)):
    print('     ', rtn_list[i])
    
# number 2 
def list_files_recursive(top_dir):
    """Returns a list of the paths of all 'parts.txt' files using recursion
    
    Position Input Parameter:

            
    Keyword Input Parameters:
        None
        
    Examples:
    >>> print(list_files_walk())

    """
    list_items = os.listdir(top_dir)
    list_txt = []
    for item in list_items:
        item_path= os.path.join(top_dir, item)
        if os.path.isdir(item_path):
            list_txt = list_txt + list_files_recursive(item_path)
        else:
            if os.path.splitext(item)[-1].lower() =='.txt':
                list_txt = list_txt + [item_path]
    return list_txt
   
# looping through the output to print out result 
rec_list = list_files_recursive('CarItems')
print("number 2 return a list of all the 'parts.txt' with path by using 'list_files_recursive()'")
for i in range(len(rec_list)):
    print('     ', rec_list[i])
    
    
# number 3 - checking if both functions have the same output
first_list = list_files_walk()
sec_list = list_files_recursive('CarItems')
print("number 3 Is the output of the first function equal to the second?:\n", first_list.sort() == sec_list.sort())

#number 4
top_dir = 'CarItemsCopy'
try: #try/except for testing
    shutil.copytree('CarItems', top_dir)
except FileExistsError:
    shutil.rmtree(top_dir)
    shutil.copytree('CarItems', top_dir)
    
def change_and_move(dir_names): 
    """Modify CarItemsCopy to have the year as part of the file names, and by
       removing the year directories.
    
    Position Input Parameter:
        
    Keyword Input Parameters:
        None
        
    Examples:
    >>> change_and_move('CarItemsCopy')
    """
    for dir_path, dir_names, file_names in os.walk(top_dir):# to find if current dir is a year directory
        if os.path.basename(dir_path).isdigit():
            #print('\n' + 'current directory: ', dir_path)
            for f_item in file_names:
                years = os.path.basename(dir_path) #storing the years to be added into the filename
                #print(os.path.join(f_item, years))
                #print(f_item.split('.')[0])
                #print(f_item.split('.')[1])
                f_item_chg = f_item.split('.')[0] + '-' + years + '.' + f_item.split('.')[1] # splits the file name and formats by name, year, and extension
                f_item_path = os.path.join(dir_path, f_item) #source path
                f_item_chg_path = os.path.join(os.path.dirname(dir_path), f_item_chg) #destination path
                
                #print('     source file path', f_item_path)
                #print('     destination file path', f_item_chg_path)
                shutil.copy(f_item_path, f_item_chg_path)
                #print(dir_path) 
            shutil.rmtree(dir_path) #removing the year directories
    return                 
change_and_move('CarItemsCopy')
print('number 4 executed')        
       
