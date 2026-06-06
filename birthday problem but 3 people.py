import math
"""
the method applied for the pair match isn't going to work if we want to know the probability of 
having 3 people at the function with the same birthday.

choosing 3 out of N group : NC3
choice of a random day For the 3 to match : 365/365 * 1/365*1/365 #a
the remaining N-3 's birthdays : (1/365)^N-3 * (factorial(365) /factorial (365 -N-3)) #b
then we multilpy the a and b to get the answer


"""
def calculating_the_probability(N):
    n_choose_3 = math.comb(N, 3) #how many combinations we can make

    three_matching = 1 / (365 ** 2)

    the_rest = (
        math.factorial(364)
        /
        (math.factorial(367 - N) * (365 ** (N - 3)))
    )
    #we multiply all to get the probablity of all of them happening together 

    return n_choose_3 * three_matching * the_rest



# now let's test it with the n = 23 from the last problem

print(calculating_the_probability(23)) # the answer is 0.0073 which is really small compared to having 2 people 

