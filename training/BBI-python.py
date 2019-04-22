import pandas as pd


#c1,c6
file=pd.read_csv('Housing-LR.csv')
print(file.head(0))
a=file.bedrooms#c2
b=file.bathrms#c3
c=file.stories#c4
d=file.gashw#c8
c1=file.lotsize
c5=file.driveway
c7=file.fullbase
c9=file.airco
c11=file.prefarea
c6=file.gardenarea
c12=file.price
c10=file.garagepl
print ("==========================================")
print(a.unique())
print(b.unique())
print(c.unique())
print(d.unique())

print ("==========================================")
print(len(a.unique()))
print(len(b.unique()))
print(len(c.unique()))
print(len(d.unique()))

print ("==========================================")

print((a.value_counts()))
print((b.value_counts()))
print((c.value_counts()))
print((d.value_counts()))


print ("==========================================")

print(a.min(), a.max(), a.mean(),a.std(),a.var())
print(b.min(), b.max(), b.mean(),b.std(),b.var())
print(c.min(), c.max(), c.mean(),c.std(),c.var())

print ("==========================================")

d.replace( [ 'yes' , 'no'] , [1,0] , inplace = True )

print ("==========================================")
#m1=c1.mean()
#c1=c1/m1
#m6=c6.mean()
#c6=c6/m6
#m12=c12.mean()
#c12=c12/m12

print ("==========================================")
print(c1.min(), c1.max(), c1.mean(),c1.std(),c1.var())
print(c6.min(), c6.max(), c6.mean(),c6.std(),c6.var())
print(c12.min(), c12.max(), c12.mean(),c12.std(),c12.var())

print ("==========================================")

#number_of_all_elemnts=len(c10)
#counts = c10.value_counts().to_dict()
#number_of_zeros=counts[0]
#new_mean=c10.sum()/(number_of_all_elemnts-number_of_zeros)
#c10.replace( [0] , new_mean , inplace = True )
#print(new_mean)

print ("==========================================")
c5.replace( [ 'yes' , 'no'] , [1,0] , inplace = True )
c7.replace( [ 'yes' , 'no'] , [1,0] , inplace = True )
c9.replace( [ 'yes' , 'no'] , [1,0] , inplace = True )
c11.replace( [ 'yes' , 'no'] , [1,0] , inplace = True )
print ("==========================================")

min=c1.min()
max=c1.max()
c1=(c1-min)/(max-min)
min=c6.min()
max=c6.max()
c6=(c6-min)/(max-min)

print ("==========================================")


file.lotsize=c1
file.gardenarea=c6


file.to_csv('karam.csv')