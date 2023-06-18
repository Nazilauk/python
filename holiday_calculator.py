#---------------------------------------------------------------------------------------------------------------------------------
# this program calculates a users holiday costs, including the plane cost, hotel cost, and
# car rental cost with user input
#--------------------------------------------------------------------------------------------------------------------------------


#Define a function to calculate the hotel cost
def hotel_cost(num_nights):
    return num_nights * 100

# Define a function to calculate the plane cost
def plane_cost(city_flight):
    # Create a dictionary to store the prices for each city
    city_prices = {
        "New York": 200,
        "Los Angeles": 250,
        "Chicago": 150
    }
    # Use the get() method to retrieve the price for the chosen city
    # If the city is not in the dictionary, return a default value of 300
    return city_prices.get(city_flight, 300)

# Define a function to calculate the car rental cost
def car_rental(rental_days):
    return rental_days * 50

# Define a function to calculate the total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    # Use the round() function to round the total cost to two decimal places
    return round(hotel_cost + plane_cost + car_rental, 2)

# Get user inputs for city_flight, num_nights and rental_days
city_flight = input("Enter the city you will be flying to (New York, Los Angeles, Chicago): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days that you will be hiring a car for: "))

# Calculate the total cost for each component of the holiday
total_hotel_cost = hotel_cost(num_nights)
total_plane_cost = plane_cost(city_flight)
total_car_rental_cost = car_rental(rental_days)
total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_car_rental_cost)

# Print out all the details about the holiday in a readable way!
print("Holiday Details:")
print(f"City Flight: {city_flight}")
print(f"Number of Nights at Hotel: {num_nights}")
print(f"Number of Days for Car Rental: {rental_days}")
print(f"Total Hotel Cost: ${total_hotel_cost:.2f}")
print(f"Total Plane Cost: ${total_plane_cost:.2f}")
print(f"Total Car Rental Cost: ${total_car_rental_cost:.2f}")
print(f"Total Holiday Cost: ${total_holiday_cost:.2f}")

