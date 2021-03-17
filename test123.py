
dotakeys = open('/home/vovucho/.steam/steam/userdata/323343420/570/remote/cfg/dotakeys_personal.lst', 'r+')
a = dotakeys.readlines()
b = a.index('\t\t\t"Key"\t\t"A"\n')
if b == 65:
    a.pop(73)
    a.insert(73, '\t\t\t"Key"\t\t"A"\n')
    a.pop(65)
    a.insert(65, '\t\t\t"Key"\t\t"S"\n')
else:
    a.pop(65)
    a.insert(65, '\t\t\t"Key"\t\t"A"\n')
    a.pop(73)
    a.insert(73, '\t\t\t"Key"\t\t"S"\n')
listt = a
dotakeys.close()


dotakeys = open('/home/vovucho/.steam/steam/userdata/323343420/570/remote/cfg/dotakeys_personal.lst', 'w')
dotakeys.writelines(listt)
dotakeys.close()

#'\t\t\t"Key"\t\t"S"\n' - 65
#'\t\t\t"Key"\t\t"A"\n' - 73