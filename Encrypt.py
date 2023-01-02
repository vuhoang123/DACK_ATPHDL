import time
# mã hóa một đoạn text


def encrypt(plaintext: bytes, key: bytes):
    now = time.time()
    ltm = time.localtime(now)
    keylen = len(key)
    for i, k in enumerate(range(0, len(plaintext), keylen)):
        if k == (ltm.tm_min % keylen):
            k = 0

        plaintext[i] ^= key[k]

# Giải mã một đoạn text


def decrypt(ciphertext: bytes, key: bytes):
    encrypt(ciphertext, key)

# Đọc file


def read_file(in_file_name: str) -> bytes:
    with open(in_file_name + ".txt", "rb") as file_in:
        content = file_in.read()
    return content

# Ghi file


def write_file(out_file_name: str, content: bytes):
    with open(out_file_name + ".txt", "wb") as file_out:
        file_out.write(content)


def file_encrypt(in_file_name: str, key: bytes):
    content = read_file(in_file_name)
    encrypt(content, key)

    out_file_name = in_file_name + "_Encrypt"
    write_file(out_file_name, content)
    print("\n\tMA HOA THANH CONG")


def file_decrypt(in_file_name: str, key: bytes):
    content = read_file(in_file_name)
    decrypt(content, key)

    out_file_name = in_file_name + "_Decrypt"
    write_file(out_file_name, content)
    print("\n\tGIAI MA THANH CONG")
