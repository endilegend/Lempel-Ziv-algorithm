def lzAlgorithim(value):
    numbersRepresentation = {}

    num = 1
    print(value)
    for i,x in enumerate(value):
        if x not in numbersRepresentation.values():
            numbersRepresentation[num] = x
        else:
            z = i+1
            while z < len(value):
                if value[i:z+1] not in numbersRepresentation.values():
                    numbersRepresentation[num] = value[i:z+1]
                    break
                z +=1
        num += 1

    outliers = "".join([value for value in numbersRepresentation.values()])
    if len(outliers) < len(value):
        remaining = len(outliers) - len(value)
        outliers += value[remaining:]


    
    

    return numbersRepresentation
                



    



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
    (lzAlgorithim(value))


