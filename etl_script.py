import pandas as pd
import ast
import sqlite3
import pickle

def read_data(path):
    return pd.read_csv(path)

def business_transformation(df, region):
    df['region'] = region
    df['total_sales'] = df['QuantityOrdered'] * df['ItemPrice']
    df['PromotionDiscount'] = df['PromotionDiscount'].apply(ast.literal_eval)
    df['discount_amount'] = df['PromotionDiscount'].apply(lambda x: pd.to_numeric(x['Amount']))
    df['net_sale'] = df['total_sales'] - df['discount_amount']
    df.drop('discount_amount',axis=1, inplace=True)
    df.drop('batch_id', axis=1, inplace=True)
    df = df.drop_duplicates(subset='OrderId')
    df_filtered = df[df['net_sale']>0]
    return df_filtered

def combine_csv(df1,df2):
    df_combined = pd.concat([df1,df2],ignore_index=True)
    return df_combined

def load_data(df, db_name='orders.db'):
    print("Loading data now")
    conn = sqlite3.connect(db_name)
    df['PromotionDiscount'] = pickle.dumps(df['PromotionDiscount'])
    df.to_sql('sales_data', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    print("Data loading completed")
    
def etl_process():
    df_a = read_data("order_region_a.csv")
    df_b = read_data("order_region_b.csv")

    df_a = business_transformation(df_a, 'A')
    df_b = business_transformation(df_b, 'B')

    df_combined = combine_csv(df_a, df_b)

    load_data(df_combined)

etl_process()
