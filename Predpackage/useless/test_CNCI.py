import numpy as np
import pandas as pd
import time
import random
import os
from Bio import SeqIO
from sklearn.metrics import roc_auc_score, accuracy_score, recall_score, f1_score, precision_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

# data preparation
# fasta format
lncRNA = list(SeqIO.parse(
    "data/Mouse_Main_lncRNAs.fa", "fasta"))
pcts = list(SeqIO.parse(
    "data/Mouse_Main_pcts.fa", "fasta"))
# lncRNA = lncRNA[:1000]
# pcts = pcts[:1000]
#pcts = pcts[:len(lncRNA)]
# gtf format
#lncRNA = pd.read_csv("gencode.v29.long_noncoding_RNAs.gtf",sep="\t")
#pcts = pd.read_csv("gencode.v29.pcts_RNAs.gtf",sep="\t")
#lncRNA = lncRNA[:len(pcts)]

# os.system("rm -rf ./cv_test/result/*")

print(len(lncRNA))
print(len(pcts))
global_y = []
for num in range(len(lncRNA)):
    global_y.append(1)
for num in range(len(pcts)):
    global_y.append(0)
global_y = np.asarray(global_y)
all_X = np.concatenate((lncRNA, pcts), axis=0)
index = [i for i in range(len(all_X))]
random.shuffle(index)
all_X = all_X[index]
global_y = global_y[index]


def CNCI_model_test(lncRNA_file, output_file):
    print("CNCI is Running ... ")
    print("python3 Models/CNCI/CNCI.py -f " +
          lncRNA_file+" -o "+output_file+" -m ve -p 4")
    os.system("python3 Models/CNCI/CNCI.py -f " +
              lncRNA_file+" -o "+output_file+" -m ve -p 4")
    output_file = output_file + "/CNCI.index"
    result = pd.read_csv(output_file, sep="\t")
    proba = list(result['index'].apply(lambda x: 0 if x == "coding" else 1))
    label = list(result['index'].apply(lambda x: 0 if x == "coding" else 1))
    return proba, label


def model_performance(model_proba, model_predict, test_y):
    test_y = test_y[:int(len(model_proba))]
    print(len(test_y))
    print(len(model_proba))
    AUC = roc_auc_score(test_y, model_proba)
    Accuracy = accuracy_score(test_y, model_predict)
    Sensitivity = recall_score(test_y, model_predict)
    Specificity = (Accuracy*len(test_y)-Sensitivity *
                   sum(test_y))/(len(test_y)-sum(test_y))
    F1 = f1_score(test_y, model_predict)
    Precision = precision_score(test_y, model_predict)
    return AUC, Accuracy, Sensitivity, Specificity, F1, Precision


def test_preparation(cv_round, model_name, train_data_lncRNA, train_data_pcts, test_data):
    path1 = "data/" + \
        model_name+"_"+str(cv_round)+".fa"
    count1 = SeqIO.write(test_data, path1, "fasta")
    path2 = "data/" + \
        model_name+"_training_lncRNA"+str(cv_round)+".fa"
    count2 = SeqIO.write(train_data_lncRNA, path2, "fasta")
    path3 = "data/" + \
        model_name+"_training_pcts"+str(cv_round)+".fa"
    count3 = SeqIO.write(train_data_pcts, path3, "fasta")
    return path1, count1, path2, path3


def crossValidation(all_X, global_y, folds):
    AUCs = []
    Accuracys = []
    Sensitivitys = []
    Specificitys = []
    F1s = []
    Precisions = []
    cv_round = 1
    for global_train_index, global_test_index in folds.split(all_X, global_y):
        print('..........................................................................')
        print('global cross validation, round %d, beginning' % cv_round)
        start = time.perf_counter()
        train_X = all_X[global_train_index]
        train_y = global_y[global_train_index]
        test_X = all_X[global_test_index]
        test_y = global_y[global_test_index]
        #path = "/home/ls1/test/mid/CPC2_test_"+str(cv_round)+".fa"
        #count = SeqIO.write(test_X,path,"fasta")
        train_X_lncRNA = train_X[train_y == 1]
        train_X_pcts = train_X[train_y == 0]

        path, count, train_X_lncRNA_path, train_X_pcts_path = test_preparation(
            cv_round, "CNCI_test", train_X_lncRNA, train_X_pcts, test_X)

        print("write back %i seqences for test" % count)

        # test
        proba, label = CNCI_model_test(
            path, "data/CNCI_result")

        AUC, Accuracy, Sensitivity, Specificity, F1, Precision = model_performance(
            proba, label, test_y)

        AUCs.append(AUC)
        Accuracys.append(Accuracy)
        Sensitivitys.append(Sensitivity)
        Specificitys.append(Specificity)
        F1s.append(F1)
        Precisions.append(Precision)
        end = time.perf_counter()

        print('AUC %.4f, Accuracy %.4f,Sensitivity %.4f, Specificity %.4f,F1 %.4f, Precision %.4f' % (
            AUC, Accuracy, Sensitivity, Specificity, F1, Precision))
        print('round %.4f, running time: %.4f hour' %
              (cv_round, (end-start)/3600))
        print(
            '..........................................................................\n')
        cv_round += 1
    return np.mean(AUCs), np.mean(Accuracys), np.mean(Sensitivitys), np.mean(Specificitys), np.mean(F1s), np.mean(Precisions)


folds = StratifiedKFold(n_splits=10, shuffle=True,
                        random_state=np.random.RandomState(1))
AUC, Accuracy, Sensitivity, Specificity, F1, Precision = crossValidation(
    all_X, global_y, folds)
print("AUC:", AUC)
print("Accuracy:", Accuracy)
print("Sensitivity:", Sensitivity)
print("Specificity:", Specificity)
print("F1:", F1)
print("Precision:", Precision)
