""" Connect to Database """
import boto3
from boto3.dynamodb.conditions import Key, Attr
from robot.api.deco import library
from robot.api.deco import keyword


@library
class dbKeywords:
    """ Connection class """

    def __init__(self):
        self.log = None

    @keyword
    def connect_to_db(self, table, arg1, arg2, aws_access_key, aws_secret_key, regionname):
        """
         This function connects to dynamodb
         """
        self.log = None
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
        )
        dynamodb = session.resource('dynamodb', region_name=regionname)
        # Specify the table to query
        # db_table = dynamodb.Table(table)
        db_table = dynamodb.Table(table)
        response = db_table.query(KeyConditionExpression=Key(arg1).eq(arg2))
        print("Details of Plant('", arg2, "') \n", response)

        return response

    # Alpha
    @keyword
    def connect_to_db_scan_data(self, table, arg1, arg2, arg3, aws_access_key, aws_secret_key, regionname):
        """
         This function connects to dynamodb and scan the results based on arguments
         """
        self.log = None
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
        )
        dynamodb = session.resource('dynamodb', region_name=regionname)
        db_table = dynamodb.Table(table)
        response = db_table.scan(FilterExpression=Attr(arg1).begins_with(arg2) and Attr(arg3).gte(0))
        print("Details of Plant('", arg2, "') \n", response)
        len(response)
        return response

# if __name__ == "__main__":
#     # TEST = dbKeywords()
#     # # TEST.connect_to_db('SFW_OEEIntermediateTable', 'entityId', 'KANSAS_PLANT')
#     # TEST.connect_to_db(table, arg1, arg2)
