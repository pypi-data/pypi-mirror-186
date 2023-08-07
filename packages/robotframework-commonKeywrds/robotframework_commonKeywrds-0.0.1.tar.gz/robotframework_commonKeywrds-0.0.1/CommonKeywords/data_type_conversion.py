import json
import operator
import os
import random
import string
import datetime
import urllib
import math
import pandas as pd
from robot.api.deco import library
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class data_type_conversion:
    """ Connection class """

    def __init__(self):
        self.log = None

    @keyword
    def list_to_dict(self, list1, list2):
        """Simple method to convert list to dict"""
        self.log = None
        dictionary = dict(zip(list1, list2))
        print(dictionary)
        return dictionary

    @keyword
    def index_list_of_duplicates(self, seq, item):
        """Simple method to get index"""
        self.log = None
        start_at = -1
        locs = []
        while True:
            try:
                loc = seq.index(item, start_at + 1)
            except ValueError:
                break
            else:
                locs.append(loc)
                start_at = loc
        return locs

    @keyword
    def repeated_words(self):
        """ Create repeatedwords """
        self.log = None
        word = "P" * 255
        return word

    @keyword
    def repeated_words_api(self):
        """ Create repeatedwords for api """
        self.log = None
        word = "P" * 257
        return word

    def callepoch_converter(self, adddays=0):
        """
        Convert Date to Epoch
        Arguments:addDays: Number of days to be added in current date
        """
        self.log = None
        newdate = datetime.date.today() + datetime.timedelta(days=adddays)
        strdate = newdate.strftime('%Y-%m-%d')
        epoch = datetime.datetime.strptime(strdate, '%Y-%m-%d')
        epochmsec = epoch.timestamp() * 1000
        return epochmsec

    @keyword
    def get_random_name(self, length):
        """It will return random  name"""
        self.log = None
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
        # print("Random string of length", length, "is:", result_str)

    @keyword
    def downloadfile(self, fileurl, path):
        """Download File from URL to specific location """
        os.environ["PYTHONHTTPSVERIFY"] = "0"
        self.log = None
        url = fileurl
        urllib.request.urlretrieve(url, path)

    @keyword
    def Updatingvalue_CSV(self, filepath, Columnname):
        """ update csv """
        self.log = None
        # reading the csv file
        df = pd.read_csv(filepath)
        df.loc[1, Columnname] = '-4'
        df.to_csv(filepath, index=False)
        print(df)

    @keyword
    def Updatemodifydata_CSV(self, filepath, Columnname):
        """ update csv """
        self.log = None
        # reading the csv file
        df = pd.read_csv(filepath)
        df.loc[1, Columnname] = 'data'
        df.to_csv(filepath, index=False)
        print(df)

    @keyword
    def dataTraceabilityFunction(self, filepath, labelname):
        """ dataTraceabilityFunction """
        self.log = None
        with open(filepath, encoding='utf8') as json_file:
            d1 = {"----------------": [labelname]}
            df1 = pd.DataFrame(d1)
            df1.to_csv(filepath, index=False, mode='a')
            json_data = json.load(json_file)
            # df = pd.DataFrame(json_data, index=[0])
            df = pd.DataFrame.from_dict(json_data)
            df.to_csv(filepath, mode='a')

    @keyword
    def toWriteDateAndTestName(self, filepath, date, testname):
        """ toWriteDateAndTestName """
        self.log = None
        with open(filepath, 'a', encoding='utf8') as file:
            file.write("\n")
            file.write(date)
            file.write(testname)
            file.write("\n")

    @keyword
    def toWriteToCSV(self, filepath, labelname, data):
        """ toWriteToCSV """
        self.log = None
        with open(filepath, 'a', encoding='utf8') as file:
            file.write("---------------")
            file.write("\n")
            file.write(labelname)
            file.write(":")
            file.write(data)
            file.write("\n")

    @keyword
    def convert(self, a):
        """ convert """
        self.log = None
        it = iter(a)
        res_dct = dict(zip(it, it))
        return res_dct

    @keyword
    def sorted_dict(self, d, number):
        """ sorted_dict """
        self.log = None
        num = int(number)
        sorted_d = dict(sorted(d.items(), key=operator.itemgetter(num)))
        return dict(sorted_d)

    @keyword
    def sorted_reversedict(self, d, number):
        """ sorted_reversedict """
        self.log = None
        num = int(number)
        sorted_d = dict(sorted(d.items(), key=operator.itemgetter(num), reverse=True))
        return dict(sorted_d)

    @keyword
    def calculatesqrt(self, number):
        """calculate sqrt"""
        self.log = None
        return math.sqrt(number)

    @keyword
    def createJsonFile(self, Filepath, Data):
        """ createJsonFile """
        self.log = None
        with open(Filepath, "r+", encoding='utf8') as file:
            file.truncate()
            datainput = json.dumps(Data, cls=DecimalEncoder)
            file.write(datainput)
            file.close()
