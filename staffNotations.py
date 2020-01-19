import sys
from PIL import Image
d=[]
d = dict([
    (88,'C8'),(76,'C7'),(64,'C6'),(52,'C5'),(40,'C4'),(28,'C3'),(16,'C2'),
    (87,'B7'),(75,'B6'),(63,'B5'),(51,'B4'),(39,'B3'),(27,'B2'),
    (85,'A7'),(73,'A6'),(61,'A5'),(49,'A4'),(37,'A3'),(25,'A2'),
    (83,'G7'),(71,'G6'),(59,'G5'),(47,'G4'),(35,'G3'),(23,'G2'),
    (81,'F7'),(69,'F6'),(57,'F5'),(45,'F4'),(33,'F3'),(21,'F2'),
    (80,'E7'),(68,'E6'),(56,'E5'),(44,'E4'),(32,'E3'),(20,'E2'),
    (78,'D7'),(66,'D6'),(54,'D5'),(42,'D4'),(30,'D3'),(18,'D2'),

])

l=[]
l1=[]
l2=['intro.png']
n=int(input("size of array?"))
for x in range(0,n):
    e=int(input("element daaalo"))
    l.append(e)
for x in l :
    if x in d:
        print(d[x])
        l1.append(d[x])
print(l)
print(l1)        
for x in l1:
    l2.append(x[0].lower()+".png")
print(l2)  
  
images = [Image.open(x) for x in l2]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

new_im.save('test.jpg')
