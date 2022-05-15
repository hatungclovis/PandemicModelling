#Code written by Clovis Hatungimana for the SIR model (modeling pandemics)

import matplotlib.pyplot as plt

# defining variables and parameters

S = [30000]   #susceptible individuals
I = [10]    #Infected individuals
R = [990]   #Removed individuals
N = S[0]+I[0]+R[0]   #Total population = S + I + R
d = 14     # number of days a person with covid is infective
b = 1/d   # the rate at which an individual transfers from infected (I) to the removed (R) population
c = 14   # the average total number of contacts per infective person
a = c*b    # the daily rate of contacts per infective individual
dt = 1    #changes in the population are calulated per day.

period_of_observation=150
# setting the values for t as a list that will contain values from 0 to 150 days.
t=[0]
counter=0

while counter < period_of_observation:
    
    #calculating by regression the number of remaining susceptible people over dt interval
    susceptible = round(S[counter], 2) - (a*round(I[counter],2)*round(S[counter],2)/N)*dt
    
    #calculating by regression the number of infected people over dt interval
    infected = round(I[counter], 2) + ((a*round(I[counter],2)*round(S[counter],2)/N)-b*round(I[counter],2))*dt
    
    #calculating by regression the number of removed people over dt interval
    removed = round (R[counter], 2) + b*round(I[counter],2)*dt
    
    susceptible= round(susceptible, 2)
    infected= round(infected, 2)
    removed = round(removed, 2)
    
    #Storing lists of values for S(t), I(t), and R(t) over our period of observation
    S.append(susceptible)
    I.append(infected)
    R.append(removed)
    
    counter=counter+1
    t.append(counter)


print ("S values:\n",S)
print()
print("I values:\n",I)
print()
print("R values:\n", R)
print()

print ('this is max I')

print(max(I))
print("this is S",S[15])

#now we plot the values of S, I, and R

plt.plot(t, R, 'y') # plotting t, R separately
plt.plot(t, S, 'b') # plotting t, S separately 
plt.plot(t, I, 'r') # plotting t, I separately 
 
plt.title("COVID-19 SIR Model")
plt.xlabel('Number of days')
plt.ylabel('Number of people')
plt.legend({'R','S','I'})
plt.show()



