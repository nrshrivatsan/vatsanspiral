import Image, ImageFont, ImageDraw
import sys

primeColor = "black"

count = 0

if sys.argv and sys.argv[1] and sys.argv[1].isdigit():
	count = int(sys.argv[1])
	
im = Image.new('RGB', (count,count), (255,255,255))
dr = ImageDraw.Draw(im)

data = [ [ 0 for i in xrange(count) ] for i in xrange(count)  ]

with open(str(count)+".txt") as f:
	lines = f.readlines()
for line in lines:
	x = lines.index(line)
	line = line.replace(" ","")
	line = line.replace("\n","")
	# print line
	ints = [ int(i) for i in line ]
	# print ints
	y = -1
	for c in line:
		y+=1
		# print y
		if c.isdigit():
			data[x][y] = int(c)
	
			# print c, x, y
i = long(-1)
for d in data:
	i+=1
	j=long(-1)
	# print d
	for val in d:
		j+=1
		if data[i][j] == 1 :
			dr.rectangle(((i,j),(i+1,j+1)), fill=primeColor)
		else:
			dr.rectangle(((i,j),(i+1,j+1)), fill="white")		

# for i in range(len(data)):		
# 	for j in range(i):			
# 		if j % 3 == 0:
# 			data[i][j] = 1

# for i in range(len(data)):		
# 	for j in range(i):
# 		if data[i][j] == 1:
# 			dr.rectangle(((i,j),(i+1,j+1)), fill="black")		

im.save(str(count)+"_"+primeColor+".png")