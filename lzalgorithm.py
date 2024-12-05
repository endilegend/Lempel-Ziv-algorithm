######################################
# Endi Troqe
# 12-05-2024
######################################

# Gets the unique substring to insert into the encode functions
def uniqueSubstrings(value):
    
    #gives the number representation with the unique values
    numbersRepresentation = {}
    num = 1
    i = 0

    #while loop that checks if the value is in the number represenation values
    while i < len(value):

        #if value isnt in number rep insert the value into the correct number
        if value[i] not in numbersRepresentation.values():
            numbersRepresentation[num] = value[i]
            #right pointer
            z = i

        #if the value is in the number rep values than keep increasing the value until it is not in there
        else:
            #right pointer
            z = i+1
            while z < len(value):
                rep = value[i:z+1]
                if rep not in numbersRepresentation.values():
                    numbersRepresentation[num]= rep
                    break
                z += 1
        #increment key by 1
        num += 1
        #increment i by 1 + the right pointer
        i = z + 1 
    return numbersRepresentation
        
def encode(uniqueSubstring):

    #used to get the length of the values
    values = (uniqueSubstring.values())
    #hashmap used to get the key of the values
    encoded = {1: "1", 2: "0"}
    #used to get the highest nmber in order to convert to bits
    high = 0

    #loop that is used for every key
    for i in range(3,len(values)+1):

        #x is equal to the value of the unique substring up until the last num
        x = uniqueSubstring[i][:-1]

        #if x is already in the values replace it with the key of x in uniqueSubstring and also get the high value and update if needed
        if x in uniqueSubstring.values(): 
            encoded[i] = f"{next((k for k, v in uniqueSubstring.items() if v == x), None)-1}{uniqueSubstring[i][-1:]}" 
            high = max(high, next((k for k, v in uniqueSubstring.items() if v == x)))

    high = high.bit_length()

    #covnevrts the number into binary 
    for i in range(3,len(values)+1):
        x = int((encoded[i])[:-1])
        x = f"{x:0{high}b}"

        encoded[i]= f"{x}{encoded[i][-1:]}"
    
    #joins the values
    encoded = "".join((encoded.values()))
    return encoded    
 



from PIL import Image
# Open BMP file
image = Image.open("small.bmp")
# Get pixel data in RGB format (or RGBA if it’s an alpha channel)
pixels = image.load()
# Access the pixel value at position (x, y)
pixel_value = pixels[0, 0]
x = "10"
for i in range(image.size[0]):
    for j in range(image.size[1]):
        # print(f"Pixel value at ({i}, {j}): {pixels[i,j]}")
        for color in pixels[i,j]:
            x += str(bin(color)[2:])


# print(x)
uniqueSubstring = (uniqueSubstrings(x))
encoded = (encode(uniqueSubstring))

image = Image.open("small.bmp")
# Get pixel data in RGB format (or RGBA if it’s an alpha channel)
pixels = image.load()

i = 0
row = 0
col = 0
while i + 24 < len(encoded):

    pixels[row,col] = (int(encoded[ i : i + 24][:8], 2), int(encoded[ i : i + 24][8:16], 2), int(encoded[ i : i + 24][16:], 2))
    col += 1
    if col >= image.size[1]:
        col = 0
        row += 1
    if row >= image.size[0]:
        break
    i += 24

image.save("modified_example.bmp")
