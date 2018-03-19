#        A     B     C
List1=[[0,3],[0,3],[3,6]]
List2=[[0,3],[3,0],[3,6]]

def CountTriangleArea(List):
    for x in range(3):
        A=List[0]
        B=List[1]
        C=List[2]
        Area=0.5*abs((((B[0]-A[0])*(C[1]-A[1]))-((B[1]-A[1])*(C[0]-A[0]))))
        if(Area!=0):
            return Area
        else:
            print("Triangle doesn't exist")
            return -1

			
			
			
print("Area: ",CountTriangleArea(List2))



