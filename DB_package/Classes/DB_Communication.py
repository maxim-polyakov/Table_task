import logging
import warnings
import pandas as pd
from multipledispatch import dispatch
from DB_package.Classes import Connections
from DB_package.Inerfaces import IDB_Communication


class DB_Communication(IDB_Communication.IDB_Communication):
    """
    It is class for communication with a data base
    """
    warnings.filterwarnings('ignore')

    @classmethod
    @dispatch(object, object)
    def insert_to(cls, df):
        # inserting data to a database
        # configure logging settings
        logging.basicConfig(level=logging.INFO, filename="misa.log", filemode="w")
        try:
            # establish a connection to the postgresql database
            postgr_conn = Connections.PostgresConnection()
            # log that the insertion process is completed
            logging.info('The db_communication.insert_to 3 method has completed successfully')
            # insert the dataframe into the specified database table
            df.to_sql('table', con=postgr_conn.engine_remote, schema='assistant_sets',
                index=False, if_exists='append')
        except Exception as e:
            # log any exceptions that occur during execution
            logging.exception('The exception occurred in db_communication.insert_to 3: ' + str(e))

    @classmethod
    def get_data(cls, select):
#
#       Its a method for getting data from a database
        logging.basicConfig(level=logging.INFO, filename="imei.log", filemode="w")
        try:
            postgr_conn = Connections.PostgresConnection()
            df = pd.read_sql(select, postgr_conn.conn_remote)
            logging.info('The db_communication.get_data is done')
            return df
        except Exception as e:
            logging.exception(str('The exception is in db_communication.get_data ' + str(e)))


    @classmethod
    def check(cls,column,table, input_string):
#
#       Its a method for checking column in a database
        logging.basicConfig(level=logging.INFO, filename="imei.log", filemode="w")
        try:
            postgr_conn = Connections.PostgresConnection()
            df = pd.read_sql('SELECT ' + column + ' FROM assistant_sets.' + table, postgr_conn.conn_remote)
            Cdict = df[column].to_dict()

            input_array = input_string.split(' ')
            for cdictvalue in Cdict.values():
                for item in input_array:
                    if(cdictvalue == item):
                        logging.info('The db_communication.check is done')
                        return True
            logging.info('The db_communication.check is done')
            return False
        except Exception as e:
            logging.exception(str('The exception is in db_communication.checkcvalidimei ' + str(e)))