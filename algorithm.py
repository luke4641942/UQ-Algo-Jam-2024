import math
import numpy as np
import pandas as pd
import statistics
from sklearn.linear_model import LinearRegression

# Custom trading Algorithm
class Algorithm():

    ########################################################
    # NO EDITS REQUIRED TO THESE FUNCTIONS
    ########################################################
    # FUNCTION TO SETUP ALGORITHM CLASS
    def __init__(self, positions):
        # Initialise data stores:
        # Historical data of all instruments
        self.data = {}
        # Initialise position limits
        self.positionLimits = {}
        # Initialise the current day as 0
        self.day = 0
        # Initialise the current positions
        self.positions = positions
        # Initialise trade counters
        self.uq_dollar_trades = 0
        self.fun_drinks_trades = 0
        self.coffee_trades = 0
        self.beans_trades = 0
        self.milk_trades = 0
        self.fintech_token_trades = 0
        self.red_pen_trades = 0
        self.goober_eats_trades = 0
        self.jean_trades = 0

        
    # Helper function to fetch the current price of an instrument
    def get_current_price(self, instrument):
        # return most recent price
        return self.data[instrument][-1]
    
    ########################################################

    # RETURN DESIRED POSITIONS IN DICT FORM
    def get_positions(self):
        # Get current position
        currentPositions = self.positions
        # Get position limits
        positionLimits = self.positionLimits
        # Declare a store for desired positions
        desiredPositions = {}
        # Loop through all the instruments you can take positions on.
        for instrument, positionLimit in positionLimits.items():
            # For each instrument initilise desired position to zero
                desiredPositions[instrument] = 0
            

        # IMPLEMENT CODE HERE TO DECIDE WHAT POSITIONS YOU WANT 
        #######################################################################
        def calculate_moving_average(data, day, window):
            if day < window:
                return None 
            price_window = data[day - window:day + 1]
            moving_average = statistics.mean(price_window)
            return moving_average
        
        def calculate_volatility(data, period):
            data = pd.Series(data)
            price_changes = data.diff().abs()
            volatility = price_changes.rolling(window=period, min_periods=1).std()
            return volatility
                
        def money_left_over(self):
            total = 500000
            for position in desiredPositions:
                cost = abs(desiredPositions[position]) * self.data[position][self.day]
                total -= cost
            return total
        

        #### Buy Fun Drinks (mean reversion) - $764,900.00 ####
        savings = money_left_over(self)
        qnty = savings / self.data["Fun Drink"][self.day]
        prev_days = min(7, self.day)
        one_day_ma = calculate_moving_average(self.data["Fun Drink"], self.day, 1)
        seven_day_ma = calculate_moving_average(self.data["Fun Drink"], self.day, prev_days)
        # ----diff variables for second moving average indicator----
        prev_days2 = min(8, max(self.day, 5))
        five_day_ma2 = calculate_moving_average(self.data["Fun Drink"], self.day, 5)
        eight_day_ma2 = calculate_moving_average(self.data["Fun Drink"], self.day, prev_days2)
        if one_day_ma == None or seven_day_ma == None:
            desiredPositions["Fun Drink"] = min(math.floor(qnty), positionLimits["Fun Drink"])
            self.fun_drinks_trades += 1
        # ----Price above/below both moving averages----
        elif self.data["Fun Drink"][self.day] < one_day_ma and one_day_ma < seven_day_ma:
            desiredPositions["Fun Drink"] = min(math.floor(qnty), positionLimits["Fun Drink"])
            self.fun_drinks_trades += 1
        elif self.data["Fun Drink"][self.day] > one_day_ma and one_day_ma > seven_day_ma:
            desiredPositions["Fun Drink"] = max(-(math.floor(qnty)), -(positionLimits["Fun Drink"]))
            self.fun_drinks_trades += 1
        # ----Price crosses moving averages----
        elif eight_day_ma2 and self.data["Fun Drink"][self.day] > five_day_ma2 and five_day_ma2 < eight_day_ma2:
            desiredPositions["Fun Drink"] = -(positionLimits["Fun Drink"])
            self.fun_drinks_trades += 1
        elif eight_day_ma2 and self.data["Fun Drink"][self.day] < five_day_ma2 and five_day_ma2 > eight_day_ma2:
            desiredPositions["Fun Drink"] = positionLimits["Fun Drink"]
            self.fun_drinks_trades += 1


        #### Goober Eats (mean reversion) - $343,500.00 ####
        savings = money_left_over(self)
        qnty = savings / self.data["Goober Eats"][self.day] 
        prev_days = min(4, self.day)
        one_day_ma = calculate_moving_average(self.data["Goober Eats"], self.day, 1)
        four_day_ma = calculate_moving_average(self.data["Goober Eats"], self.day, prev_days)
        # ----diff variables for second moving average indicator----
        prev_days2 = min(4, max(self.day, 2))
        two_day_ma2 = calculate_moving_average(self.data["Goober Eats"], self.day, 2)
        four_day_ma2 = calculate_moving_average(self.data["Goober Eats"], self.day, prev_days2)
        if one_day_ma == None or four_day_ma == None:
            pass
        # ----Price above/below both moving averages----
        elif self.data["Goober Eats"][self.day] <= one_day_ma and one_day_ma < four_day_ma:
            desiredPositions["Goober Eats"] = min(math.floor(qnty), positionLimits["Goober Eats"])
            self.goober_eats_trades += 1
        elif self.data["Goober Eats"][self.day] >= one_day_ma and one_day_ma > four_day_ma:
            desiredPositions["Goober Eats"] = max(-(math.floor(qnty)), -(positionLimits["Goober Eats"]))
            self.goober_eats_trades += 1
        # ----Price crosses moving averages----
        elif four_day_ma2 and self.data["Goober Eats"][self.day] > two_day_ma2 and two_day_ma2 < four_day_ma2:
            desiredPositions["Goober Eats"] = max(-(math.floor(qnty)), -(positionLimits["Goober Eats"]))
            self.goober_eats_trades += 1
        elif four_day_ma2 and self.data["Goober Eats"][self.day] < two_day_ma2 and two_day_ma2 > four_day_ma2:
            desiredPositions["Goober Eats"] = min(math.floor(qnty), positionLimits["Goober Eats"])
            self.goober_eats_trades += 1


        #### Buy Coffee (linear regression model) - $251,700.00 ####
        if self.day < 1:
            #pass
            desiredPositions["Coffee"] = positionLimits["Coffee"]
            self.coffee_trades += 1
        else:
            # Use past 25 days including today for features
            prev_days = min(25, self.day)
            milk_prices = self.data["Milk"][self.day - prev_days : self.day + 1]
            bean_prices = self.data["Coffee Beans"][self.day - prev_days : self.day + 1]
            coffee_prices = self.data["Coffee"][self.day - prev_days : self.day + 1]

            # Prepare data for training (exluding todays price for training)
            milk_array = np.array(milk_prices).reshape(-1, 1)
            bean_array = np.array(bean_prices).reshape(-1, 1)
            past_coffee_array = np.array(coffee_prices).reshape(-1, 1)
            X = np.hstack((milk_array[:-1], bean_array[:-1], past_coffee_array[:-1])) 
            # Target prices (shifted 1 forward for next days price)
            y = np.array(coffee_prices[1:])  

            # Model building
            model = LinearRegression()
            model.fit(X, y)
            X_today = np.array([[self.data["Milk"][self.day], self.data["Coffee Beans"][self.day], self.data["Coffee"][self.day]]])
            predicted_coffee_price = model.predict(X_today)
        
            savings = money_left_over(self)
            qnty = savings / self.data["Coffee"][self.day] 
            if predicted_coffee_price[0] > self.data["Coffee"][self.day]:
                desiredPositions["Coffee"] = min(math.floor(qnty), positionLimits["Coffee"])
                self.coffee_trades += 1
            elif predicted_coffee_price[0] < self.data["Coffee"][self.day]:
                desiredPositions["Coffee"] = max(-(math.floor(qnty)), -(positionLimits["Coffee"]))
                self.coffee_trades += 1
            

        #### Buy Thrifted Jeans (mean reversion) - $340,684.00 ####
        savings = money_left_over(self)
        qnty = savings / self.data["Thrifted Jeans"][self.day] 
        prev_days = min(8, self.day)
        one_day_ma = calculate_moving_average(self.data["Thrifted Jeans"], self.day, 1)
        eight_day_ma = calculate_moving_average(self.data["Thrifted Jeans"], self.day, prev_days)
        if one_day_ma == None or eight_day_ma == None:
            #pass
            desiredPositions["Thrifted Jeans"] = min(math.floor(qnty), positionLimits["Thrifted Jeans"])
            self.jean_trades += 1
        # ----Price above/below both moving averages----
        elif self.data["Thrifted Jeans"][self.day] < one_day_ma and one_day_ma < eight_day_ma:
            desiredPositions["Thrifted Jeans"] = min(math.floor(qnty), positionLimits["Thrifted Jeans"])
            self.jean_trades += 1
        elif self.data["Thrifted Jeans"][self.day] > one_day_ma and one_day_ma > eight_day_ma:
            desiredPositions["Thrifted Jeans"] = max(-(math.floor(qnty)), -(positionLimits["Thrifted Jeans"]))
            self.jean_trades += 1
        # ----Price crosses moving averages----
        elif self.data["Thrifted Jeans"][self.day] > one_day_ma and one_day_ma < eight_day_ma:
            desiredPositions["Thrifted Jeans"] = max(-(math.floor(qnty)), -(positionLimits["Thrifted Jeans"]))
            self.jean_trades += 1
        elif self.data["Thrifted Jeans"][self.day] < one_day_ma and one_day_ma > eight_day_ma:
            desiredPositions["Thrifted Jeans"] = min(math.floor(qnty), positionLimits["Thrifted Jeans"])
            self.jean_trades += 1
        

        #### Buy Red pens if price is less (Volatility ependent stratergy) - $104,000.00 ####
        savings = money_left_over(self)
        qnty = savings / self.data["Red Pens"][self.day] 
        volatility = calculate_volatility(self.data["Red Pens"], 10)[self.day]
        volatility_threshold = 0.014
        if volatility and volatility > volatility_threshold:
            prev_days = min(14, max(self.day, 3))
            three_day_ma = calculate_moving_average(self.data["Red Pens"], self.day, 3)
            fourteen_day_ma = calculate_moving_average(self.data["Red Pens"], self.day, prev_days)
            if three_day_ma == None or fourteen_day_ma == None:
                pass
            elif self.data["Red Pens"][self.day] > three_day_ma * 0.98 and three_day_ma > fourteen_day_ma:
                desiredPositions["Red Pens"] = min(math.floor(qnty), positionLimits["Red Pens"])
                self.red_pen_trades += 1
            elif self.data["Red Pens"][self.day] < three_day_ma * 1.02 and three_day_ma < fourteen_day_ma:
                desiredPositions["Red Pens"] = max(-(math.floor(qnty)), -(positionLimits["Red Pens"]))
                self.red_pen_trades += 1
        else:
             # Apply mean reversion strategy during low volatility
            prev_days = min(10, max(self.day, 2))
            two_day_ma = calculate_moving_average(self.data["Red Pens"], self.day, 2)
            ten_day_ma = calculate_moving_average(self.data["Red Pens"], self.day, prev_days)
            if two_day_ma == None or ten_day_ma == None:
                pass
            elif self.data["Red Pens"][self.day] < two_day_ma and two_day_ma < ten_day_ma:
                desiredPositions["Red Pens"] = min(math.floor(qnty), positionLimits["Red Pens"])
                self.red_pen_trades += 1
            elif self.data["Red Pens"][self.day] > two_day_ma and two_day_ma > ten_day_ma:
                desiredPositions["Red Pens"] = max(-(math.floor(qnty)), -(positionLimits["Red Pens"]))
                self.red_pen_trades += 1
            
        
        #### Buying Milk (ma) - $58,000.00 ####
        savings = money_left_over(self)
        qnty = savings / self.data["Milk"][self.day]
        # prev_days = min(7, max(self.day, 2))
        two_day_ma = calculate_moving_average(self.data["Milk"], self.day, 2)
        seven_day_ma = calculate_moving_average(self.data["Milk"], self.day, 7)
        if two_day_ma == None or seven_day_ma == None:
            # pass
            desiredPositions["Milk"] = min(math.floor(qnty), positionLimits["Milk"])
            self.milk_trades += 1
        # ----Price above/below both moving averages----
        elif self.data["Milk"][self.day] <= two_day_ma and two_day_ma < seven_day_ma:
            desiredPositions["Milk"] = min(math.floor(qnty), positionLimits["Milk"])
            self.milk_trades += 1
        elif self.data["Milk"][self.day] >= two_day_ma and two_day_ma > seven_day_ma:
            desiredPositions["Milk"] = max(-(math.floor(qnty)), -(positionLimits["Milk"]))
            self.milk_trades += 1
        # ----Price crosses moving averages----
        elif self.data["Milk"][self.day] > two_day_ma and two_day_ma < seven_day_ma:
            desiredPositions["Milk"] = max(-(math.floor(qnty)), -(positionLimits["Milk"]))
            self.milk_trades += 1
        elif self.data["Milk"][self.day] < two_day_ma and two_day_ma > seven_day_ma:
            desiredPositions["Milk"] = min(math.floor(qnty), positionLimits["Milk"])
            self.milk_trades += 1


        #### Buy Fintech Token (Volatility ependent stratergy) - $93,559.45 ####
        savings = money_left_over(self)
        qnty = savings / self.data["Fintech Token"][self.day] 
        volatility = calculate_volatility(self.data["Fintech Token"], 11)[self.day]
        volatility_threshold = 12
        if volatility and volatility > volatility_threshold:
            # Apply momentum stratergy during high volitility
            # prev_days = min(24, max(self.day, 10))
            eight_day_ma = calculate_moving_average(self.data["Fintech Token"], self.day, 8)
            tf_day_ma = calculate_moving_average(self.data["Fintech Token"], self.day, 24)
            if eight_day_ma == None or tf_day_ma == None:
                pass
                # desiredPositions["Fintech Token"] = min(math.floor(qnty), positionLimits["Fintech Token"]) 
            elif self.data["Fintech Token"][self.day] > eight_day_ma * 0.95 and eight_day_ma > tf_day_ma:
                desiredPositions["Fintech Token"] = min(math.floor(qnty), positionLimits["Fintech Token"]) 
                self.fintech_token_trades += 1
            elif self.data["Fintech Token"][self.day] < eight_day_ma * 1.02 and eight_day_ma < tf_day_ma:
                desiredPositions["Fintech Token"] = max(-(math.floor(qnty)), -(positionLimits["Fintech Token"]))
                self.fintech_token_trades += 1
        else:
             # Apply mean reversion strategy during low volatility
            prev_days = min(5, self.day)
            one_day_ma = calculate_moving_average(self.data["Fintech Token"], self.day, 1)
            five_day_ma = calculate_moving_average(self.data["Fintech Token"], self.day, prev_days)
            if one_day_ma == None or five_day_ma == None:
               # pass
                desiredPositions["Fintech Token"] = min(math.floor(qnty), positionLimits["Fintech Token"])
                self.fintech_token_trades += 1 
            elif self.data["Fintech Token"][self.day] < one_day_ma and one_day_ma < five_day_ma:
                desiredPositions["Fintech Token"] = min(math.floor(qnty), positionLimits["Fintech Token"]) 
                self.fintech_token_trades += 1
            elif self.data["Fintech Token"][self.day] > one_day_ma and one_day_ma > five_day_ma:
                desiredPositions["Fintech Token"] = max(-(math.floor(qnty)), -(positionLimits["Fintech Token"]))
                self.fintech_token_trades += 1
        

        #### Buying Coffee Beans (ma) - $36,843.42 ####
        savings = money_left_over(self)
        qnty = savings / self.data["Coffee Beans"][self.day]
        prev_days = min(4, max(self.day, 1))
        one_day_ma = calculate_moving_average(self.data["Coffee Beans"], self.day, 1)
        four_day_ma = calculate_moving_average(self.data["Coffee Beans"], self.day, prev_days)
        # ----diff variables for second moving average indicator----
        prev_days2 = min(9, max(self.day, 2))
        two_day_ma2 = calculate_moving_average(self.data["Coffee Beans"], self.day, 2)
        nine_day_ma2 = calculate_moving_average(self.data["Coffee Beans"], self.day, prev_days2)
        if one_day_ma == None or four_day_ma == None:
            # pass
            desiredPositions["Coffee Beans"] = min(math.floor(qnty), positionLimits["Coffee Beans"])
            self.beans_trades += 1
        # ----Price above/below both moving averages----
        elif self.data["Coffee Beans"][self.day] < one_day_ma and one_day_ma < four_day_ma:
            desiredPositions["Coffee Beans"] = min(math.floor(qnty), positionLimits["Coffee Beans"])
            self.beans_trades += 1
        elif self.data["Coffee Beans"][self.day] > one_day_ma and one_day_ma > four_day_ma:
            desiredPositions["Coffee Beans"] = max(-(math.floor(qnty)), -(positionLimits["Coffee Beans"]))
            self.beans_trades += 1
        # ----Price crosses moving averages----
        elif nine_day_ma2 and self.data["Coffee Beans"][self.day] > two_day_ma2 and two_day_ma2 < nine_day_ma2:
            desiredPositions["Coffee Beans"] = max(-(math.floor(qnty)), -(positionLimits["Coffee Beans"]))
            self.beans_trades += 1
        elif nine_day_ma2 and self.data["Coffee Beans"][self.day] < two_day_ma2 and two_day_ma2 > nine_day_ma2:
            desiredPositions["Coffee Beans"] = min(math.floor(qnty), positionLimits["Coffee Beans"])
            self.beans_trades += 1


        #### Buying UQ Dollar (scalping) - $66,174.77 ####
        savings = money_left_over(self)
        qnty = savings / self.data["UQ Dollar"][self.day]
        if self.data["UQ Dollar"][self.day] < 100:
            desiredPositions["UQ Dollar"] = min(math.floor(qnty), positionLimits["UQ Dollar"])
            self.uq_dollar_trades += 1
        elif self.data["UQ Dollar"][self.day] >= 100:
            desiredPositions["UQ Dollar"] = max(-(math.floor(qnty)), -(positionLimits["UQ Dollar"]))
            self.uq_dollar_trades += 1


        if self.day == 364:
            print("------------------------------------------")
            print("This is the number of milk trades completed:" + str(self.milk_trades))
            print("This is the number of beans trades completed:" + str(self.beans_trades))
            print("This is the number of uq dollar trades completed:" + str(self.uq_dollar_trades))
            print("This is the number of fintech trades completed:" + str(self.fintech_token_trades))
            print("This is the number of fun drinks trades completed:" + str(self.fun_drinks_trades))
            print("This is the number of coffee trades completed:" + str(self.coffee_trades))
            print("This is the number of red pen trades completed:" + str(self.red_pen_trades))
            print("This is the number of goober eats trades completed:" + str(self.goober_eats_trades))
            print("This is the number of jeans trades completed:" + str(self.jean_trades))
            print("------------------------------------------")
            

        #######################################################################
        # Return the desired positions
        return desiredPositions
    






    