from pyspark.sql.types import  StringType, StructType, StructField, IntegerType,  BooleanType, TimestampType, ArrayType, DateType, LongType, DoubleType, ByteType
from pyspark.sql.functions import  col, to_timestamp,  to_date,  length 
from pyspark.sql import DataFrame




def convert_to_string_type(df:DataFrame, columns):
    """Method to convert columns to stringType

    Args:
        df (dataframe): dataframe 
        columns (array): contain an array of columns to be changed

    Raises:
        Exception: throw exception in case of error

    Returns:
        dataframe: dataframe modified
    """
    try:
        for column in columns:
            df = df.withColumn(column, col(column).cast(StringType()) )
        return df
    except Exception as e:
        raise KeyError(e)    



def convert_to_time_stamp_type(df: DataFrame,columns):
    """Method to convert  columns to time_stamp

    Args:
        df (dataframe): dataframe
        columns (array): contain an array of columns to be changed
    
    Raises:
        Exception: throw exception in case of error
        
    Returns:
        dataframe: dataframe modified
    """
    try:
        for column in columns:
            val = df.filter(length(col(column)) >=17)
            if val.count()>=1:
                df = df.withColumn(column,  to_timestamp(col(column),"MM/dd/yyyy HH:mm:ss"))
            else:
                val = df.filter(length(col(column)) >10)
            if val.count()>=1:
                df = df.withColumn(column,  to_timestamp(col(column),"d/M/yy H:mm"))
            else:
                df = df.withColumn(column,  to_timestamp(col(column),"dd/MM/yyyy")  )
        return df;  
    except Exception as e:
        raise KeyError(e)



def convert_to_date_type(df:DataFrame, columns):
    """Method to convert columns to date

    Args:
        df (dataframe): dataframe
        columns (array): contain an array of columns to be changed
    
    Raises:
        Exception: throw exception in case of error
    
    Returns:
        dataframe: dataframe modified
    """
    try:
        for column in columns:
            df = df.withColumn(column, to_date(col(column).cast(StringType()) , 'yyyyMMdd'))
        return df
    except Exception as e:
        raise KeyError(e)   
 
 
    
def convert_array_to_string(array):
    """Method to convert _array to string

    Args:
        array (array): array

    Raises:
        Exception: throw exception in case of error
        
    Returns:
        String: return a string separated with commas
    """   
    try: 
        return ','.join(map(str, array))   
    except Exception as e:
        raise Exception(e)
    
    
def check_header_schema(struct_df:StructType): 
    """Method to validate the fields in StructField
    Args:
        struct_df (StructType): StructType to be evaluated 

    Raises:
        Exception: lauch exception in case of error

    Returns:
        boolean: boolean in case of not satisfy the validation of fields arguments
    """    
    try:
        flag=True
        if len(struct_df.fieldNames()) == 0: 
            flag=False
            
        return flag
    except Exception as e:
        raise Exception(e)
    

def check_data_file(dataFrame: DataFrame):
    """Method to check if a dataframe have information
    Args:
        dataFrame (dataframe): dataframe

    Raises:
        Exception: launch exception in case of error

    Returns:
        boolean: boolean in case of not satisfy the validations of records
    """
    try:
         flag=True
         data = dataFrame.select('*').limit(1)
         if data.count() <= 0 :
             flag= False
         
         return flag
    except Exception as e:
        raise Exception(e)
    

    
def check_header_names_schema(struct_conf:StructType, struct_not_conf:StructType)->list:
    """Method to find or compare column names in a StructType configured in a dataframe
    Args:
        struct_conf (StructType): StructType configurations in columns
        struct_not_conf (StructType): StructType not configurated
   
    Raises:
        Exception: launch exception in case of error
   
    Returns:
        list: an array of columns names not found.
    """    
    try:
        colums_failed=[]
        fields_conf = struct_conf.fieldNames()
        fields_not_conf = struct_not_conf.fieldNames()
        
        for column_in_file in fields_not_conf:
            if column_in_file not in fields_conf: 
                colums_failed.append(column_in_file)
        
        return colums_failed
    except Exception as e:
        raise Exception(e)
    

    
def convert_to_schema(values: dict) -> StructType:
    """Method to build a schema for table from a dict
    
    Raises:
        Exception: launch exception in case of error
        
    Returns:
        StructType: the schema parametrized
    """    
    fields = []
    try:
        for k,v in values.items():
          fields.append(StructField(k, __str_to_class(v), True))

        schema = StructType(fields)
        return schema
    
    except Exception as e:
      raise Exception(e)
        
        
        
def __str_to_class(val):
    """Method to get typeobject in schema  
    Args:
        val (StructField): type struct in column
    Returns:
        StructFiled: the struct field in column
    """    
    obj = None
    
    if val == 'IntegerType()':
      obj = IntegerType()
    elif val == 'StringType()':
      obj = StringType()
    elif val == "TimestampType()" :
      obj = TimestampType()
    elif val == "LongType()" :
      obj = LongType()
    elif val == "DoubleType()" :
      obj = DoubleType()
    elif val == "ByteType()" :
      obj = ByteType()
    elif val == "BooleanType()" :
      obj = BooleanType()
    elif val == "ArrayType()" :
      obj = ArrayType()
    elif val == "DateType()" :
      obj = DateType()
      
    return obj



def check_header_order_schema(struct_conf:StructType, struct_not_conf:StructType):
    """Method to check the order of headers in the file readed and configured

        struct_conf (StructType): StructType configurations in columns
        struct_not_conf (StructType): StructType not configurated
   
    Raises:
        Exception: launch exception in case of error
   
    Returns:
        boolean: boolean in case of not satisfy the names colums configurated
    """
    try:
        flag = True
        tuple_struct_conf = tuple(struct_conf.fieldNames())
        tuple_struct_not_conf = tuple(struct_not_conf.fieldNames())
        
        if tuple_struct_conf != tuple_struct_not_conf:
            flag=False
        
        return flag
    except Exception as e:
        raise Exception(e)