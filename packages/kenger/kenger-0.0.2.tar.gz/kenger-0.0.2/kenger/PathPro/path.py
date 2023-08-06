import os

#当前文件目录路径
FileDir = os.path.abspath(os.path.dirname(__file__))




def get_files(path):
    files =[]
    for root, dir,file in os.walk(path):
        for file_name in file:
            # 如果是csv
            if file_name.endswith('.csv'):
                complete_name = root + "/"+ file_name
                files.append([complete_name, file_name])
                # print(complete_name)
    return files

if __name__=="__main__":

    print( '***获取当前目录***')
    print( os.getcwd())
    print( os.path.abspath(os.path.dirname(__file__)))

    print( '***获取上级目录***')
    print( os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print( os.path.abspath(os.path.dirname(os.getcwd())))
    print( os.path.abspath(os.path.join(os.getcwd(), "..")))

    print( '***获取上上级目录***')
    print( os.path.abspath(os.path.join(os.getcwd(), "../..")))

