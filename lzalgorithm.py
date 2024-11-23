def uniqueSubstrings(value):
    
    numbersRepresentation = {}

    num = 1
    i = 0
    while i < len(value):
        if value[i] not in numbersRepresentation.values():
            numbersRepresentation[num] = value[i]
            z = i

        else:
            z = i+1
            while z < len(value):
                rep = value[i:z+1]
                if rep not in numbersRepresentation.values():
                    numbersRepresentation[num]= rep
                    break
                z += 1
        num+=1
        i = z +1 
    return numbersRepresentation

def encode(uniqueSubstring):
    
    values = list(uniqueSubstring.values())
    encoded = {1: "1", 2: "0"}
    high = 0

    for i in range(3,len(values)+1):
        x = (uniqueSubstring[i])[:-1]
        if x in values: 
            encoded[i] = f"{values.index(x)+1}{uniqueSubstring[i][-1:]}" 
            high = max(high, values.index(x)+1)

    # got the .bit_length() from stack overflow
    high = high.bit_length()

    for i in range(3,len(values)+1):
        x = int((encoded[i])[:-1])
        #got how to get the minimum bits from ChatGPT
        x = f"{x:0{high}b}"

        encoded[i]= f"{x}{encoded[i][-1:]}"

    encoded = "".join(list(encoded.values()))
    
    return encoded     


from PIL import Image
# Open BMP file
image = Image.open("example.bmp")
# Get pixel data in RGB format (or RGBA if it’s an alpha channel)
pixels = image.load()
# Access the pixel value at position (x, y)
pixel_value = pixels[0, 0]

values = {}
for i in range(image.size[0]):
    for j in range(image.size[1]):

        x = f"{pixels[i,j]}"
        x =x.strip('() ')
        x = x.split(",")
        p = []
        for i in x:
            i = int(i)
            p.append(f"10{format(i,'b')}")
            
        values[i,j] = "".join(p)

for key,value in values.items():
    uniqueSubstring = (uniqueSubstrings(value))
    print(encode(uniqueSubstring))

