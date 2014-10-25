def countSetBits(n):
    count = 0;
    while (n):

      n &= (n-1) ;
      count+=1;

    return count;

def generate_num_ones():
  result = []
  for x in range(0, 65537):
    result.append(countSetBits(x))
  return result


l = generate_num_ones()
#print l
stringlen = input()

if(stringlen%16!=0):
  padding = 16-(stringlen%16)
else:
  padding = 0

stringlen = stringlen + padding

inputstring = raw_input()
padstring = ''
for x in range(0, padding):
  padstring+='0'

inputstring = padstring+inputstring
count = 0
for i in range(0, stringlen, 16):
  count += l[int(inputstring[i:i+16], 2)]

print count
#print int(inputstring, 2)
