x1,y1,x2,y2,x3,y3 = map(int, input().split())

if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
    print(-1.0)
else: 
    case1 = ((x1-x2)**2+(y1-y2)**2)**(1/2) + ((x2-x3)**2+(y2-y3)**2)**(1/2)
    case2 = ((x1-x2)**2+(y1-y2)**2)**(1/2) + ((x1-x3)**2+(y1-y3)**2)**(1/2)
    case3 = ((x1-x3)**2+(y1-y3)**2)**(1/2) + ((x2-x3)**2+(y2-y3)**2)**(1/2)
    print(2*(max(case1, case2, case3)-min(case1, case2, case3)))
