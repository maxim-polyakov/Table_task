from DB_package.Classes import DB_Communication
import pandas as pd
import numpy as np

def parsing_tables():
    dbc = DB_Communication.DB_Communication()
    df_market = dbc.get_data('select id, name from assistant_sets.market_goods')
    df_seller = dbc.get_data('select  name, seller_name, price from assistant_sets.seller_goods')
    d = {'id': df_market['id'], 'name': df_market['name'], 'seller_price': df_seller['price'], 'seller': df_seller['seller_name']}
    df2 = pd.DataFrame(data=d)
    df2 = df2.dropna()
    dbc.insert_to(df2)
    pass

# _______________________________________________________________________________
if __name__ == "__main__":
#
#
    parsing_tables()


