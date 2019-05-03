class Sol:
    def sumII(self,array,goal):
        left=-0
        right=-1
        while(array[left]<array[right]):
            if array[left]+array[right]==goal:
                p1=array.index(array[left])
                p2=array.index(array[right])
                p1+=1
                p2+=1
                print(p1, p2)
                break
            elif(array[left]+array[right]<goal):
                left+=1
            else:
                right-=1
        return

if __name__ == '__main__':
    array=[1,2,7,11]
    goal=9
    p1=Sol()
    p1.sumII(array,goal)
