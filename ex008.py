medida = float(input('Digite uma distancia em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m, corresponde a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(medida, km, hm, dam, dm, cm, mm))
