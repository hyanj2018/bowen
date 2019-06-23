#定义一个读取txt文件的函数
def  read_data():
    datas = []
    with  open(r"E:\PycharmProjects\diesheng\data\data_1.txt","r") as fb:
        d = fb.readlines()
        for i in d:
            datas.append(i.replace("\n","").split(","))
    return  datas
read_data()