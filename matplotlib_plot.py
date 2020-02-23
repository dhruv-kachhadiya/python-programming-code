#this is programme using matplotlib.pyplot (type=plot)

from matplotlib import pyplot as pt

car=['tata','suzuki','honda','hundai','nissan']
profit=[1.1,10.8,9.5,10.2,9.9]
pt.plot(car,profit,color='green')
pt.ylabel('profit_in_billion')
pt.xlabel('car_companies')
pt.title('car company\'s profit')
pt.show()
