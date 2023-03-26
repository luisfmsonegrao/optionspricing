import math
import unittest
import numpy as np
import unittest as ut

class TestBinomialOptionTreeConstructor(unittest.TestCase):
    
    def setUp(self):
        self.price = 100
        self.strike = 101
        self.option_type = "Put"
        self.up_move = 1.1
        self.down_move = 0.9
        self.rate = 0.05
        self.nsteps = 3
        self.step = 1
        self.bot = BinomialOptionTree(self.price, self.strike, self.option_type, self.up_move, self.down_move, self.rate, self.nsteps, self.step)

    def test_constructor_price(self):
        self.assertEqual(self.bot.stock_price, self.strike, "Wrong price!")





class BinomialOptionTree:


    def __init__(
            self, 
            stock_price, 
            strike_price, 
            option_type, 
            up_move, 
            down_move, 
            rate, 
            n_steps, 
            step
        ):
        self.stock_price = stock_price
        self.strike_price = strike_price
        self.option_type = self._validate_option_type(option_type)
        self.up_move = self._set_up_move(up_move)
        self.down_move = self._set_down_move(down_move)
        self.rate = rate
        self.n_steps = self._set_n_steps(n_steps)
        self.step = self._set_step(step)
        self.risk_free_probability = self._calculate_risk_free_probability()
        self.prices = self._generate_prices()
        self.payoffs = self._generate_payoffs()
        self.discounted_values = self._generate_discounted_values()
        self.present_value = self.option_present_value()


    def _calculate_risk_free_probability(self):
        p = (math.exp(self.rate*self.step)-self.down_move)/(self.up_move - self.down_move)
        return p

    def option_present_value(self):
        return self.discounted_values[0]


    def _generate_prices(self):
        prices = np.array([self.stock_price])
        for n in range(1, self.n_steps+1):
            new_prices = np.array([0.0]*(n+1))
            for i in range (0,n+1):
                new_prices[i] = self.stock_price*(self.up_move**(n-i))*(self.down_move**(i))
            prices = np.append(prices, new_prices)
        return prices

    def _generate_discounted_values(self):
        discounted_values = np.array(self.payoffs)
        for i in range(1,self.n_steps+1):
            current_values_min_ind = len(self.payoffs)-sum(j for j in range(self.n_steps+2-i,self.n_steps+2))
            current_values_max_ind = len(self.payoffs)-sum(j for j in range(self.n_steps+3-i,self.n_steps+2))
            current_values = self.payoffs[current_values_min_ind:current_values_max_ind]
            next_values_min_ind = len(self.payoffs)-sum(j for j in range(self.n_steps+1-i, self.n_steps+2))
            next_values_max_ind = len(self.payoffs)-sum(j for j in range(self.n_steps+2-i, self.n_steps+2))
            next_payoffs = self.payoffs[next_values_min_ind:next_values_max_ind]
            if self.option_type == "American Put" or self.option_type == "American Call":
                discounted_values[next_values_min_ind:next_values_max_ind] = np.maximum(next_payoffs, self._calculate_binomial_value(current_values))
            else:
                discounted_values[next_values_min_ind:next_values_max_ind] = self._calculate_binomial_value(current_values)
        return discounted_values

    def _generate_payoffs(self):
        if self.option_type in ["Call", "American Call", "European Call"]:
            payoffs = np.maximum((self.prices - self.strike_price), 0)
        elif self.option_type in ["Put", "American Put", "European Put"]:
            payoffs = np.maximum(-(self.prices - self.strike_price), 0)
        return payoffs

    def _calculate_binomial_value(self, payoffs):
        binomial_values = np.array([0.0]*(len(payoffs)-1))
        for i in range(len(binomial_values)):
            binomial_values[i] = math.exp(-self.rate*self.step)*(self.risk_free_probability*payoffs[i] + (1-self.risk_free_probability)*payoffs[i+1])
        return binomial_values

    def _validate_option_type(self, option_type):
        types = ["Call", "Put", "American Put", "American Call", "European Put", "European Call"]
        if not (option_type in types):
            raise ValueError("{} is not a valid option type. Please enter one of the following: {}".format(option_type, types))
        return option_type

    def _set_up_move(self, up_move):
        if up_move < 1:
            raise ValueError("Up move must be greater than 1.")
        return up_move

    def _set_down_move(self, down_move):
        if not (0 < down_move < 1):
            raise ValueError("Down move must be smaller than 1 and greater than 0.")
        return down_move

    def _set_n_steps(self, n_steps):
        if n_steps < 1:
            raise ValueError("Number of steps must be at least 1.")
        return n_steps

    def _set_step(self, step):
        if step <= 0:
            raise ValueError("Size of step must be greater than 0.")
        return step
        


if __name__ == "__main__":
    print("Running...")
    #calcular preco de opcoes dado input do utilizador