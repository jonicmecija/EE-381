'''
EE 381
Project 1
Jonic Mecija
014467048
Start Date: 8/26/19
End Date: 8/28/19
'''


def main():

    def data():
        nums = []
        x = True
        print("You will be asked to enter a nonnegative integers.")
        print("When you want to stop enter a letter.")

        while(x):
            try: 
                num = int(input("Enter a nonnegative integer."))
                nums.append(num)
            except ValueError:
                print("Input has been stopped ")
                print("\n")
                x = False

        print("You entered these numbers.", nums)
        return nums

    def mean(V):
        s = sum(V) # Sum of inputted numbers
        N = len(V) # Number of numbers entered
        mean = s/N 
        print("The mean of the numbers inputted is", mean)


    def median(V):
        N = len(V) # number of numbers entered
        V.sort() # sorting from small to large 

        # is the length even or odd

        if N % 2 == 0: # even
            m1 = N/2
            m2 = (N/2) +1

            m1 = int(m1)
            m2 = int(m2)

            m1 = m1 - 1
            m2 = m2 - 1

            median = (V[m1] + V[m2])/2
        else:
            m = (N+1)/2
            m = int(m) - 1
            median = V[m]
        
        print("The median of the numbers inputted is ", median)

    def mode(V):
        from collections import Counter

        c = Counter(V) #creates tuples of elements in the list (not mutable)
        print(c)
        freq = c.most_common() #most common method
        print(freq)
        max_occur = freq[0][1] #second element of tples will be max assigned

        if max_occur != 1:
            modes = [] #empty list 

            for m in freq:
                if m[1] == max_occur: # second position in tuple equal to max_occur
                    modes.append(m[0])
            
            print("The mode(s) are: ", modes)

        else:
            print("There is no mode.")
    V = data()
    mean(V)
    median(V)
    mode(V)

main()

'''
    #find sum
    numSum = 0
    for x in nums:
        numSum = x + numSum

    #find median
    nums.sort()
    middle = 0
    # even number of elements
    if len(nums) % 2 == 0:
        print("")
    else:
        middle = len(nums)/2

    print("You entered these numbers: ", nums)
    print(len(nums))
    print("Mean: ", numSum/len(nums))
    print("Median: ", ((nums[middle+1] + nums[middle-1])/2))
    print("Mode: ")
'''
