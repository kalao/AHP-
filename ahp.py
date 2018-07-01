mport numpy as np
#http://blog.163.com/zhoulili1987619@126/blog/static/3530820120169194260252/
class ahp:
    def __init__(self):
            pass

	        def calvector(self,Bn):
		        ans=0
			        ans1=0
				        result=np.zeros((1,len(Bn[0])))

					        for i in range(len(Bn)):
						            for j in range(len(Bn[i])):
							                    ans=ans+Bn[i][j]
									            for k in range(len(Bn)):
										                ans1=0
												            for j in range(len(Bn[k])):
													                    ans1=ans1+Bn[k][j]

															                result[0][k]=ans1/ans
																	        return result
																		    def calD(self):
																		            pass
																			    t=ahp()
																			    A=np.array([[1,2,7,5,5],[1/2,1,4,3,3],[1/7,1/4,1,1/2,1/3],[1/5,1/3,2,1,1],[1/5,1/3,3,1,1]])
																			    vec=t.calvector(A)
																			    #print(vec)
																			    B1=np.array([[1,1/3,1/8],[3,1,1/3],[8,3,1]])
																			    B2=np.array([[1,2,5],[1/2,1,2],[1/5,1/2,1]])
																			    B3=np.array([[1,1,3],[1,1,3],[1/3,1/3,1]])
																			    B4=np.array([[1,3,4],[1/3,1,1],[1/4,1,1]])
																			    B5=np.array([[1,4,1/4],[1,1,1/4],[4,1,1]])
																			    vec1=t.calvector(B1)
																			    #print(vec1)
																			    vec2=t.calvector(B2)
																			    #print(vec2)
																			    vec3=t.calvector(B3)
																			    #print(vec3)
																			    vec4=t.calvector(B4)
																			    #print(vec4)
																			    vec5=t.calvector(B5)
																			    #print(vec5)
																			    y=np.zeros((3,5))
																			    for i in range(3):
																			       for j in range(5):
																			              y[i][0] = vec1[0][i]
																				             y[i][1] = vec2[0][i]
																					            y[i][2] = vec3[0][i]
																						           y[i][3] = vec4[0][i]
																							          y[i][4] = vec5[0][i]
																								  #print(y)
																								  print(np.dot(y,vec.T))
																								  #y3>y1>y2
