import glob

desiredfolder = 'D:\\ebirdsounds\\sounds\\raw\\'
desiredfolder = 'C:\\Users\\joeld\\Desktop\\Python\\ebird\\sounds\\'

files = glob.glob(f"{desiredfolder}*.wav")
files = [x[len(desiredfolder):] for x in files]

names = [x.replace('_','(')[:-4]+')' for x in files]

filesanki = [f'[sounds:{x}]' for x in files]
out = [[x,filesanki[i]] for i,x in enumerate(names)]
out2 = [';'.join(x) for x in out]
out3 = '\n'.join(out2)


print(out3)

with open("out.csv",'w') as f:
    f.write(out3)
