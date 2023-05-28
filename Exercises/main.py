# import necessary libraries
from Exercise_1 import run_fizz_buzz
from Exercise_2 import valuation_service

if __name__ == '__main__':
    # exercise 1
    #run_fizz_buzz()

    # exercise 2
    valuation_service('data.csv', 'currencies.csv', 'matchings.csv')


# matching_id,total_price,avg_price,currency,ignored_products_count
# 1,10080.0,2782.5,PLN,1
# 1,2205.0,2782.5,PLN,1
# 2,21000.0,5337.5,PLN,0
# 2,7350.0,5337.5,PLN,0
# 3,11760.0,4284.0,PLN,1
# 3,8400.0,4284.0,PLN,1
# 3,7560.0,4284.0,PLN,1