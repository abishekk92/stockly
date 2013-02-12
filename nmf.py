from numpy import *

def difcost(a,b):
	dif=0
	for i in range(shape(a)[0]):
		for j in range(shape(a)[1]):
			diff+=pow(a[i,j]-b[i,j],2)
	return dif

def factorize(input_matrix,pc=10,iter=50):
	ic,fc=shape(input_matrix)[0],shape(input_matrix)[1]
	#initiliazing with random weights
	weight=matrix([[random.random() for j in xrange(pc)] for i in xrange(ic)])
	features=matrix([[random.random() for j in xrange(fc)] for i in xrange(pc)])
	
	#calculate to max with given iter
	for i in xrange(iter):
		upper_bound_matrix=weight*features
		#calculates the distance 
		cost=difcost(input_matrix,upper_bound_matrix)
		if i%10==0: print cost 
		
		if cost==0: break #fully factorized
		#multiplicative update of both feature and weight matrix until the cost is 0
		t_weight_input_matrix=(transpose(weight)*input_matrix)
		t_weight_upper_bound=(transpose(weight)*weight*features)
		features=matrix(array(features)*array(t_weight_input_matrix)/array(t_weight_upper_bound))

		input_matrix_t_features=(v*transpose(features))
		upper_bound_t_features=(weight*features*transpose(features))
		weight=matrix(array(weights)*array(input_matrix_t_features)/array(upper_bound_t_features))

	return weight,features





