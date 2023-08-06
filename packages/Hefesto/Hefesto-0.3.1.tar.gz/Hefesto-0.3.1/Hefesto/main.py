import pandas as pd
from perseo.main import milisec
# from template import Template
from Hefesto.template import Template
import sys
import yaml
import math
import requests

class Hefesto():

    def __init__(self, datainput, reset = False):
        # Create an object as dictonary to reduce duplicate calls:
        self.reg = dict()

        # Import data input:
        if not reset:
            self.df_data = pd.read_csv(datainput)
        else:
            self.df_data = datainput
            return self.df_data

    def transform_shape(self,configuration, uniqid_generation= True, contextid_generation= True, clean_blanks= True):

        if type(configuration) is not dict:
            sys.exit("configuration file must be a dictionary from a Python, YAML or JSON file")

        
        # Import static template for all CDE terms:
        temp = Template.template_model
        
        # Empty objects:
        resulting_df = pd.DataFrame()
        row_df = {}

        # Iterate each row from data input
        # check each YAML object from configuration file to set the parameters
        for row in self.df_data.iterrows():

            for config in configuration.items():

                # Create a unique stamp per new row to about them to colapse:
                milisec_point = milisec()

                row_df.update({milisec_point: {'model':config[1]["cde"]}})
                
                # Add YAML template static information
                for cde in temp.items():
                    if cde[0] == row_df[milisec_point]["model"]:
                        row_df[milisec_point].update(cde[1])

                # Relate each YAML parameter with original data input
                for element in config[1]["columns"].items():
                    for r in row[1].index:
                        if r == element[1]:
                            dict_element = {element[0]:row[1][r]}
                            row_df[milisec_point].update(dict_element)

                # Delete all "empty" row from Value columns that doesnt contain value or nan
                print(row_df[milisec_point]["valueOutput"])
                if not clean_blanks:
                    final_row_df = pd.DataFrame(row_df[milisec_point], index=[1])
                    resulting_df = pd.concat([resulting_df, final_row_df])

                else:
                    if row_df[milisec_point]["valueOutput"] == None:
                        del row_df[milisec_point]

                    elif type(row_df[milisec_point]["valueOutput"]) == float:
                        if math.isnan(row_df[milisec_point]["valueOutput"]):
                            del row_df[milisec_point]
                        else:
                            final_row_df = pd.DataFrame(row_df[milisec_point], index=[1])
                            resulting_df = pd.concat([resulting_df, final_row_df])
                    else:
                        final_row_df = pd.DataFrame(row_df[milisec_point], index=[1])
                        resulting_df = pd.concat([resulting_df, final_row_df])
                    
        # uniqid (re)generation:
        resulting_df = resulting_df.reset_index(drop=True)

        if uniqid_generation:
            resulting_df['uniqid'] = ""
            for i in resulting_df.index:
                resulting_df.at[i, "uniqid"] = milisec()

        # context_id (re)generation:
        if contextid_generation:
            resulting_df['context_id'] = ""
            for i in resulting_df.index:
                resulting_df.at[i, "context_id"] = milisec()

        
        print("Structural transformation: Done")
        new = Hefesto.__init__(self, datainput= resulting_df, reset = True)
        return new

    def get_uri(self, col, ont):

        
        if not col in list(self.df_data.columns):
            sys.exit("ERROR: selected column doesnt exist")

        # Column duplication to work in new column:
        self.df_data[col+"_uri"] = self.df_data.loc[:, col]
        

        # Loop throught new column to replace current value with API term:
        for i in self.df_data[col+"_uri"].index:
            term = self.df_data.at[i,col+"_uri"]
            if term in self.reg:
                self.df_data.at[i,col+"_uri"] = self.reg[term] 

            else: # API call to OLS
                url= "http://www.ebi.ac.uk/ols/api/search?q="+ term +"&ontology=" + ont
                r = requests.get(url,headers= {"accept":"application/json"})
                data = r.json()
                # JSON navigation:
                try:
                    data_iri = data["response"]["docs"][0]["iri"]
                except IndexError:
                    data_iri = "NOT MATCH"
                # Attach new value to the Dataframe:
                self.reg[term] = data_iri
                self.df_data.at[i,col+"_uri"] = data_iri 

        print("URLs from Label calling: Done")
        new = Hefesto.__init__(self, datainput= self.df_data, reset = True)
        return new



    def get_label(self, col):

        # Column duplication to work in new column:
        self.df_data[col+"_label"] = self.df_data.loc[:, col]

        # Loop throught new column to replace current value with API term:
        for i in self.df_data[col+"_label"].index:
            term = self.df_data.at[i,col+"_label"]
            if term in self.reg:
                self.df_data.at[i,col+"_label"] = self.reg[term] 

            else: # API call to OLS
                url= 'http://www.ebi.ac.uk/ols/api/terms?iri='+ term
                r = requests.get(url,headers= {"accept":"application/json"}) # API call to OLS
                data = r.json()
                # JSON navigation:
                try:
                    data_label = data["_embedded"]["terms"][0]["label"]
                except TypeError:
                    data_label = "NOT MATCH"
                # Attach new value to the Dataframe:
                self.reg[term] = data_label
                self.df_data.at[i,col+"_label"] = data_label 

        print("Labels from URL calling: Done")
        new = Hefesto.__init__(self, datainput= self.df_data, reset = True)
        return new

    
    def replacement(self, col, key, value, duplicate = False):

        if duplicate == "True":
            # Column duplication to work in new column:
            self.df_data[col+"_dup"] = self.df_data.loc[:, col]
            self.df_data[col+"_dup"] = self.df_data[col+"_dup"].replace([key],value)
        else:
            self.df_data[col] = self.df_data[col].replace([key],value) 

        print("Replacement from " + key + "to "+ value + " at column " + col +": Done")
        new = Hefesto.__init__(self, datainput= self.df_data, reset = True)
        return new
        
# # Test
# with open("../data/CDEconfig.yaml") as file:
#     configuration = yaml.load(file, Loader=yaml.FullLoader)

# test = Hefesto(datainput = "../data/OFFICIAL_DATA_INPUT.csv")
# transform = test.transform_shape(configuration=configuration) #, clean_blanks=False
# label = test.get_label("outputURI")
# url_from_label= test.get_uri("outputURI_label","ncit")
# repl= test.replacement("outputURI_label", "Date","DateXXX", duplicate=False)
# transform.to_csv ("../data/result6.csv", index = False, header=True)