# Ghi vao file
def write_to_file(file_name: str, content: str):
    with open(file_name + ".txt", "w") as file:
        file.write(content)

def read_from_file(filename: str) -> str:
    content = ""
    with open(filename + ".txt", "r") as file:
        if file.mode != "r":
            print("Error: file not opened.")
            return content

        for line in file:
            content += line

    return content

#chia noi dung thanh nhieu phan
def divided_content(content: str, count_f: int) -> list:
    list_content = []

    # khich thuoc tung file
    size = len(content) // (count_f - 1)
    
    k = 0
    # lay ra n - 1 doan du lieu
    for i in range(count_f - 1):
        list_content.append(content[k:k+size])
        k += size

    # kiem tra neu con thi ghi vao file tiep 
    if k < len(content):
        list_content.append(content[k:])

    return list_content

# tao ten file
def create_name_file(file_name: str, num: int) -> int:
    result = 0

    # bien doi 1 ki tu thanh 1 ki tu khac
    # cong thuc: a+2num mod 122
    for i in range(len(file_name)):
        result = ((ord(file_name[i]) * num*2) % 122)

    return result

# doc file
def divided(file_name: str, count_f: int):
    content = read_from_file(file_name)
    print(content)
    # lay noi dung file
    list_content = divided_content(content, count_f)

    for i in range(2, count_f+2):
        filename_new = str(create_name_file(file_name, i))
        write_to_file(filename_new, list_content[i-2])

# gop fil laij
def join(file_name: str, count_f: int):
    content = ""
    list_content = []
    l_name_file = []
    filename_new = ""

    for i in range(2, count_f+2):
        l_name_file.append(str(create_name_file(file_name, i)))

    for i in range(count_f):
        content += read_from_file(l_name_file[i])

    write_to_file(file_name + "Join", content)
