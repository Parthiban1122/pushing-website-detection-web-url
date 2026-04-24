import csv
import Feature_extraction as urlfeature
import trainer as tr 
import pandas as pd

def resultwriter(feature,output_dest): 
    dicts = [item[1] for item in feature]
    df = pd.DataFrame(dicts)
    df.to_csv(output_dest, index=False)

def process_URL_list(file_dest,output_dest):
    feature=[]
    with open(file_dest) as file:
        for line in file:
            url=line.split(',')[0].strip()
            malicious_bool=line.split(',')[1].strip()
            if url!='':
                print ('working on: '+url)            
                ret_dict=urlfeature.feature_extract(url)
                ret_dict['malicious']=malicious_bool
                feature.append([url,ret_dict]);
    resultwriter(feature,output_dest)

def process_test_list(file_dest,output_dest):  
    feature=[]
    with open(file_dest) as file:
        for line in file:
            url=line.strip()
            if url!='':
                print ('working on: '+url)            
                ret_dict=urlfeature.feature_extract(url)
                feature.append([url,ret_dict]);
    resultwriter(feature,output_dest)


def process_test_url(url,output_dest): 
    feature=[]
    url=url.strip()
    if url!='':
        print ('working on: '+url)            
        ret_dict=urlfeature.feature_extract(url)
        feature.append([url,ret_dict]);
    resultwriter(feature,output_dest)


def main():
        process_URL_list('URL.txt','url_features.csv')
        process_test_list("query.txt",'query_features.csv')
        tr.train('url_features.csv','url_features.csv')       
        tr.train('train_features.csv','test_features.csv')      
