import json
from .text_tools import re_found, re_findall
#import .fs_tools as fs_tools

def getdicv(dic, key):
  for k,v in dic.items():
    if k == key:
      return v
  return None

def walk_dic(dic):
  if isinstance(dic, dict): 
    for k, v in dic.items():
      if isinstance(v, dict) or isinstance(v, list):
        walk_dic(v)
      else:
        print("{0} : {1}".format(k, v))
  elif isinstance(dic, list):
    for d in dic:
      walk_dic(d)
  
def walk_dic1(dic, result):
  updated_result = []
  if result is None:   result = []
  if isinstance(dic, dict): 
    for k, v in dic.items():
      #"weight(course.text_search_blob.stemmed:health in 344)
      if k=="description" and re_found("(weight\([^()]+\))", v) == True:
        desc_found = re_findall ("(weight\([^()]+\))" , v)
        result.append(desc_found[0] + " : value =" + str(dic["value"]))
      if isinstance(v, dict) or isinstance(v, list):
        updated_result = walk_dic1(v,result)
    return result
  elif isinstance(dic, list):
    for d in dic:
      updated_result = walk_dic1(d, result)
  else:
    return updated_result

if __name__ == "__main__": 
  a = {"a.b" : "123"}
  print (getdicv(a,"a.b"))

  with open("R:/1.json", "r") as content:
    dic = json.loads(content.read())

  result = []
  result = walk_dic1(dic, result)
  print ("\n".join(result))

  pass