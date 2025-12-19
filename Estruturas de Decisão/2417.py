Cv, Ce, Cs, Fv, Fe, Fs = input().split()
Cv = int(Cv)
Ce = int(Ce)
Cs = int(Cs)
Fv = int(Fv)
Fe = int(Fe)
Fs = int(Fs)
 
if Cv*3 + Ce*1 > Fv*3 + Fe*1:
    print (f'C')

elif Cv*3 + Ce*1 == Fv*3 + Fe*1 and Cs == Fs:
    print (f'=')
    
elif Cv*3 + Ce*1 == Fv*3 + Fe*1 and Cs > Fs:
    print (f'C')
    
elif Cv*3 + Ce*1 == Fv*3 + Fe*1 and Cs < Fs:
    print (f'F')
    
elif Cv*3 + Ce*1 < Fv*3 + Fe*1:
    print (f'F')
