import nmf
from numpy import *
import models as model
data_matrix=[]
for html_data in model.html_data.objects:data_matrix.append([(index.day_high,index.date) for index in html_data.indexes])
input_matrix=matrix(reduce(lambda x,y: x[0]+y[0],data_matrix))
date_matrix=reduce(lambda x,y: x[1]+y[1],data_matrix)
print date_matrix
#v,f = nmf.factorize(input_matrix)
#print "Weights",v
#print "Features",f

