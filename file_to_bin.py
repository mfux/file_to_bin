import random

def flip(bit):
    result = bit
    if bit == "1":
        result = "0"
    else:
        result = "1"
    return result

def change(binary):
    result = ""
    for bit in binary:
        if random.random() < 0.9999:
            result += bit
        else:
            result += flip(binary)
    return result

binstrs = []
print("processing")
with open("/Users/mfuchs/Documents/file_to_bin/kanu.png", "rb") as f:
    ibytes = bytearray(f.read())
for byte in ibytes:
    binary = bin(byte)[2:]
    while len(binary) < 8:
        binary = "0" + binary
    binary = change(binary)
    binstrs.append(binary)
print(binstrs[:10])
ibytes2 = bytearray([int(binstr, 2) for binstr in binstrs])
print(ibytes[:10])
print(ibytes2[:10])

# write binary data to file
with open("/Users/mfuchs/Documents/file_to_bin/binarypic.txt", "w") as f:
    f.write(''.join(binstrs))

# write file copy from bytes
with open("/Users/mfuchs/Documents/file_to_bin/copy.png", "wb") as f:
    f.write(ibytes2)
    print("ok")

print("done")
