ene_name=str("ene")
TIMESTEP=4
##
ene_file=open(ene_name, 'r')
energies=list()
for i in ene_file:
	energies.append(i)
ene_file.close()
##
for l in energies:
    time_text=str()
    a=str()
    for c in range(10):
        a+=l[c]
    time_ps=str(round(float(a)*2.418884254E-5*TIMESTEP,5))
    time_text+=" "*(10-len(time_ps))+time_ps
    print(l.replace(a, time_text).replace('\n',''))
