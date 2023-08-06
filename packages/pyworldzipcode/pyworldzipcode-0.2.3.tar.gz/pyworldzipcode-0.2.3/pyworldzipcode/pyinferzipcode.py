# -*- coding: utf-8 -*-
# git filter-branch --tree-filter "rm -rf pyzipcode/allCountries.txt" HEAD
# git filter-branch -f  --index-filter "git rm --cached --ignore-unmatch pyzipcode/allCountries.txt"
# git filter-branch -f --index-filter "git rm --cached --ignore-unmatch fixtures/11_user_answer.json"
# GB is delivery is pending
# git prune -n | git cat-file -p 9cc84ea9b4d95453215d0c26489d6a78694e0bc6
# py -m pip install --upgrade build;py -m build;py -m twine upload --repository testpypi dist/*;
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
import pandas as pd
from typing import Union
import os
current_path = os.path.dirname(os.path.realpath(__file__))

__version__ = "0.1.9"
__author__ = "Dalwinder singh"

val_countries = ["AD", "AR", "AS", "AT", "AU", "AX", "AZ", "BD", "BE", "BG", "BM", "BR", "BY", "CA", "CH", "CL", "CO",
                "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EE", "ES", "FI", "FM", "FO", "FR", "GB", "GF", "GG", "GL",
                "GP", "GT", "GU", "HR", "HU", "IE", "IM", "IN", "IS", "IT", "JE", "JP", "KR", "LI", "LK", "LT", "LU",
                "LV", "MC", "MD", "MH", "MK", "MP", "MQ", "MT", "MW", "MX", "MY", "NC", "NL", "NO", "NZ", "PE", "PH",
                "PK", "PL", "PM", "PR", "PT", "PW", "RE", "RO", "RS", "RU", "SE", "SG",
                "SI", "SJ", "SK", "SM", "TH", "TR", "UA", "US", "UY", "VA", "VI", "WF", "YT", "ZA"]


class WorldPostalSearch(object):
    # def __init__(self):
    #     self.df = pd.read_csv(current_path + "/world_postal.zcsv",compression="zip").drop("Unnamed: 0", 1)
    #
    # def break_data(self):
    #   df = self.df
    #   df["postal_code"] = df["postal_code"].astype(str)
    #   df["country_code"] = df["country_code"].astype(str)
    #   df["admin_code1"] = df["admin_code1"].astype(str)
    #   df["admin_name1"] = df["admin_name1"].astype(str)
    #   df["admin_name2"] = df["admin_name2"].astype(str)
    #   df["admin_name3"] = df["admin_name3"].astype(str)
    #   df["place_name"] = df["place_name"].astype(str)
    #   print(df.shape,df["country_code"].unique)
    #
    #   for i in df["country_code"].unique():
    #       print(i)
    #
    #       df1 = df[df["country_code"] == i]
    #       df1.to_csv(current_path + "/"+i+".zcsv",compression="zip", index=False)
    #       print(df1.shape)

    def valid_countries(self):
        return val_countries

    def getdf(self, countries: Union[list, str]):
        if isinstance(countries, list):
            countries = countries
        if isinstance(countries, str):
            countries = [countries]
        df_list = []
        for i in countries:
            if i in val_countries:
                df_i = pd.read_csv(current_path + "/" + i + ".zcsv", compression="zip", dtype=str)#.replace(pd.NA, None)

                df_i["postal_code"] = df_i["postal_code"].astype(str)
                df_i["country_code"] = df_i["country_code"].astype(str)
                df_i["admin_code1"] = df_i["admin_code1"].astype(str)
                df_i["admin_name1"] = df_i["admin_name1"].astype(str)
                df_i["admin_name2"] = df_i["admin_name2"].astype(str)
                df_i["admin_name3"] = df_i["admin_name3"].astype(str)
                df_i["place_name"] = df_i["place_name"].astype(str)
                df_list.append(df_i)
        if len(df_list) == 0:
            df = pd.DataFrame()
        else:
            df = pd.concat(df_list, axis=0)
        return df

    def bulkget(self, zip_country_tuple_list):
        country_list = list(set([i[1] for i in zip_country_tuple_list]))
        postal_code_list = [i[0] for i in zip_country_tuple_list]
        df = self.getdf(country_list)
        if df.empty:
            return [{}]
        df = df[df["postal_code"].isin(postal_code_list)].drop_duplicates()
        if df.empty:
            return [{}]
        else:
            df.columns = ["postal_code", "country_code",  "state_name", "state_code", "admin_name2",
                          "admin_name3", "place_name"]
        return df.to_dict("records")

    def _get(self, pincode: Union[list, str], country: str):
        postal_code_list=[]
        if isinstance(pincode, list):
            postal_code_list = pincode
        if isinstance(pincode, str):
            postal_code_list = [pincode]
        df = self.getdf([country])
        if df.empty:
            return [{}]
        df = df[df["postal_code"].isin(postal_code_list)]
        if df.empty:
            return [{}]
        else:
            df.columns = ["postal_code", "country_code", "state_name", "state_code", "admin_name2",
                         "admin_name3", "place_name"]
            return df.to_dict("records")

#print(WorldPostalSearch().bulkget([("AD100", "AD"), ("AD1000", "AD"), ("AD100", "AD"), ("AD200", "AD")]))
#
# print(WorldPostalSearch()._get("AD100", "AD"))
# print(WorldPostalSearch().bulkget([("AD100", "AD")]))
# WorldPostalSearch().break_data()

