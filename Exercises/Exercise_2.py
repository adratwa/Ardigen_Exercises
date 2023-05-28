"""
This Python script performs a product valuation task.

The script reads product, currency conversion rates, and matching criteria from CSV files.

It then converts product prices to PLN, calculates the total price of each product,

and identifies the top-priced products for each matching_id based on provided criteria.

The results, which include matching_id, total_price, average of total price within top-priced products per matching_id,

currency, and the count of non-selected products per matching_id, are stored in 'top_products.csv'.

Note: The CSV files are expected to be in a directory named 'data'. The script can handle FileNotFoundError.
"""

# import necessary libraries
import pandas as pd
import os


# function that reads data from csv files
def load_data(data_file, currencies_file, matchings_file):
    # directory where all data is stored
    data_directory = 'data/'
    # try/except block to handle any FileNotFoundError
    try:
        data = pd.read_csv(os.path.join(data_directory, data_file))
        currencies = pd.read_csv(os.path.join(data_directory, currencies_file))
        matchings = pd.read_csv(os.path.join(data_directory, matchings_file))
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
    # convert the currency
    data = currency_convertor_to_pln(data, currencies)
    # compute the total price for each product
    data['total_price'] = data['price'] * data['quantity']
    # merge product data with matchings data on 'matching_id'
    data = pd.merge(data, matchings, on='matching_id', how='right')
    # sort the data based on 'matching_id' and 'total_price'
    data.sort_values(['matching_id', 'total_price'], ascending=[True, False], inplace=True)

    # create price rank column in matching_id group
    data['rank_in_group'] = data.groupby('matching_id')['total_price'].rank(ascending=False)
    # count ignored products
    ignored_products = data.query('top_priced_count < rank_in_group').groupby('matching_id', as_index=False)['id'].count().rename(
        columns={'id': 'ignored_products_count'})
    # get valid rows with ignored products count
    data = data.query('top_priced_count >= rank_in_group').merge(ignored_products, how='left').fillna(value=0)
    # get average of 'total_price' by 'matching_id' for top ranked products
    chosen_avgs = data.groupby('matching_id', as_index=False).agg(
        avg_price=('total_price', 'mean'))

    # merge data
    result = data.merge(chosen_avgs, on='matching_id', how='right')

    # reorder the columns in the DataFrame
    column_order = ['matching_id', 'total_price', 'avg_price', 'currency', 'ignored_products_count']
    result = result[column_order]
    # change type from float to int
    result['ignored_products_count'] = result['ignored_products_count'].astype(int)

    return result


# function that saves the top products data to a csv file
def save_results(results):
    results.to_csv('data/top_products.csv', index=False)
    print("Results were successfully saved in 'top_products.csv' file")


# main function that loads the data, gets the top products and saves the data in csv
def valuation_service(data_file, currencies_file, matchings_file):
    data, currencies, matchings = load_data(data_file, currencies_file, matchings_file)
    result = get_top_priced(data, currencies, matchings)
    save_results(result)



