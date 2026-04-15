import numpy as np
import matplotlib.pyplot as plt
import math
rng = np.random.default_rng()

#let's create a traffic light
class Car:
    #Lambda1 is the average time the first car has waited at the traffic light before it turns green
    #Lambda2 is the average number of cars came at the same time
    #lambda3 is average difference in time between the arrival of two cars
    def Wait_time_cars(Lambda1,Lambda2,lambda3,Total_cars): #perfectly working now
        First_car_Time = -1
        Number_first_cars = -1
        while First_car_Time <= 0: #the first car can't wait for a negative time
            First_car_Time = np.random.poisson(Lambda1)
        while Number_first_cars <= 0: #the number of cars that came at the same time can't be negative
            Number_first_cars = np.random.poisson(Lambda2)
        Time = np.ones(Total_cars)
        #print("First_car_Time:", First_car_Time)
        #print("Number_first_cars:", Number_first_cars)
        i = 0
        i = Car.fill_time(Time,i,Number_first_cars,First_car_Time) #fill the time for the first cars that came at the same time
        #print("i:", i)
        new_time = -1
        new_number_cars = -1
        while i < Total_cars: #while there are still cars that haven't come to the traffic light
            while new_time <= 0: #the time difference between the arrival of two cars can't be negative
                new_time = max(0, Time[i-1] - np.random.poisson(lambda3))
            while new_number_cars <= 0 or i + new_number_cars > Total_cars: #the number of cars that came at the same time can't be negative
                new_number_cars = max(0, np.random.poisson(Lambda2))
                ##print("new_number:cars:", new_number_cars)
            ##print("new_time:", new_time)
            #print("new_number_cars:", new_number_cars)
            i = Car.fill_time(Time,i,i+new_number_cars,new_time) #fill the time for the new cars that came at the same time
            ##print("i:", i)
            new_time = -1
            new_number_cars = -1
        return Time
    
    def fill_time(Time,start_pos,final_pos,new_time): #final_pos = Total_cars stops the loop
        for i in range(start_pos,final_pos):
            Time[i] = new_time
        return final_pos

#let's test the function
# We can calculate the waiting time for each car before the traffic light turns green for its road.
Total_cars = 20 
Lambda2_road1 = 5  #number of cars that came at the same time, more traffic on the first road
Lambda2_road2 = 3  #number of cars that came at the same time, medium traffic on the second road
Lambda2_road3 = 2  #number of cars that came at the same time, less traffic on the third road
lambda3_road1 = 5 #difference in time between the arrival of two cars
lambda3_road2 = 10 #difference in time between the arrival of two cars
lambda3_road3 = 15 #difference in time between the arrival of two cars
time_averages_road1 = []
time_averages_road2 = []
time_averages_road3 = []
time_averages_general = []
t = 15 * (np.arange(7) + 2) #time in seconds for the traffic light to turn green for the first road
Time_to_exit = 3 #time in seconds for a car to exit the traffic light after it turns green
for t1 in t:

    t2 = (Lambda2_road2/Lambda2_road1)* t1 #time in seconds for the traffic light to turn green for the second road
    t3 = (Lambda2_road3/Lambda2_road1)* t1 #time in seconds for the traffic light to turn green for the third road

    Cars_got_out_road1 = t1 // Time_to_exit #number of cars that got out of the traffic light for the first road
    Cars_got_out_road2 = t2 // Time_to_exit #number of cars that got out of the traffic light for the second road
    Cars_got_out_road3 = t3 // Time_to_exit #number of cars that got out of the traffic light for the third road

    average_time_per_car_cycle_road1 = np.round((Cars_got_out_road1 + 1)* Time_to_exit / 2) #average time for a car to exit the traffic light for the first road
    average_time_per_car_cycle_road2 = np.round((Cars_got_out_road2 + 1)* Time_to_exit / 2) #average time for a car to exit the traffic light for the second road
    average_time_per_car_cycle_road3 = np.round((Cars_got_out_road3 + 1)* Time_to_exit / 2) #average time for a car to exit the traffic light for the third road

    exit_batch_size_road1 = Total_cars // Cars_got_out_road1 #number of cars that got out of the traffic light in each batch for the first road
    exit_batch_size_road2 = Total_cars // Cars_got_out_road2 #number of cars that got out of the traffic light in each batch for the second road
    exit_batch_size_road3 = Total_cars // Cars_got_out_road3 #number of cars that got out of the traffic light in each batch for the third road
    
    average_waiting_time_first_car_road1 = average_time_per_car_cycle_road1 + 0.5 * exit_batch_size_road1*(t1+t2+t3) #average waiting time for a car before the traffic light turns green for the first road
    average_waiting_time_first_car_road2 = average_time_per_car_cycle_road2 + 0.5 * exit_batch_size_road2*(t1+t2+t3) #average waiting time for a car before the traffic light turns green for the second road
    average_waiting_time_first_car_road3 = average_time_per_car_cycle_road3 + 0.5 * exit_batch_size_road3*(t1+t2+t3) #average waiting time for a car before the traffic light turns green for the third road


    Lambda1_road1 = average_waiting_time_first_car_road1 # time in seconds
    Lambda1_road2 = average_waiting_time_first_car_road2 # time in seconds
    Lambda1_road3 = average_waiting_time_first_car_road3 # time in seconds

    Time1 = Car.Wait_time_cars(Lambda1_road1,Lambda2_road1,lambda3_road1,Total_cars) #time for the first road
    Time2 = Car.Wait_time_cars(Lambda1_road2,Lambda2_road2,lambda3_road2,Total_cars) #time for the second road
    Time3 = Car.Wait_time_cars(Lambda1_road3,Lambda2_road3,lambda3_road3,Total_cars) #time for the third road
    
    Waiting_time_road1 = 0
    Waiting_time_road2 = 0
    Waiting_time_road3 = 0

    for i in range(Total_cars):
        Waiting_time_road1 += Time1[i] + math.floor(3 * i  / t1) * (t1+t2+t3) + ((i%Cars_got_out_road1) + 1)  * 3  #waiting time for the first road
        Waiting_time_road2 += Time2[i] + math.floor(3 * i / t2) * (t1+t2+t3) + ((i%Cars_got_out_road2) + 1) * 3  #waiting time for the second road
        Waiting_time_road3 += Time3[i] + math.floor(3 * i / t3) * (t1+t2+t3) + ((i%Cars_got_out_road3) + 1) * 3  #waiting time for the third road
        #print("Waiting_time_road1:", Waiting_time_road1) 
    average_waiting_time_road1 = Waiting_time_road1 / Total_cars #average waiting time for the first road
    average_waiting_time_road2 = Waiting_time_road2 / Total_cars #average waiting time for the second road
    average_waiting_time_road3 = Waiting_time_road3 / Total_cars #average waiting time for the third road 
    time_averages_road1.append(average_waiting_time_road1)
    time_averages_road2.append(average_waiting_time_road2)
    time_averages_road3.append(average_waiting_time_road3)
    time_averages_general_in_i = round((average_waiting_time_road1 + average_waiting_time_road2 + average_waiting_time_road3)//3)
    time_averages_general.append(time_averages_general_in_i)
    #print("Time1:", Time1)

plt.plot(t, time_averages_road1, label='Road 1')
plt.plot(t, time_averages_road2, label='Road 2')
plt.plot(t, time_averages_road3, label='Road 3')
plt.plot(t,time_averages_general, label='General Average')
min_index = np.argmin(time_averages_general)
min_average_time = time_averages_general[min_index]
optimal_time = t[min_index]
plt.annotate(
    f"my optimal point: ({optimal_time:.2f} s, {min_average_time:.2f} s)",  # Text to display with the optimal point coordinates
    xy=(optimal_time, min_average_time),            # lowest point coordinates (x, y) in data coordinates
    xytext=(optimal_time - 0.5, min_average_time - 0.5),  # text position (x, y) in data coordinates
    ha = 'center',            
    va = 'bottom',             # text position in alignment (x, y)
    fontsize=9,                   # font size
    color='black',                # text color
    arrowprops=dict(arrowstyle='-|>',
        linewidth=0.5,
        mutation_scale=25,
        color='red',
        connectionstyle="arc3,rad=-0.1")  # arrow properties: style, width, and color     
)
#plt.xlabel('Time for traffic light to turn green for the first road (seconds)')
#plt.ylabel('Average waiting time for a car (seconds)')
plt.title('Average waiting time for a car before the traffic light turns green')
plt.legend()
plt.show()
# we can officially say that now we have our time vector indicating the waiting time for each car before the traffic light turns green.
# let's imagine that the traffic light turns green for the first road, then the second road, then the third road, 
# and then it turns red again for all roads, and this cycle repeats. 
# what I see is an instant photo of the traffic the second the traffic light turns green 




