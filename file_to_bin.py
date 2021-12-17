import random

def flip(bit):
    if bit == "1":
        return "0"
    else:
        return "1"

def change(binary):
    result = ''
    for bit in binary:
        if random.random() > 0.99:
            result += flip(bit)
        else:
            result += bit

binstrs = []
print("processing")
with open("/Users/mfuchs/scm/file_to_bin/kanu.png", "rb") as f:
    ibytes = bytearray(f.read())
for byte in ibytes:
    binary = bin(byte)[2:]
    while len(binary) < 8:
        binary = "0" + binary
    print(type(binary))
    # binary = change(binary)
    binstrs.append(binary)
print(binstrs[:10])
ibytes2 = bytearray([int(binstr, 2) for binstr in binstrs])
print(ibytes[:10])
print(ibytes2[:10])

# write binary data to file
with open("/Users/mfuchs/scm/file_to_bin/binarypic.txt", "w") as f:
    f.write(''.join(binstrs))

# write file copy from bytes
with open("/Users/mfuchs/scm/file_to_bin/copy.png", "wb") as f:
    f.write(ibytes2)
    print("ok")

print("done")
