import pandas as pd
#import models for predictions
from sklearn.model_selection import train_test_split
#estimates linear relationship between a scaled response and one or more possible explanations
from sklearn.linear_model import LinearRegression
#calculates mse
from sklearn.metrics import mean_squared_error
import csv
#used to make graphs
import matplotlib.pyplot as plt
#the data within temperature is purely fabricated by me to act as a benchmark to which the model can be compared and data to predict the users mood
data = pd.read_csv('temp.csv')

#determine what variables are being compared to what.
#in this case the low spent inside, average temperature and peak temperature are being compared to the mood
X = data[['mini', 'mean', 'maxi']]
Y = data['mood']
#X= input features
#Y=Target variable(mood)
#random_state: sets seed for reproducibility
#This is essential for evaluating the correlation
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
#create a linear regression
model = LinearRegression()
#fit model with training data
model.fit(X_train, Y_train)

#predict mode scores for text set

Y_pred = model.predict(X_test)


print("\033[94m\033[1mLinear Regression Model Complete!\033[0m")




#tell the user exactly whats happening
print ("The mean squared error or mean squared deviation of an estimator measures the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value. In other words, do the parameters in question really affect the mood of the user?")
#abbreviate the mean squared error
#mean squared error is how the data to relates to the variable ie are they dependent on one another or independent
mse = mean_squared_error(Y_test, Y_pred)
#use a dictionary to print whether the data is good or not
print(f"Mean Squared Error: {mse}")

# Display how accuarate the model is by calculating the mean squared error and print it in words for the user to interpret
#Result is easy for the user to read as it is colour coded from green to red(depending how good or bad the accuaracy is)
def interpret_mse(mse):
    if mse < 10:
        return "\033[32mExcellent model accuracy.\033[0m"
    elif mse < 20:
        return "\033[92mGood model accuracy.\033[0m"
    elif mse < 30:
        return "\033[93mAverage model accuracy.\033[0m"
    elif mse < 40:
        return "\033[38;2;255;165;0mBelow average model accuracy.\033[0m"
    else:
        return  "\033[91mPoor model accuracy! Get better data.\033[0m\n"


mse_remark = interpret_mse(mse)
print("How good is this model? ", mse_remark)



#make a prediction of the users mood using the model above
#function
def predict_mood(low_inside, temperature, maxi):
    df = pd.DataFrame([[low_inside, temperature, maxi]],
                      columns=['mini', 'mean', 'maxi'])
    return model.predict(df)[0]


# Let the user enter their own 3 parameters
print("")
print("USER CHOOSES 3 TEMPERATURE PARAMETERS")
day_of_of_the_week=input(str("What day of the week is it?"))
low = int(input("Enter minimum temperature. Can be any integer from 0-24"))
temp = float(input("Enter average temperature. Can be anything from 0-50 "))
peak = int(input("Enter peak temperature. Can be anything from 0-50"))

predicted_mood = predict_mood(low, temp, peak)  # Example values
print("\nThe Predicted Mood Score for",day_of_of_the_week,"is", predicted_mood)


#what will the users mood be if all 3 parameters are low
#ie what will the users mode be if they spent all day outside in the cold

print("-----------------------------------------------------------")

print("What will the mood be if you spend all day outside in the cold?")

#low values
low= 2
average_temp = 1
peak = 3
#print the users state of mind when they spend all day outside in the cold
demeanour_low_parameters = predict_mood(low, average_temp, peak)
print("\nThe low temp score mood is", demeanour_low_parameters)



#what will the users mood be if all 3 parameters are high
#ie what will the users mode be if they spent all day inside beside a hot fire
print("-----------------------------------------------------------")
print("What if question 2")
print("What will the users mood be if they spend all day inside in the warmth")

#3 high values
low= 24
average_temp = 30
peak = 35
#print the users state of mind when they spend all day inside in the warmth
demeanour_high_parameters = predict_mood(low, average_temp, peak)
print("\nThe higher temp score mood is", demeanour_high_parameters)



#which variable most relates to the users state of mind
print("\033[38;2;255;165;0mwhat if question 3")
print("Let's test if average temperature is more important than peak tempLevel")
print("We will keep the low (A) the same and double the others (B) and (C) one at a time\033[0m")


print("normal values examples:")

#normal value examples
low= 17
average_temp = 20
peak = 25
#use these three values to get the baseline
baseline_mood = predict_mood(low, average_temp, peak)
print("\nThe baseline Score mood is", baseline_mood)
print("")


#double average_temp
print("double average_temp")
low= 17
average_temp = 40
peak = 25
#abbreviate predicted mood
doubleAverageOutcome = predict_mood(low, average_temp, peak)
print("The double temperature mood is", doubleAverageOutcome)
print("")

#double peak temperature
print("double peak temperature")
low= 17
average_temp = 20
peak = 50

doublePeakOutcome = predict_mood(low, average_temp, peak)
print("The double peak mood is", doublePeakOutcome)
print("")
#print answers to what if question 3
print("\033[94m\033[1mOutcome:\033[0m")
if doubleAverageOutcome > doublePeakOutcome:
    print("It's the average temperature that improves mood the most.")
    print("You should try stay warm throughout the day")
else:
    print("It's the peak temperature that improves mood the most")
    print("You should try stay in direct warmth for a few moments then continue about your day.")
#show answers to what if questions

variable_names = ['Mood if Little high temp', 'Mood if Lots of high temp',]
values = [demeanour_low_parameters, demeanour_high_parameters]

#create bar chart
plt.bar(variable_names, values)

#add title and labels
plt.xlabel('Amount of temp')
plt.ylabel('Mood')
plt.title('Bar Chart of WHAT-IF Q1 and Q2 Outcomes')

#show graph
plt.show()

#------------------------------------
#repeat
#show results for the what if questions on graph


#label which is which
variable_names = ['Mood if Double Average', 'Mood if Double Peak',]
values = [doubleAverageOutcome, doublePeakOutcome]

#create bar chart
plt.bar(variable_names, values)

plt.xlabel('Amount of temp')
plt.ylabel('Mood')
plt.title('Bar Chart of WHAT-IF Q3 Outcome')

plt.show()
