import datetime
import yfinance as yf
import plotly.graph_objects as go
import plotly.io as pio

current_time = datetime.datetime.now()

total_stock_values = []
stock_names = []

class Stock_Portfolio():
    def get_stock_value(interval = '15m'):
        global num_stocks
        num_stocks = int(input("hey how many stocks do you have?? "))
        for i in range(num_stocks):
            stock_name = input("Stock Symbol: ")
            stock_names.append(stock_name)

            data = yf.download(tickers = stock_name, period= '1d', interval = interval)
            now_value = data['Open'].iloc[-1]

            num_shares = int(input('how many shares do you have?? '))
            total_val = now_value * float(num_shares)

            total_val = float('%.2f' % (total_val))
            total_stock_values.append(total_val)

            print("Value of  " + str(stock_name) + " is " + str(now_value))
            print("Total Value of shares : " + str(total_val))
    pio.renderers.default = 'browser'

    def create_pie_chart():
        # Calculate total portfolio value
        total_value = sum(total_stock_values)
        
        # Create the pie chart
        fig = go.Figure(data=[go.Pie(labels=stock_names, 
                                    values=total_stock_values, 
                                    textinfo='label+percent', 
                                    insidetextorientation='radial')])
        
        # Add a descriptive title
        fig.update_layout(title_text=f"Stock Portfolio: ${total_value:,.2f}",  # Format total value nicely
                        title_font_size=20)
        
        # Render the pie chart in the browser
        fig.show()

        # Print portfolio details
        print(current_time.strftime('%Y-%m-%d'))
        print(f"Total Stock Values: {total_stock_values}")
        print(f"Stock Names: {stock_names}")
    if __name__ == "__main__":
        get_stock_value()
        create_pie_chart()



# a
# 3
# 5
# b
# 4
# c
# 6
