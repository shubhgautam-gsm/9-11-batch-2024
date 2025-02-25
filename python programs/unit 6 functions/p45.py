#A random bytearray          65 66 67 
randomByteArray = bytearray('ABC', 'utf-8')
randomByteArray2 = bytearray('ग ', 'utf-8')
# randomByteArray2 = bytearray('a', 'ascii')


mv = memoryview(randomByteArray)
mv2 = memoryview(randomByteArray2)

# access the memory view's zeroth index
print(mv[0])
print(mv2[0])

# It create byte from memory view
print(bytes(mv[0:2]))
# It create list from memory view
print(list(mv[0:3]))
