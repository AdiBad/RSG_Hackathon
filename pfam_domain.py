#Original edit by Gaurav Gautam and me

#Code to get domain from eggnog api

import urllib.request, json
import re

import pandas as pd
f = open("/Users/gaurav/rsg_hackathon/2_annotations_fixed.tsv",'r')
df = pd.read_csv(f, sep = "\t")

# load the gene ids we want to extract from web api
gene_ids = pd.DataFrame(df);
gene_ids = gene_ids.iloc[:,1]

for cluster in gene_ids:
    # print(cluster)
    url_try = "http://eggnogapi5.embl.de/nog_data/json/domains/"+str(cluster)
    top_dom = {}
    with urllib.request.urlopen(url_try) as url:
        data = json.loads(url.read().decode())
        data = str(data)
        print(data)
        if("[[" in data):
            l = data.split("[[")[1].split("'")[1]
            top_dom[cluster] = l

    form = {cluster:top_dom};
    f = open("/Users/gaurav/rsg_hackathon/top_domains.txt", "a")
    f.write( str(form)+ "\n");
    f.close()
