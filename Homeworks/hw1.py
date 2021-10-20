import random

class Portfolio():
    
    def __init__(self, cash = 0, stocks = {}, mutual_funds = {}, actions = []):
        self.cash = cash
        self.stocks = stocks
        self.mutual_funds = mutual_funds
        self.actions = actions
    
    def addCash(self, amount):
        self.cash += amount
        self.actions.append(f"Add ${amount} to the portfolio")
        
    def withdrawCash(self, amount):
        self.cash -= amount
        self.actions.append(f"Remove ${amount} from the portfolio")
        
    def buyStock(self, share, stock):
        self.cash -= stock.price / share
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] += share
        else:
            self.stocks[stock.symbol] = share
        self.actions.append(f'Buy {share} shares of stock "{stock.symbol}"')
        
    def sellStock(self, stock, share):
        self.cash += random.uniform(0.5, 1.5) / share
        self.stocks[stock] -= share
        self.actions.append(f'Sell {share} shares of "{stock}"')
    
    def buyMutualFund(self, share, mf):
        self.cash -= 1 / share
        if mf.symbol in self.mutual_funds:
            self.mutual_funds[mf.symbol] += share
        else:
            self.mutual_funds[mf.symbol] = share
        self.mutual_funds[mf.symbol] = share
        self.actions.append(f'Buy {share} shares of "{mf.symbol}"')
        
    def sellMutualFund(self, mf, share):
        self.cash += random.uniform(0.9, 1.2) / share
        self.mutual_funds[mf] -= share
        self.actions.append(f'Sell {share} shares of "{mf}"')
    
    def history(self):
        for i, action in enumerate(self.actions):
            print(f"{i+1}- {action}")
        
    def __str__(self):
        return_str = f"cash:\n${self.cash:.2f}\n\nstock:"
        for stock, share in self.stocks.items():
            return_str += f"\n{share} {stock}"
        return_str += f"\n\nmutual funds:"
        for mf, share in self.mutual_funds.items():
            return_str += f"\n{share:.2f} {mf}"
        return return_str
        #return f"cash: ${self.cash}\nstock: {self.stocks}\nmutual funds: {self.mutual_funds}"
    

    
class Stock():
    
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol


        
class MutualFund():
    
    def __init__(self, symbol):
        self.symbol = symbol


portfolio = Portfolio() # Creates a new portfolio
portfolio.addCash(300.50) # Adds cash to the portfolio

s = Stock(20, "HFH") # Creates Stock with price 20 and symbol "HFH"

portfolio.buyStock(5, s) # Buys 5 shares of stock s

mf1 = MutualFund("BRT") # Create MF with symbol "BRT"
mf2 = MutualFund("GHT") # Create MF with symbol "GHT"

portfolio.buyMutualFund(10.3, mf1) # Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) # Buys 2 shares of "GHT"

portfolio.sellMutualFund("BRT", 3) # Sells 3 shares of BRT

portfolio.sellStock("HFH", 1) # Sells 1 share of HFH

portfolio.withdrawCash(50) # Removes $50


print(portfolio) # Print portfolio

portfolio.history() # Prints a list of all transactions ordered by time