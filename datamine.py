from os import listdir

def read_data(file_path):
    with open(file_path, "r") as f:
        f.readline()
        return f.read()
    
def read_all_data():
    data = []
    for file_name in listdir("data"):
        file_path = f"data/{file_name}"
        data.append(read_data(file_path))
    return data

def split_arr(dataArr):
    for i in range(len(dataArr)):
        dataArr[i] = dataArr[i].split("\n")
        dataArr[i].pop()
        for j in range(len(dataArr[i])):
            dataArr[i][j] = dataArr[i][j].split(",")

    return dataArr

def merge_arrs(dataArr):
    result = []
    for i in dataArr:
        for j in i:
            result.append(j)
    return result

def filter_by_product(dataArr, product):
    length = len(dataArr)
    counter = 0

    while counter < length:
        if dataArr[counter][0] != product:
            dataArr.pop(counter)
            length -= 1
        else:
            counter += 1
    return dataArr

def format_into_profits(dataArr):
    for i in range(len(dataArr)):
        price = dataArr[i].pop(1)
        numPrice = float(price[1:])
        quantity = float(dataArr[i][1])
        dailySale = f"${(numPrice * quantity):.2f}"
        dataArr[i][1] = dailySale
    return dataArr

def remove_product_field(dataArr):
    for i in range(len(dataArr)):
        dataArr[i].pop(0)
    return dataArr

def format_as_file(dataArr):
    result = ""
    for i in range(len(dataArr)):
        temp = ""
        for j in range(len(dataArr[i]) - 1):
            temp += dataArr[i][j]
            temp += ","
        temp += dataArr[i][-1]
        temp += "\n"
        result += temp
    
    return result

def write_result_to_output(result, file_path):
    with open(file_path, 'w') as f:
        f.write(result)

def main():
    dataArr = read_all_data()
    dataArr = split_arr(dataArr)
    dataArr = merge_arrs(dataArr)
    dataArr = filter_by_product(dataArr, "pink morsel")
    dataArr = format_into_profits(dataArr)
    dataArr = remove_product_field(dataArr)
    result = format_as_file(dataArr)
    write_result_to_output(result, "data/output.csv")

main()
