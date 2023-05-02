in_list=list()
in_read=open('ttotshort.in', 'r')
in_name=in_read.readline().replace('\n', '')
in_atoms=int(in_read.readline())

for i in in_read:
	if i!= '\n':
		in_list.append(int(i.replace('\n','')))
in_list.sort()
out_atoms=len(in_list)
in_read.close()

i_long=open(in_name,'r')
o_short=open(in_name+'short','w')
o_short.write('')
o_short.close()
o_short=open(in_name+'short','a')

i_list=list()
for i in i_long:
        i_list.append(i)
steps=len(i_list)/(in_atoms+2)
#print ('N of steps  '+str(steps))

for i in range(int(steps)):
        o_short.write(' '*9+str(out_atoms)+'\n'*2)
        for j in in_list:
                o_short.write(i_list[i*(in_atoms+2)+j+1])

i_long.close()
o_short.close()
