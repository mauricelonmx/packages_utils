#Class that insert and control the log info that is releated to the PipeLine
import time
import datetime
from datetime import date

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, TimestampType,ArrayType
from pyspark.sql import SparkSession

## Información del pipeline
__table = None
__source_type = None
__pipeline_name = None

## Información de la data
__file_configuration = None
__source = None
__destiny_schema = None
__destiny_table = None
__beginning_time = None
__data_date = None

##Información del proceso
__status = None
__comments = ""
__num_records = None
__filters = None

#init sesssion
spark = SparkSession.builder.appName("ETL_Logs").getOrCreate()
  
def create_logs(schema = "bronze", etl_pipeline_log_table = None, pipeline_name = None, source_type = None):
    """ 
    Method to initiate the table where the information related to the pipeline will be store.
    
    Args:
        schema (string): schema where the log table is. 
        etl_pipeline_log_table (string): name of the table
        pipeline_name (string): name of the Pipelien. It can be iddentify the version
        source_type (string): type of load, e.g. Batch, streaming, etc
    """
    global __table
    __table =  schema + '.' + etl_pipeline_log_table
    global __pipeline_name
    __pipeline_name = pipeline_name
    global __source_type
    __source_type = source_type
    global __beginning_time
    __beginning_time=time.time()

def set_statusTrue():
    """ 
    Method to set status True of the load process.
    """
    global __status
    __status = True

def set_statusFalse():
    """ 
    Method to set status False of the load process.
    """
    global __status
    __status = False

def get_status():
    """ 
    Method that returns the status of the process

    Returns:
        Boolean: return the status of the process
    """
    return __status

def set_num_records(num_records):
    """ 
    Method to set status of the number of recrods that where loaded.

    Args:
        num_records (Integer): Number of records that where loaded
    """
    global __num_records
    __num_records = num_records 

def set_filters(filters):
    """ 
    Method to set filters that are being used in the process

    Args:
        filters (Array): Array of dict with the filter that are being used
    """
    global __filters
    __filters = filters

def set_destiny_schema(destiny_schema):
    """ 
    Method to set the schema where the table is being stored

    Args:
        destiny_schema (String): Name of the schema where the data is loaded 
    """
    global __destiny_schema
    __destiny_schema = destiny_schema

def set_destiny_table(destiny_table):
    """ 
    Method to set the name of the table where the table is being stored

    Args:
        destiny_table (String): Name of the table where the data is loaded
    """
    global __destiny_table
    __destiny_table = destiny_table

def set_source(source):
    """ 
    Method to set the source where the data were trasnfered
    Args:
        source (String): Name of the file or table
    """
    global __source
    __source = source


def add_comment(msg, func="", level="INFO"):
    """ 
    Method to add comments of the process

    Args:
        msg (String): Message that want to be save on the table to indicate the error
        func (String): Function where the comment was generated
        level (String): Criticity level of the message, DEBUG, INFO, WARNING, ERROR
    """
    global __comments
    comment_time = datetime.datetime.fromtimestamp(time.time())
    __comments += "[{}][{}][Function - {}]: {}.\n".format(comment_time,level,func,msg)

def set_info_load(file_configuration=None, source=None, destiny_schema=None, destiny_table=None, data_date=None, filters = None):
    """ 
    Method that add the information of the data source that were processed. It is call to initializate the variables, like time where it begins
    
    Args:
        file_configuration (String): Path of the JSON Configuration of the table
        source (String): Path of the input source, it could be a file or table
        destiny_schema (String): Name of the schema where the data is loaded 
        destiny_table (String): Name of the table where the data is loaded
        filters (array): List of filters, like columns that are Timestamp, partition date
        data_date (String): Date of the data
    """
    global __file_configuration
    __file_configuration=file_configuration
    global __source
    __source = source
    global __destiny_schema
    __destiny_schema=destiny_schema
    global __destiny_table
    __destiny_table=destiny_table
    global __beginning_time
    __beginning_time=time.time()
    global __data_date
    __data_date = data_date
    global __status
    __status = True
    global __comments
    __comments= ""  
    global __num_records
    __num_records = None
    global __filters
    __filters = filters 

def insert_elt_logs():
    """
     Method to save the process result in the table that where configurate it.
    """
    try:
        df = get_df()
        df.write.mode('append').option("mergeSchema", "true").format('delta').saveAsTable(__table)
    except Exception as e:
        output = f"{e}"
        #raising an exception
        raise Exception("ERROR: writing logs - insert_elt_logs",output)
      
def get_data():
    """ 
    Method that returns an array with the process information, like beginning time, ending time, table's name, etc.
    
    Returns:
        Array: return an array with all data structured
    """
    today = int(date.today().strftime("%Y%m%d"))
    data = [(today,
        __source_type,
        __pipeline_name,
        __file_configuration,
        __source,
        __destiny_schema,
        __destiny_table,
        __data_date,
        datetime.datetime.fromtimestamp(__beginning_time),
        datetime.datetime.fromtimestamp(time.time()),
        __status,
        __comments,
        __num_records,
        (__filters))]
    return data

def get_schema():
    """ 
    Method that returns a StructType with the schema of the log table
    
    Returns:
       StructType: return a StructType with the table's schema
    """
    schema = StructType([ 
        StructField("partition_date",IntegerType(),True),
        StructField("source_type",StringType(),True),
        StructField("pipeline_name",StringType(),True),
        StructField("file_configuration",StringType(),True),
        StructField("source", StringType(), True),
        StructField("destiny_schema", StringType(), True),
        StructField("destiny_table", StringType(), True),
        StructField("data_date", StringType(), True),
        StructField("beginning_time", TimestampType(), True),
        StructField("ending_time", TimestampType(), True),
        StructField("status",BooleanType(),True),
        StructField("comments", StringType(), True),
        StructField("num_records", IntegerType(), True),
        StructField("filters",ArrayType(
            StructType([
               StructField('partition', StringType(), True),
               StructField('field_to_string', StringType(), True),
               StructField('field_to_date', StringType(), True),
               StructField('field_to_stamp', StringType(), True)
               ])
            ),True)
        ])
    return schema
      
def get_df():
    """ 
    Method that returns the dataframe to be stored in the tble
    
    Returns:
        Dataframe: return a datafrema with the table's schema and process data
    """
    df = spark.createDataFrame(data = get_data(),schema = get_schema())  
    return df


