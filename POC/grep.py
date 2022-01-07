import os


def fun_grep(path, files, string):
    #listing of directories and file in give directory
    dir_list = os.listdir(path)

    for i in dir_list:
        i = os.path.join(path, i)
        #checking if it is dirrctory or file
        if (os.path.isdir(i)):
            # i is directory travesal to the directory
            files + fun_grep(i, files, string)

        else:
            try:
                #Try to read text file
                f = open(i, 'rt')
                file = f.read()

                #checking if string present in the file
                if string in file:
                    #store the path of file
                    files.append(i)
            except:
                # file is binary file
                pass
            finally:
                f.close()

    return files


path = r'C:\Users\Pavan\Desktop\desktop\paper'
files_path = []
string = "Apple"
fun_grep(path, files_path, string)
for i in files_path:
    print(i)
