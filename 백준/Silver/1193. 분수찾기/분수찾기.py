n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line
    
gap = end - n
if(line%2 == 0):
    top = line - gap
    bottom = gap + 1
else:
    top = gap + 1
    bottom = line - gap
    
print("%d/%d"%(top,bottom))