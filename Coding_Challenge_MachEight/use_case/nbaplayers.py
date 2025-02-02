from more_itertools import locate
import requests
from config.utils import NO_RECORDS_FOUND_MESSAGE

class RecoveryData:
    
    def __init__(self, inches:int):
        
        self.limitInches = inches
        self.data_response = None      
        self.indexedList = None
        self.valuesBase = None
        self.valuesFromIndex = None
        self.filterCombinations = list()
        self.combinationsFiltered = list()
        self.cleanCombinations = dict()
        self.name = None
        self.list_names = list()


    def get_response_data(self, url:str) -> list:
        """
        return the response data from the url
        """
        
        try:
            response = requests.get(url).json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        else:
            self.data_response = response.get('values')
            return self.data_response
    
    def create_dict_with_index(self, data_reponse:list) -> dict:
        """
        creates and returns a dict adding index values for every dict in the response of get_response_data
        """
        
        self.indexedList = {index: value for index, value in enumerate(data_reponse)} if data_reponse else {}
    
        return self.indexedList
    
    def get_index_with_inches_from_dict(self, indexedList:dict) -> list:
        """
        creates and returns a list of dicts with the inch values from the response of get_response_data
        """
               
        self.valuesBase = [{index:int(value.get('h_in'))} for index, value in indexedList.items()] if indexedList else {}
        
        return self.valuesBase
    
    def get_values_from_index(self, indexedList:dict) -> list:
        """
        creates and returns a list with the inches values from create_dict_with_index
        """
        
        self.valuesFromIndex = [int(value.get('h_in')) for index, value in indexedList.items()]
        
        return self.valuesFromIndex
    
    
    def get_filter_combinations(self, indexInchesDict:dict) -> list[tuple]:
        """
        creates and returns a list of tuples with the combinations that matches the limitInches
        """      
         
        indexKey = list(indexInchesDict.keys())[0]
        actualValue = list(indexInchesDict.values())[0]
        searchNumber = self.limitInches - actualValue

        matchValues = (list(locate(self.valuesFromIndex, lambda x:  x == searchNumber)))
        finalMatches = [(valueKey, indexKey) if valueKey <= indexKey else (indexKey, valueKey) for valueKey in matchValues if indexKey != valueKey]

        self.filterCombinations += finalMatches

        return self.filterCombinations
    
    
    def get_combinations_filtered(self, valuesBase:list) -> list:
        """
        creates and returns a list with the combinations filter that matches the get_filter_combinations
        """    
                
        self.combinationsFiltered = list(filter(self.get_filter_combinations, valuesBase)) if valuesBase else []
        
        return self.combinationsFiltered 
    
    def get_clean_and_order_combinations(self, filterCombinations:list) -> list:
        """
        creates and returns a list with the combinations filtered, remove duplicates for avoid repeated data and order list by value
        """            
        self.cleanCombinations = list(set(filterCombinations))
        self.cleanCombinations.sort() if filterCombinations else []
        
        return self.cleanCombinations

 
    def get_name(self, value) -> str:
        """
        creates and returns a string from the name of the player
        """             
        self.name =  f"{self.indexedList.get(value).get('first_name')} {self.indexedList.get(value).get('last_name')}" if value else None

        return self.name
    
    def get_list_names(self, cleanCombinations:list) -> list:
        """
        creates and returns a the list of string with the couple of names of the players
        """            
        self.list_names = [f'- {self.get_name(valor[0])}         {self.get_name(valor[1])}' for valor in cleanCombinations] if cleanCombinations else []

        self.list_names.insert(0,f'app {self.limitInches}') if self.list_names else None
        
        return self.list_names
        
    
    def get_process_data(self, url:str) -> list:
        """
        process the request and returns the response to the api
        """            
        self.get_response_data(url)
        self.create_dict_with_index(self.data_response)
        self.get_index_with_inches_from_dict(self.indexedList)
        self.get_values_from_index(self.indexedList)
        self.get_combinations_filtered(self.valuesBase)
        self.get_clean_and_order_combinations(self.filterCombinations)
        self.get_list_names(self.cleanCombinations)
                                
        return  self.list_names if self.list_names else f'app {self.limitInches} - {NO_RECORDS_FOUND_MESSAGE}'