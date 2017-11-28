#!/usr/bin/env python3
import numpy
import pdb
import hcluster
list1 = [[292, 1203, 32, 17, 917], [830, 1079, 494], [46, 565, 262, 74, 21, 17, 539], [1050, 58, 52], [1079, 494], [16, 52], [16, 17], [29, 52], [405, 958, 292, 345, 97, 58, 17, 1061, 4, 494], [94, 446, 32, 1592, 194, 9392, 9, 687, 1540, 3029, 32, 52], [4687, 1741, 97, 32, 17, 238], [14, 15, 21, 52], [292, 1203, 32, 17, 917], [491, 48, 494], [806, 17], [1622, 16, 17], [16, 17], [46, 350, 97, 58, 494], [16, 17, 127, 2954], [379, 529, 15, 1516, 1531, 793, 17, 284], [29, 18708, 2687, 44, 1060, 17]]

length = len(list1)

jc_matrix = numpy.zeros((length,length) )



for i in range(length):
   for j in range(i+1):
         if i == j:
             jc_matrix[i][j] = -1
         else:
             jc_matrix[i][j] = round(float(len(set(list1[i]) & set(list1[j])))/float(len(set(list1[i]) | set( list1[j]))),3) #round it 3 dec places


print jc_matrix  
numpy.savetxt('jaccard.txt',jc_matrix, delimiter=" ", fmt="%s" )       

tree = hcluster.hcluster(jc_matrix,list1)
