import random
import math


def generater_random_birthdays():
    """
  For the sake of simplicity, we will assign a number to each day of the year, with the first day
    represented by 1 and the last day represented by 365, ignoring leap years.

  We should also mention that, in the real world, the probability of being born on each day is not 
   exactly (1/365). Birth rates can vary due to seasons, holidays, and other social factors.

 However, for the sake of simplicity, we will assume that the probability of being born on any given day 
 is equal, so (P(\text{each day}) = 1/365).


    """
    birthday = random.randint(1,356)
    return birthday


#now we need to calculate the probability of collision 

def probability_of_birthday_collision(n):
    probability_not_colliding = (
        math.factorial(365)
        / (math.factorial(365 - n) * (365 ** n))
    )
    return 1 - probability_not_colliding


# now let's test it and see when it starts to be a 50-50 chance of 2 people having the same birthday


for i in range(50):
    print(f"{i} :  p = {probability_of_birthday_collision(i)}")
    if probability_of_birthday_collision(i) >= 0.50:
        break
         

# now we can test it by randomly generating a group of 23 and giving them random birthdays


def sim_birthday_problem(n):
    birthdays = [generater_random_birthdays() for i in range(n)]
    count_birthdays = {}

    for birthday in birthdays:
        if birthday not in count_birthdays:
            count_birthdays[birthday] = 1
        else :
            return True

# now let's calculate basice probablity 
def basic_probablity_testing (n):
    we_have_a_match = []
    for i in range(1000):
        result =sim_birthday_problem(n)
        we_have_a_match.append(result)
    return we_have_a_match.count(True) / 1000
    



print(basic_probablity_testing(23))