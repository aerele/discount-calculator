from multiprocessing.sharedctypes import Value
import frappe

def dis(doc,method):
    for i in range(0,len(doc.items)):
        a= doc.items[i]["rate"] *doc.items[i]["qty"]
        dis=0.0
        if(doc.items[i]["discount_1"]):
            dis,a=find_amount(dis,a,doc.items[i]["discount_1"])
        if(doc.items[i]["discount_2"]):
            dis,a=find_amount(dis,a,doc.items[i]["discount_2"])
        if(doc.items[i]["discount_3"]):
            dis,a=find_amount(dis,a,doc.items[i]["discount_3"])
        if(doc.items[i]["discount_4"]):
            dis,a=find_amount(dis,a,doc.items[i]["discount_4"])
        if(doc.items[i]["discount_5"]):
            dis,a=find_amount(dis,a,doc.items[i]["discount_5"])
        if(doc.items[i]["discount_6"]):
            dis,a=find_amount(dis,a,doc.items[i]["discount_6"])
        doc.items[i]["discount_amount"]=dis
      
        
		   
def find_amount(dis,a,val):
    dis=dis+(a*(val/100))
    a=a-(a*(val/100))
    return dis,a
