''' os.rename(file_name,file_name.translate(None, "0123456789"))
Lower Version of python supports '''

import os    

def rename_file_names():
    #(1) get file names from a folder
    file_list=os.listdir(r"D:\2075\Python Examples\Python New Example\prank\prank")    
    print (file_list)    
    saved_path=os.getcwd()    
    print("current working direcorty is"+saved_path)    
    os.chdir(r"D:\2075\Python Examples\Python New Example\prank\prank")    
    remove="0123456789"    
    table=str.maketrans("","",remove)
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(table))
        os.rename(file_name,file_name.translate(table))    

rename_file_names() 
