import csv as csv
import numpy as np

csv_file_object = csv.reader(open('./train.csv', 'rb'))
header = csv_file_object.next()

data=[]
for row in csv_file_object:
  data.append(row)
data = np.array(data)

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
survivor_proportion = number_survived / number_passengers

# use Numpy to select only the columns that equal male/female
women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"

# use these stats as a mask on our original train data to find survivor proportions

# select survived column for each
women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

# then find percentage of survivors
proportion_women_survived = \
    np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = \
    np.sum(men_onboard) / np.size(men_onboard)

# then print
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived


# read in test file and apply predictions
prediction_file = open('./test.csv', 'wb')
prediction_file_object = csv.writer(prediction_file)

# basic survival model says: if woman then survived, if man then dead
prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
  if row[3] == 'female':
    prediction_file_object.writerow([row[0], '1'])
  else:
    prediction_file_object.writerow([row[0], '0'])
test_file.close()
prediction_file.close()
