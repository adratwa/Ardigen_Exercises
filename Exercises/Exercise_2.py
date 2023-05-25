"""
This Python script performs a product valuation task.

The script reads product, currency conversion rates, and matching criteria from CSV files.

It then converts product prices to PLN, calculates the total price of each product,

and identifies the top-priced products for each matching_id based on provided criteria.

The results, which include matching_id, total_price, average price, currency, and the count of non-selected products per matching_id,

are stored in 'top_products.csv'.

Note: The CSV files are expected to be in a directory named 'data'. The script can handle FileNotFoundError.
"""

# import necessary libraries
import pandas as pd


# function that reads data from csv files
def load_data(data_file, currencies_file, matchings_file):
    # directory where all data is stored
    data_directory = 'data/'
    # try/except block to handle any FileNotFoundError
    try:
        data = pd.read_csv(data_directory + data_file)
        currencies = pd.read_csv(data_directory + currencies_file)
        matchings = pd.read_csv(data_directory + matchings_file)
        return data, currencies, matchings
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None


# function that converts price to PLN
def currency_convertor_to_pln(data, currencies):
    # merge product data with currency data on 'currency' column
    data = data.merge(currencies, on='currency', how='left')
    # convert price to PLN
    data['price'] = data['price'] * data['ratio']
    # change the 'currency' column to 'PLN'
    data['currency'] = 'PLN'
    # drop 'ratio' column as it is no longer needed
    data.drop(columns='ratio', inplace=True)
    return data


# function that gets top priced products based on 'matching_id'
def get_top_priced(data, currencies, matchings):
    data = currency_convertor_to_pln(data, currencies)
    # compute the total price for each product
    data['total_price'] = data['price'] * data['quantity']

    # merge product data with matchings data on 'matching_id'
    data = pd.merge(data, matchings, on='matching_id', how='right')
    # sort the data based on 'matching_id' and 'total_price'
    data_sorted = data.sort_values(['matching_id', 'total_price'], ascending=[True, False])

    top_products = []

    for matching_id, group in data_sorted.groupby('matching_id'):
        # get the number of top priced products for each group
        chosen_products_count = group['top_priced_count'].values[0]
        # compute number of ignored products, in case if number is negative take 0
        ignored_products_count = max(len(group) - chosen_products_count, 0)

        # select top priced products from the group
        chosen_products = group.head(chosen_products_count)
        # compute average price of top priced columns from the gorup
        avg_price_in_chosen_products = round(chosen_products['price'].mean(), 2)

        # iterate over each chosen product and add it to the top products list
        for row in chosen_products.itertuples(index=False):
            total_price = row.total_price
            top_products.append([matching_id, total_price, avg_price_in_chosen_products, 'PLN', ignored_products_count])

    return pd.DataFrame(top_products, columns=['matching_id', 'total_price', 'avg_price', 'currency',
                                                 'ignored_products_count'])


# function that saves the top products data to a csv file
def save_results(results):
    results.to_csv('data/top_products.csv', index=False)
    print("Results were successfully saved in 'top_products.csv' file")


# main function that loads the data, gets the top products and saves the data in csv
def valuation_service(data_file, currencies_file, matchings_file):
    data, currencies, matchings = load_data(data_file, currencies_file, matchings_file)
    result = get_top_priced(data, currencies, matchings)
    save_results(result)



