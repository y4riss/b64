import sys

# creating base64 table index
A_Z = [chr(i) for i in range(65,91)]
a_z = [chr(i) for i in range(97,123)]
zero_nine = [chr(i) for i in range(48,58)]
additional_chars = ['+','/']
base64_index_table = A_Z + a_z + zero_nine + additional_chars

# binary to decimal custom function
def bin_to_int(byte):
        #110101
        result = 0
        for i in range(0,len(byte)):
            result += int(byte[len(byte) - 1 - i]) * pow(2 ,i)
        return result

def b64_encode(word):

    # converting the word into its binary format
    binary = []
    for c in word:
        binary.append(bin(ord(c)).split("b")[-1].rjust(8,'0'))

    binary = "".join(binary)

    # splitting the binary format into chunks of 6 bits
    new_word = []

    while len(binary):
        new_word.append(binary[0:6])
        binary = binary[6:]

    # adding padding to the last elem
    new_word[-1] = new_word[-1].ljust(6, '0')

 
    # encrypting the text
    result = ""
    for byte in new_word:
        result += base64_index_table[bin_to_int(byte)]

    # adding padding of "="
    def get_multiple_of_4(num):

        while num % 4 != 0:
            num += 1
        return num
    result = result.ljust(get_multiple_of_4(len(result)),'=')
    return result


def b64_decode(word):

    #stripping away '='
    word = word.split("=")[0]

    #find index of each character in b64_index_table
    indexes = []
    for c in word:
        indexes.append(base64_index_table.index(c))

    # index to binary ( 6 bits)
    binary = []
    for i in indexes:
        binary.append(bin(i).split("b")[-1].rjust(6,'0'))

    binary = "".join(binary)
    # form group of 8 bits
    new_word = []
    while len(binary):
        new_word.append(binary[0:8])
        binary = binary[8:]

    # transform each byte to its ascii representation
    result = ""
    for c in new_word:
        result += chr(bin_to_int(c))
    return result

#python b64.py 
if __name__ == '__main__':
    
    len_args = len(sys.argv)
    if (len_args != 3):
        print(f"[] Usage : python {sys.argv[0]} <string> (-d | -e )")
        exit(0)
    option = sys.argv[2]
    if (option != '-d' and option != '-e'):
        print(f"[] Usage : python {sys.argv[0]} <string> (-d | -e )")
        exit(0)

    word = sys.argv[1]
    if (option == '-d'):
        print(f"[+] {word} ---> {b64_decode(word)}")
    else:
        print(f"[+] {word} ---> {b64_encode(word)}")
                                 