import struct

def int_to_floating_bin(MyInt, NBit=32):
    LStrReturned=[]
    if MyInt>=0:
        LStrReturned.append("0")
        for elt in bin(MyInt)[2:]:
            LStrReturned.append(elt)
    else:
        LStrReturned.append("1")
        for elt in bin(MyInt)[3:]:
            LStrReturned.append(elt)

    while len(LStrReturned)!=32:
        LStrReturned.append("0")

    StrReturned=''.join(LStrReturned)
    NewInteger=int(StrReturned,2)
    return struct.unpack('f',struct.pack('I',NewInteger))[0]




