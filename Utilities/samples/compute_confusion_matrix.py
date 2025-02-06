import pandas as pd
import math

field_description_column_01, field_description_column_02, field_description_column_03 = 'predicted: no', 'predicted: yes', 'total_row'
field_description_row_01, field_description_row_02, field_description_row_03 = 'actual: no', 'actual: yes', 'total_column'
# TN, FP = column_01[0], column_02[0]
# FN, TP = column_01[1], column_02[1]
"""
[8,4,92,96], [2,1,98,99], [2,0,98,100], [1,0,99,100], [0,0,100,100]
scores = [0.65, 0.9, 0.96, 0.98, 0.99]
"""
TN, FN = 50, 5
FP, TP = 10, 100
TP = 63;	FN = 37
FP = 28;	TN = 72
TP = 20;	FN = 10
FP = 180;	TN = 1820
TP = 8;	FN = 92
FP = 4;	TN = 96
"""
TP = 2;	FN = 98
FP = 1;	TN = 99
"""
column_01 = [TN, FN, 0]
column_01[2] = column_01[0] + column_01[1]
column_02 = [FP, TP, 0]
column_02[2] = column_02[0] + column_02[1]
column_03 = [(column_01[0] + column_02[0]), (column_01[1] + column_02[1]), (column_01[2] + column_02[2])]

data = {field_description_column_01:column_01, field_description_column_02:column_02, field_description_column_03:column_03 }

df = pd.DataFrame(data, index=[field_description_row_01,field_description_row_02,field_description_row_03])
print (df)

total = column_03[2]
actual_yes_total = column_03[1]
actual_no_total = column_03[0]
predicted_yes_total = column_02[2]
predicted_no_total = column_01[2]

print("Accuracy (ACC): Overall, how often is the classifier correct? ", (TP+TN)/total )
print("Misclassification Rate (aka 'Error Rate', 1 - Accuracy): Overall, how often is it wrong? ", (FP+FN)/total )
recall = (TP/actual_yes_total); TPR = recall; sensitivity = recall
precision = (TP/predicted_yes_total); PPV = precision
FPR = (FP/actual_no_total)
print("True Positive Rate (TPR aka 'Sensitivity' or 'Recall'): When it's actually yes, how often does it predict yes? ", recall)
print("False Positive Rate ((FPR), Fall-out, probability of false alarm): When it's actually no, how often does it predict yes? ", FPR)
TNR = (TN/actual_no_total); specificity = TNR
print("True negative rate (TNR), Specificity (SPC), (1 - False Positive Rate): When it's actually no, how often does it predict no? ", TNR)
print("Precision, Positive predictive value (PPV): When it predicts yes, how often is it correct? ", precision )
print("False omission rate (FOR): ", (FP/predicted_no_total)) # 1 - NPV
print("False discovery rate (FDR): ",(FP/predicted_yes_total) )
NPV = (TP/predicted_no_total)
print("Negative predictive value (NPV): ", NPV)
print("Prevalence: How often does the yes condition actually occur in our sample? ", (actual_yes_total/total) )
FNR = (FN/actual_yes_total)
print("False negative rate (FNR), Miss rate: ", FNR)
print("F1 score = ", (2/((1/recall)+(1/precision))))
print("Negative predictive value (NPV): ", (TN / (FN + TN)))
LR_plus, LR_minus = (TPR/FPR), (FNR/TNR)
print("Positive likelihood ratio (LR+): ", LR_plus)
print("Negative likelihood ratio (LR−): ", LR_minus)
print("Diagnostic odds ratio (DOR): ", (LR_plus/LR_minus))
print("(FPR, TPR):", FPR, ", ", TPR)
MCC = ((TP*TN) - (FP*FN)) / math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
print("Matthews Correlation Coefficient (MCC) : ", MCC)
BM = TPR + TNR - 1
print("Informedness or Bookmaker Informedness (BM): ", BM)
MK = PPV + NPV - 1
print("Markedness (MK): ", MK)

score_AUC = sensitivity*(1-specificity)*(1/2)
print("score_AUC: ", score_AUC)

print("Bayesian Probability:")
field_description_column_01, field_description_column_02, field_description_column_03 = 'Actual: +ve (1%)', 'Actual: -ve (99%)', 'total_row'
field_description_row_01, field_description_row_02, field_description_row_03 = 'Test: +ve', 'Test: -ve', 'total_column'
rate_population_positive = 0.01
rate_population_negative = 1 - rate_population_positive
probability_not_H = rate_population_negative # Chance of population -ve
probability_E_H = 0.8 # Chance of a +ve test given that it is true. This is the chance of a TP
probability_H = rate_population_positive # Chance of population +ve
probability_E_not_H = 9.6/100 # Chance of +ve test (X) given being part of population -ve. This is a false +ve
rate_of_actual = [rate_population_positive, rate_population_negative]
TP, FP = (rate_of_actual[0] * probability_E_H), (rate_of_actual[1] * probability_E_not_H)
FN, TN = (rate_of_actual[0] * 0.2), (rate_of_actual[1] * .904)
column_01 = [TP, FN, 0]
column_01[2] = column_01[0] + column_01[1]
column_02 = [FP, TN, 0]
column_02[2] = column_02[0] + column_02[1]
test_positive_total, test_negative_total = (column_01[0] + column_02[0]), (column_01[1] + column_02[1])
column_03 = [test_positive_total, test_negative_total, (column_01[2] + column_02[2])]

data = {field_description_column_01:column_01, field_description_column_02:column_02, field_description_column_03:column_03 }

df = pd.DataFrame(data, index=[field_description_row_01, field_description_row_02, field_description_row_03])
print (df)
probability_H_E = (TP/ test_positive_total) # Chance of actual +ve given a +ve test. (target result)
print ("Chance of TP: ", probability_H_E)
print ("Chance of TN: ", (TN/ test_negative_total))

error_acceptable = 0.000000001 / 100 # 0.000000001%
error = 1

while (error > error_acceptable):
    probability_H_E = (probability_E_H * probability_H) / ((probability_E_H * probability_H) + (probability_E_not_H * probability_not_H))
    error = math.fabs(probability_H_E - probability_H)
    probability_H = probability_H_E # updated priori probability with posteriori probability
    print(probability_H_E)


"""
Version: 2018-01-26_0250hr_27sec

Ref:
http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/
https://en.wikipedia.org/wiki/Receiver_operating_characteristic
"""