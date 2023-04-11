from struct import pack, unpack
from bitstream import BitStream
from io import BytesIO
import sys

#Global variables, easier to pass around
#.bss
left9 = [0] * 0x400 #u16
right9 = [0] * 0x400 #u16
left12 = [0] * 0x10000 #u16
right12 = [0] * 0x10000 #u16
stack = [0] * 0x100 #u32
#.sbss
bitlen = [0, 0] #s32
ccnt = [0, 0] #s32
wptr = [0, 0] #s32
bitcode = [0, 0] #u32

#make this global so it's easier to pass around
stream12 = BitStream()

#stub off of getbitsc so that we can cache all 12-bit data and modify it
def bitstream_write(size, slot, data):
    if size != 32 and slot == 1: #skip initial 32-bit fetch, make sure 12-bit table
        #ashcompress/Wii Menu uses 11-bits, MPR uses 15 bits, add 4 bits to the start
        if size == 11:
            stream12.write([False, False, False, False], bool)
        #write each bit into the stream for writing
        for i in range(size-1, -1, -1):
            stream12.write((data >> i) & 1, bool)
    return data #makes getbitsc cleaner

#only modifications from stock decompression is bitstream_write
def getbitsc(src, size, slot):
    global bitlen, wptr, bitcode, stream12
    src.seek(wptr[slot])
    m = bitlen[slot]
    g = bitcode[slot]
    #check if we're out of bounds (num bits already read + request is more than the 32 max, load more)
    if m + size > 32:
        j = unpack(">I", src.read(4))[0]
        wptr[slot] += 4
        bitlen[slot] = (m + size - 32) & 0xFFFFFFFF;
        bitcode[slot] = (j << (m + size - 32)) & 0xFFFFFFFF
        return bitstream_write(size, slot, (g >> (32 - size)) | (j >> (64 - size - m)))
    #if it's exactly the number of bits we have on hand, simply return the rest and load 32 more
    elif m + size == 32:
        wptr[slot] += 4
        bitlen[slot] = 0
        bitcode[slot] = unpack(">I", src.read(4))[0]
        return bitstream_write(size, slot, g >> (32 - size))
    #return only what's requested
    else:
        bitlen[slot] = (m + size) & 0xFFFFFFFF
        bitcode[slot] = (g << size) & 0xFFFFFFFF
        return bitstream_write(size, slot, g >> (32 - size))

#only called once, constructs the tree in a loop, and returns the root node for traversal
def readtree9(src):
    global ccnt, stack, left9, right9

    sp = 0
    j = ccnt[0]
    m = ccnt[0]
    while True:
        if getbitsc(src, 1, 0):
            #use the stack so we know when to go left or right
            stack[sp] = (j | 0x80000000) & 0xFFFFFFFF
            stack[sp + 1] = (j | 0x40000000) & 0xFFFFFFFF
            j += 1
            m += 1
            sp += 2
        else:
            #get the leaf data
            z = getbitsc(src, 9, 0)
            while sp:
                sp -= 1
                f = stack[sp]
                if not f & 0x80000000:
                    left9[f & 0x3FFFFFFF] = (z & 0xFFFF)
                    j = m
                    break #we're not done yet, continue reading
                else:
                    right9[f & 0x3FFFFFFF] = (z & 0xFFFF)
                    z = f & 0x3FFFFFFF
                    if sp == 0: #only once we've reached the root node do we return
                        return z

#same as above, except we read 11 bits (15 for MPR)
def readtree12(src):
    global ccnt, stack, left12, right12

    sp = 0
    j = ccnt[1]
    m = ccnt[1]
    while True:
        if getbitsc(src, 1, 1):
            stack[sp] = (j | 0x80000000) & 0xFFFFFFFF
            stack[sp + 1] = (j | 0x40000000) & 0xFFFFFFFF
            j += 1
            m += 1
            sp += 2
        else:
            z = getbitsc(src, 11, 1)
            while sp:
                sp -= 1
                f = stack[sp]
                if not f & 0x80000000:
                    left12[f & 0x3FFFFFFF] = (z & 0xFFFF)
                    j = m
                    break
                else:
                    right12[f & 0x3FFFFFFF] = (z & 0xFFFF)
                    z = f & 0x3FFFFFFF
                    if sp == 0:
                        return z

if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        #Need to modify input so we don't try to read out of bounds by appending 4 extra bytes
        input_data = BytesIO(f.read())
        input_data.seek(0, 2)
        input_data.write(b"\0" * 4) #we'll calculate the correct number once we write a corrected file
        input_data.seek(0)

    #read the 12-byte header, "ASH0", decompressed size, and offset to 12-bit data
    header = unpack(">4s2I", input_data.read(12))
    out_size = header[1]
    
    #here we grab the offset, and store all data before for writing
    offset12 = header[2]
    input_data.seek(0)
    initial_data = input_data.read(offset12)
    input_data.seek(12)
    
    wptr = [12, offset12]
    bitlen = [0, 0]
    ccnt = [0x200, 0x8000] #remaining allocation for each tree
    #prefetch initial data
    getbitsc(input_data, 32, 0)
    getbitsc(input_data, 32, 1)
    #build the 9-bit and 12-bit trees
    root9 = readtree9(input_data)
    root12 = readtree12(input_data)
    #now we reconstruct the original data
    q = 0
    while q < out_size:
        j = root9
        while j >= 0x200:
            if getbitsc(input_data, 1, 0):
                j = right9[j]
            else:
                j = left9[j]
        if j < 0x100:
            q += 1
        else:
            i = root12
            while i >= 0x8000:
                if getbitsc(input_data, 1, 1):
                    i = right12[i]
                else:
                    i = left12[i]
            j -= 253
            i = q - i - 1
            while j > 0:
                j -= 1
                q += 1
                i += 1
    print(q)

    with open(sys.argv[1], "wb") as o:
        o.write(initial_data) #write everything before the 12-bit data we needed to modify
        padding = (len(stream12) + 7) & ~7
        stream12.write([False] * (padding - len(stream12)), bool) #pad stream out to 8 bits
        size12 = len(stream12) // 8 #grab number of bytes
        o.write(stream12.read(bytes))
        padding = (size12 + 3) & ~3
        o.write(b"\0" * (padding - size12)) #pad it out to 4 bytes so we don't out-of-bounds in getbitsc
        
            
