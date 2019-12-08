#Original edit by Nil Fernandez Lojo

from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from joblib import dump, load
import re
import numpy as np
from collections import Counter


data_file = "data_repartition_duplicated.tsv"
f=open(data_file, "r")
f1= f.readlines()
f.close() 

y = []
class_list_families = []
list_families = []
data_input = []
seq_identity = []
count_median = []
count_var = []
domain_name = []

for line in f1:
	data_input = re.split("\t+", line)
	list_families.append(data_input[0])
	y.append(data_input[1])
	class_list_families.append(int(data_input[2]))
	seq_identity.append(float(data_input[3])) 
	count_median.append(float(data_input[4])) 
	count_var.append(float(data_input[5])) 
	domain_name.append(data_input[6])
	#other data

domain_name_np = np.array(domain_name)
domain_name_np_2, indices = np.unique(domain_name_np, return_inverse=True)
domain_name = indices

index_train = [index for index, value in enumerate(class_list_families) if value == 0]
index_cross_validation = [index for index, value in enumerate(class_list_families) if value == 1]
index_test = [index for index, value in enumerate(class_list_families) if value == 2]


list_families_train = []
y_train = []
seq_identity_train = []
count_median_train = []
count_var_train = []
domain_name_train = []

list_families_cross_validation = []
y_cross_validation = []
seq_identity_cross_validation = []
count_median_cross_validation = []
count_var_cross_validation = []
domain_name_cross_validation = []

list_families_test = []
y_test = []
seq_identity_test = []
count_median_test = []
count_var_test = []
domain_name_test = []

for i in range(len(class_list_families)):
	if (class_list_families[i] == 0):
		list_families_train.append(class_list_families[i])
		y_train.append(y[i])
		seq_identity_train.append(seq_identity[i])
		count_median_train.append(count_median[i])
		count_var_train.append(count_var[i])
		domain_name_train.append(domain_name[i])
	elif (class_list_families[i] == 1):
		list_families_cross_validation.append(class_list_families[i])
		y_cross_validation.append(y[i])
		seq_identity_cross_validation.append(seq_identity[i])
		count_median_cross_validation.append(count_median[i])
		count_var_cross_validation.append(count_var[i])
		domain_name_cross_validation.append(domain_name[i])
	else:
		list_families_test.append(class_list_families[i])
		y_test.append(y[i])
		seq_identity_test.append(seq_identity[i])
		count_median_test.append(count_median[i])
		count_var_test.append(count_var[i])
		domain_name_test.append(domain_name[i])

#X split in 3 data sets

y_train_df =pd.DataFrame({'labels':y_train})
y_cross_validation_df =pd.DataFrame({'labels':y_cross_validation})
y_test_df =pd.DataFrame({'labels':y_test})

# X_train_df = pd.DataFrame({'seq_identity':seq_identity_train, 'count_median':count_median_train, 'count_var':count_var_train})
# X_cross_validation_df = pd.DataFrame({'seq_identity':seq_identity_cross_validation, 'count_median':count_median_cross_validation, 'count_var':count_var_cross_validation})
# X_test_df = pd.DataFrame({'seq_identity':seq_identity_test, 'count_median':count_median_test, 'count_var':count_var_test})

X_train_df = pd.DataFrame({'seq_identity':seq_identity_train, 'count_median':count_median_train, 'count_var':count_var_train, 'domain_name':domain_name_train})
X_cross_validation_df = pd.DataFrame({'seq_identity':seq_identity_cross_validation, 'count_median':count_median_cross_validation, 'count_var':count_var_cross_validation, 'domain_name':domain_name_cross_validation})
X_test_df = pd.DataFrame({'seq_identity':seq_identity_test, 'count_median':count_median_test, 'count_var':count_var_test, 'domain_name':domain_name_test})


#x = np.chararray(y) 
#print(np.unique(x)) 
#print(X_train_df.loc[0:10,:])


clf=RandomForestClassifier(n_estimators=1000)
clf.fit(X_train_df,y_train_df)
#dump(clf, 'fitted_model.joblib') 
#clf2 = load('fitted_model.joblib') 
y_pred=clf.predict(X_cross_validation_df)
y_pred_test=clf.predict(X_test_df)

print("Accuracy:",metrics.accuracy_score(y_cross_validation_df, y_pred))
print("Accuracy test :",metrics.accuracy_score(y_test_df, y_pred_test))

label_names = ['J', 'A','K','L','B', 'D', 'Y', 'V', 'T', 'M', 'N', 'Z', 'W', 'U', 'O', 'C', 'G', 'E', 'F', 'H', 'I', 'P', 'Q', 'R']
letter_counts = Counter(y_train)
majority_vote = []
for i in range(len(y_pred)):
	majority_vote.append('K')

print("Accuracy majority vote:",metrics.accuracy_score(y_cross_validation_df, majority_vote))

print(len(y_train), len(y_cross_validation_df))

