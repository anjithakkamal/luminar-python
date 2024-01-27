from itertools import count
from json import load
f=open("C:\\Users\\HP\\Desktop\\MY PYTHON\\restcountries\\data.json","r",encoding="UTF-8")
data=load(f)
#1)no of countries
print("no of countries :- ",len(data))

#2)print countries name
country_name=[c.get("name") for c in data]
print("country names :- ",country_name)

#3)print country and capital
for c in data:
    print("country :- ",c.get("name"))
    print("capital :- ",c.get("capital"))

#4)sub region of a country of Afghanistan
subregion_of_Afghanistan=[c.get("name") for c in data if c.get("subregion")=="Southern Asia"]
print("sub region of afghanistan :- ",subregion_of_Afghanistan)

#5)"population": 40218234 which country
population_filter=[c.get("name") for c in data if c.get("population")==40218234]
print("population filter :- ",population_filter)

#6)largest population of a country
# def get_population(dictionary):
#     return dictionary.get("population")
largest_population=max(data,key=lambda dictionary:dictionary.get("population"))
print("largest population :- ",largest_population.get("name"),largest_population.get("population"))

#7)smallest population of a country
smallest_population=min(data,key=lambda dictionary:dictionary.get("population"))
print("smallest population of a country :- ",smallest_population.get("name"),smallest_population.get("population"))

#8)currencies symbol of Zimbabwe

# country_symbol=[(c.get("name"),c.get("currencies").get("symbol")) for c in data]
# print("currencies symbol of Zimbabwe :- ",country_symbol)

#9)print languages of uganda
uganda_lang=[c.get("languages") for c in data if "Uganda" in c . get("name") ]
print("languages of uganda :- ",uganda_lang)
#######################################orrrrrrrrrrr
values={}
for c in data:
    lang_list=[]
    if "languages" in c:
        for l in c.get("languages"):
            lang_list.append(l.get("name"))
            values[c.get("name")]=lang_list
print("languge of uganda :- ",values.get("India"))
#10)print Taiwan transalations
Taiwan_transalations=[c.get("translations") for c in data if "Taiwan" in c.get("name")]
print("translations of taiwan :- ",Taiwan_transalations)

#11)print all independent countries
independent_countries=[c.get("name") for c in data if c.get("independent")==True]
print("independent countries:- ",independent_countries)

# 12) borders of specific countries
borders=[c.get("borders") for c in data if c.get("name")=="India"]
print("india borders :- ",borders[0])#[0] avoid list of list[[]]

# 13)borders of india
border_filter=[c.get("name") for c in data if  "borders" in c and "IND" in c.get("borders")]
print("india borders present :- ",border_filter)

# 14)country name with language name
values={}
for c in data:
    lang_list=[]
    if "languages" in c:
        for l in c.get("languages"):
            lang_list.append(l.get("name"))
            values[c.get("name")]=lang_list
print("country name with language name :- ",values)

# 15) countries with indian rupee????????????????
for c in data:
    if "currencies" in c:
        for curr in c.get("currencies"):
            if curr.get("name")=="Indian rupee":
                print("********countries with indian rupee************** :-",c.get("name"))

# 16) country with maximum area
# largest_country=max(data,key=lambda c:c.get("area"))
# print("country with maximum area",largest_country.get("name"))

# 17)all countries with multiple timezone
timezone=[c.get("name") for c in data if len(c.get("timezones"))>1]
print("all countries with multiple timezone :- ",timezone)

# 18)country name start with A
name_filter=[c.get("name") for c in data if c.get("name").startswith("A")]
print("*****COUNTRY NAME STARTS WITH A **********:- ",name_filter)

# 19)regions count
region_count=[c.get("name") for c in data if c.get("region")=="Asia"]
print("***region count***",len(region_count))
# 20)saarc
# saarc=[c.get("regionalBlocs").get("name") for c in data if c.get("acronym")=="SAARC"]
# print("**********saarc",saarc)
# values={}
# for c in data:
#     lang_list=[]
#     if "regionalBlocs" in c:
#         for l in c.get("regionalBlocs"):
#             lang_list.append(l.get("name"))
#             values[c.get("name")]=lang_list
# print("country name with language name :- ",values)

# region=[c.get("region") for c in data]
# print("region----------",count.region)

#21)  region count
region=[]
for c in data:
    region.append(c.get("region"))
print("rrrrrrrrr :-*****",region)
wc={a:region.count(a) for a in set(region)}
print("region :-",wc)

#22) india timezone
india_time_zone=[c.get("timezones") for c in data if c.get("name")=="India"]
print("india timezone :- ",india_time_zone[0][0])
afg_time_zone=[c.get("timezones") for c in data if c.get("name")=="Afghanistan"]
print("india timezone :- ",afg_time_zone[0][0])
timezone_india=india_time_zone[0][0]
timezone_afg=afg_time_zone[0][0]
india_offset=timezone_india.lstrip("UTC").replace(":",".")
afg_offset=timezone_afg.lstrip("UTC").replace(":",".")
# print("remove : to .",india_offset)
# print("remove : to .",afg_offset)
# if india_offset>afg_offset:
#     print("indian time zone ahead of afg timezone")
# else:
#     print("india time zone behind of afg timezone")
from datetime import datetime,timedelta
offset_india=timedelta(hours=float(india_offset))
print("offset india",offset_india)
offset_usa=timedelta(hours=float(afg_offset))
print("offset usa",offset_usa)
time_country1=datetime.utcnow()+offset_india
print("first",time_country1)
time_country2=datetime.utcnow()+offset_usa
print("second",time_country2)
time_diff=time_country1-time_country2
print("time difference ",time_diff.total_seconds())
if time_diff.total_seconds()>0:
    print("ahead")
else:
    print("behind")

