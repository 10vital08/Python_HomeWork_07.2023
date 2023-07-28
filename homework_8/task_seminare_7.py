# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle

def pic_in_csv(f_name):
    myFileArr = []
    with open(f_name, "r") as file:
        while res := file.readline():
            myFileArr.append(res.replace("\n", "").split(','))
        file.close()

        result = []
        for row in range(len(myFileArr)):
            obj = {}
            if row != 0:
                for i in range(len(myFileArr[0])):
                    obj[myFileArr[0][i]] = myFileArr[row][i]
                result.append(obj)

        for row in result:
            print(pickle.dumps(row))

if __name__ == '__main__':
    pic_in_csv('new_user.csv')