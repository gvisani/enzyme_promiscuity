
import numpy as np
import pickle
import matplotlib.pyplot as plt
import sklearn
import sklearn.preprocessing
import sklearn.metrics
import matplotlib.pyplot as plt
from numpy import interp
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data
import sys


########## DATA PREPARATION #################

def partition_data(data, Pl1, Pl2, Pl3, Pl4, Pg, Pl1_weights, Pl2_weights, Pl3_weights, Pl4_weights, Pg_weights):
    indexes = pickle_load("HMLCF_data/indexes_for_splitting")

    cutoff = int(8295*0.20)

    train_i = indexes[cutoff:]
    test_i = indexes[:cutoff]

    partition = {"training": {}, "testing": {}}

    partition["training"]["X"] = []
    temp = data[train_i]
    # for elem in temp:
    #     partition["training"]["X"].append(torch.from_numpy(elem))
    # print(data[train_i])
    partition["training"]["X"] = torch.from_numpy(np.array(data[train_i]))
    # print(partition["training"]["X"])
    # print(partition["training"]["X"].shape)
    # print(partition["training"]["X"][0])

    partition["training"]["Pg"] = []
    partition["training"]["Pg weights"] = []
    temp = Pg[train_i]
    temp2 = Pg_weights[train_i]
    # for i, elem in enumerate(temp):
    #     partition["training"]["Pg"].append(torch.from_numpy(elem))
    #     partition["training"]["Pg weights"].append(torch.from_numpy(temp2[i]))
    partition["training"]["Pg"] = torch.from_numpy(np.array(Pg[train_i]))
    partition["training"]["Pg weights"] = torch.from_numpy(np.array(Pg_weights[train_i]))


    partition["training"]["Pl1"] = []
    partition["training"]["Pl1 weights"] = []
    temp = Pl1[train_i]
    temp2 = Pl1_weights[train_i]
    # for i, elem in enumerate(temp):
    #     partition["training"]["Pl1"].append(torch.from_numpy(elem))
    #     partition["training"]["Pl1 weights"].append(torch.from_numpy(temp2[i]))
    partition["training"]["Pl1"] = torch.from_numpy(np.array(Pl1[train_i]))
    partition["training"]["Pl1 weights"] = torch.from_numpy(np.array(Pl1_weights[train_i]))

    partition["training"]["Pl2"] = []
    partition["training"]["Pl2 weights"] = []
    temp = Pl2[train_i]
    temp2 = Pl2_weights[train_i]
    # for i, elem in enumerate(temp):
    #     partition["training"]["Pl2"].append(torch.from_numpy(elem))
    #     partition["training"]["Pl2 weights"].append(torch.from_numpy(temp2[i]))
    partition["training"]["Pl2"] = torch.from_numpy(np.array(Pl2[train_i]))
    partition["training"]["Pl2 weights"] = torch.from_numpy(np.array(Pl2_weights[train_i]))
        
    partition["training"]["Pl3"] = []
    partition["training"]["Pl3 weights"] = []
    temp = Pl3[train_i]
    temp2 = Pl3_weights[train_i]
    # for i, elem in enumerate(temp):
    #     partition["training"]["Pl3"].append(torch.from_numpy(elem))
    #     partition["training"]["Pl3 weights"].append(torch.from_numpy(temp2[i]))
    partition["training"]["Pl3"] = torch.from_numpy(np.array(Pl3[train_i]))
    partition["training"]["Pl3 weights"] = torch.from_numpy(np.array(Pl3_weights[train_i]))
        
    partition["training"]["Pl4"] = []
    partition["training"]["Pl4 weights"] = []
    temp = Pl4[train_i]
    temp2 = Pl4_weights[train_i]
    # for i, elem in enumerate(temp):
    #     partition["training"]["Pl4"].append(torch.from_numpy(elem))
    #     partition["training"]["Pl4 weights"].append(torch.from_numpy(temp2[i]))
    partition["training"]["Pl4"] = torch.from_numpy(np.array(Pl4[train_i]))
    partition["training"]["Pl4 weights"] = torch.from_numpy(np.array(Pl4_weights[train_i]))

    partition["testing"]["X"] = []
    temp = data[test_i]
    # for elem in temp:
    #     partition["testing"]["X"].append(torch.from_numpy(elem))
    partition["testing"]["X"] = torch.from_numpy(np.array(data[test_i]))

    partition["testing"]["Pg"] = []
    partition["testing"]["Pg weights"] = []
    temp = Pg[test_i]
    temp2 = Pg_weights[test_i]
    # for i, elem in enumerate(temp):
    #     partition["testing"]["Pg"].append(torch.from_numpy(elem))
    #     partition["testing"]["Pg weights"].append(torch.from_numpy(temp2[i]))
    partition["testing"]["Pg"] = torch.from_numpy(np.array(Pg[test_i]))
    partition["testing"]["Pg weights"] = torch.from_numpy(np.array(Pg_weights[test_i]))

    partition["testing"]["Pl1"] = []
    partition["testing"]["Pl1 weights"] = []
    temp = Pl1[test_i]
    temp2 = Pl1_weights[test_i]
    # for i, elem in enumerate(temp):
    #     partition["testing"]["Pl1"].append(torch.from_numpy(elem))
    #     partition["testing"]["Pl1 weights"].append(torch.from_numpy(temp2[i]))
    partition["testing"]["Pl1"] = torch.from_numpy(np.array(Pl1[test_i]))
    partition["testing"]["Pl1 weights"] = torch.from_numpy(np.array(Pl1_weights[test_i]))
        
    partition["testing"]["Pl2"] = []
    partition["testing"]["Pl2 weights"] = []
    temp = Pl2[test_i]
    temp2 = Pl2_weights[test_i]
    # for i, elem in enumerate(temp):
    #     partition["testing"]["Pl2"].append(torch.from_numpy(elem))
    #     partition["testing"]["Pl2 weights"].append(torch.from_numpy(temp2[i]))
    partition["testing"]["Pl2"] = torch.from_numpy(np.array(Pl2[test_i]))
    partition["testing"]["Pl2 weights"] = torch.from_numpy(np.array(Pl2_weights[test_i]))
        
    partition["testing"]["Pl3"] = []
    partition["testing"]["Pl3 weights"] = []
    temp = Pl3[test_i]
    temp2 = Pl3_weights[test_i]
    # for i, elem in enumerate(temp):
    #     partition["testing"]["Pl3"].append(torch.from_numpy(elem))
    #     partition["testing"]["Pl3 weights"].append(torch.from_numpy(temp2[i]))
    partition["testing"]["Pl3"] = torch.from_numpy(np.array(Pl3[test_i]))
    partition["testing"]["Pl3 weights"] = torch.from_numpy(np.array(Pl3_weights[test_i]))
        
    partition["testing"]["Pl4"] = []
    partition["testing"]["Pl4 weights"] = []
    temp = Pl4[test_i]
    temp2 = Pl4_weights[test_i]
    # for i, elem in enumerate(temp):
    #     partition["testing"]["Pl4"].append(torch.from_numpy(elem))
    #     partition["testing"]["Pl4 weights"].append(torch.from_numpy(temp2[i]))
    partition["testing"]["Pl4"] = torch.from_numpy(np.array(Pl4[test_i]))
    partition["testing"]["Pl4 weights"] = torch.from_numpy(np.array(Pl4_weights[test_i]))

    # print(partition["training"]["Pl1"].shape)
    # print(partition["training"]["Pl1"])
    # print(partition["training"]["Pl1"][0])

    return partition

def get_training_data_only(data, Pl1, Pl2, Pl3, Pl4, Pg, Pl1_weights, Pl2_weights, Pl3_weights, Pl4_weights, Pg_weights):
    indexes = pickle_load("HMLCF_data/indexes_for_splitting")
    cutoff = int(8295*0.20)
    train_i = indexes[cutoff:]

    return data[train_i], Pl1[train_i], Pl2[train_i], Pl3[train_i], Pl4[train_i], Pg[train_i], Pl1_weights[train_i], Pl2_weights[train_i], Pl3_weights[train_i], Pl4_weights[train_i], Pg_weights[train_i]

def partition_data_cv(data, Pl1, Pl2, Pl3, Pl4, Pg, Pl1_weights, Pl2_weights, Pl3_weights, Pl4_weights, Pg_weights, num_folds):
    data_size = data.shape[0]
    print(data_size)

    indexes = np.linspace(0, data_size-1, data_size, dtype=int)
    np.random.shuffle(indexes)

    indexes_list = []
    for i in range(num_folds):
        indexes_list.append(indexes[int(data_size*(1.0/float(num_folds))*i) : int(data_size*(1.0/float(num_folds))*(i+1))])

    partitions = []
    for i in range(num_folds):
        train_i = np.array([])
        for j in range(num_folds):
            if i != j:
                train_i = np.append(train_i, indexes_list[j])

        train_i = train_i.astype(int)
        test_i = indexes_list[i]

        partition = {"training": {}, "testing": {}}

        partition["training"]["X"] = []
        temp = data[train_i]
        partition["training"]["X"] = torch.from_numpy(np.array(data[train_i]))

        partition["training"]["Pg"] = []
        partition["training"]["Pg weights"] = []
        temp = Pg[train_i]
        temp2 = Pg_weights[train_i]
        partition["training"]["Pg"] = torch.from_numpy(np.array(Pg[train_i]))
        partition["training"]["Pg weights"] = torch.from_numpy(np.array(Pg_weights[train_i]))


        partition["training"]["Pl1"] = []
        partition["training"]["Pl1 weights"] = []
        temp = Pl1[train_i]
        temp2 = Pl1_weights[train_i]
        partition["training"]["Pl1"] = torch.from_numpy(np.array(Pl1[train_i]))
        partition["training"]["Pl1 weights"] = torch.from_numpy(np.array(Pl1_weights[train_i]))

        partition["training"]["Pl2"] = []
        partition["training"]["Pl2 weights"] = []
        temp = Pl2[train_i]
        temp2 = Pl2_weights[train_i]
        partition["training"]["Pl2"] = torch.from_numpy(np.array(Pl2[train_i]))
        partition["training"]["Pl2 weights"] = torch.from_numpy(np.array(Pl2_weights[train_i]))
            
        partition["training"]["Pl3"] = []
        partition["training"]["Pl3 weights"] = []
        temp = Pl3[train_i]
        temp2 = Pl3_weights[train_i]
        partition["training"]["Pl3"] = torch.from_numpy(np.array(Pl3[train_i]))
        partition["training"]["Pl3 weights"] = torch.from_numpy(np.array(Pl3_weights[train_i]))
            
        partition["training"]["Pl4"] = []
        partition["training"]["Pl4 weights"] = []
        temp = Pl4[train_i]
        temp2 = Pl4_weights[train_i]
        partition["training"]["Pl4"] = torch.from_numpy(np.array(Pl4[train_i]))
        partition["training"]["Pl4 weights"] = torch.from_numpy(np.array(Pl4_weights[train_i]))

        partition["testing"]["X"] = []
        temp = data[test_i]
        partition["testing"]["X"] = torch.from_numpy(np.array(data[test_i]))

        partition["testing"]["Pg"] = []
        partition["testing"]["Pg weights"] = []
        temp = Pg[test_i]
        temp2 = Pg_weights[test_i]
        partition["testing"]["Pg"] = torch.from_numpy(np.array(Pg[test_i]))
        partition["testing"]["Pg weights"] = torch.from_numpy(np.array(Pg_weights[test_i]))

        partition["testing"]["Pl1"] = []
        partition["testing"]["Pl1 weights"] = []
        temp = Pl1[test_i]
        temp2 = Pl1_weights[test_i]
        partition["testing"]["Pl1"] = torch.from_numpy(np.array(Pl1[test_i]))
        partition["testing"]["Pl1 weights"] = torch.from_numpy(np.array(Pl1_weights[test_i]))
            
        partition["testing"]["Pl2"] = []
        partition["testing"]["Pl2 weights"] = []
        temp = Pl2[test_i]
        temp2 = Pl2_weights[test_i]
        partition["testing"]["Pl2"] = torch.from_numpy(np.array(Pl2[test_i]))
        partition["testing"]["Pl2 weights"] = torch.from_numpy(np.array(Pl2_weights[test_i]))
            
        partition["testing"]["Pl3"] = []
        partition["testing"]["Pl3 weights"] = []
        temp = Pl3[test_i]
        temp2 = Pl3_weights[test_i]
        partition["testing"]["Pl3"] = torch.from_numpy(np.array(Pl3[test_i]))
        partition["testing"]["Pl3 weights"] = torch.from_numpy(np.array(Pl3_weights[test_i]))
            
        partition["testing"]["Pl4"] = []
        partition["testing"]["Pl4 weights"] = []
        temp = Pl4[test_i]
        temp2 = Pl4_weights[test_i]
        partition["testing"]["Pl4"] = torch.from_numpy(np.array(Pl4[test_i]))
        partition["testing"]["Pl4 weights"] = torch.from_numpy(np.array(Pl4_weights[test_i]))

        partitions.append(partition)

    return partitions

class Dataset(torch.utils.data.Dataset):
    def __init__(self, data, Pg, Pl1, Pl2, Pl3, Pl4, Pg_weights, Pl1_weights, Pl2_weights, Pl3_weights, Pl4_weights):
        "Initialization. All items are in parallel."
        self.data = data
        self.Pg = Pg
        self.Pl1 = Pl1
        self.Pl2 = Pl2
        self.Pl3 = Pl3
        self.Pl4 = Pl4
        self.Pg_weights = Pg_weights
        self.Pl1_weights = Pl1_weights
        self.Pl2_weights = Pl2_weights
        self.Pl3_weights = Pl3_weights
        self.Pl4_weights = Pl4_weights

    def __len__(self):
        'Denotes the total number of samples'
        return self.data.shape[0]

    def __getitem__(self, index):
        'Generates one sample of data'
        data = self.data[index]
        Pg = self.Pg[index]
        Pl1 = self.Pl1[index]
        Pl2 = self.Pl2[index]
        Pl3 = self.Pl3[index]
        Pl4 = self.Pl4[index]
        Pg_weights = self.Pg_weights[index]
        Pl1_weights = self.Pl1_weights[index]
        Pl2_weights = self.Pl2_weights[index]
        Pl3_weights = self.Pl3_weights[index]
        Pl4_weights = self.Pl4_weights[index]
        target = (Pg, Pl1, Pl2, Pl3, Pl4)
        weights = (Pg_weights, Pl1_weights, Pl2_weights, Pl3_weights, Pl4_weights)

        return data, target, weights

########## DATA PREPARATION #################




########## MODEL CLASS AND FUNCTIONS ###############

x_size = 167

class Net(nn.Module):

    def __init__(self, C, Cl1, Cl2, Cl3, Cl4, dropout, h_size, reduced=False):
        super(Net, self).__init__()
        self.C = C     # total number of classes
        self.Cl1 = Cl1
        self.Cl2 = Cl2
        self.Cl3 = Cl3
        self.Cl4 = Cl4
        self.reduced = reduced
        self.dropout = dropout
        self.h_size = h_size
        
        self.global1 = nn.Linear(x_size, h_size)
        self.batch_norm1 = nn.BatchNorm1d(h_size)
        self.global2 = nn.Linear(h_size + x_size, h_size)
        self.batch_norm2 = nn.BatchNorm1d(h_size)
        if not self.reduced:
            self.global3 = nn.Linear(h_size + x_size, h_size)
        else:
            self.global3 = nn.Linear(x_size, h_size)
        self.batch_norm3 = nn.BatchNorm1d(h_size)
        self.global4 = nn.Linear(h_size + x_size, h_size)
        self.batch_norm4 = nn.BatchNorm1d(h_size)
        self.globalOut = nn.Linear(h_size, self.C)
        
        self.local1 = nn.Linear(h_size, h_size)
        self.batch_normL1 = nn.BatchNorm1d(h_size)
        self.localOut1 = nn.Linear(h_size, self.Cl1)
        self.local2 = nn.Linear(h_size, h_size)
        self.batch_normL2 = nn.BatchNorm1d(h_size)
        self.localOut2 = nn.Linear(h_size, self.Cl2)
        self.local3 = nn.Linear(h_size, h_size)
        self.batch_normL3 = nn.BatchNorm1d(h_size)
        self.localOut3 = nn.Linear(h_size, self.Cl3)
        self.local4 = nn.Linear(h_size, h_size)
        self.batch_normL4 = nn.BatchNorm1d(h_size)
        self.localOut4 = nn.Linear(h_size, self.Cl4)

    def forward(self, x):
        if not self.reduced:
            Ag1 = F.dropout(self.batch_norm1(F.relu(self.global1(x))), p=self.dropout)
            # Al1 = F.dropout(self.batch_normL1(F.relu(self.local1(Ag1))), p=self.dropout)
            # Pl1 = torch.sigmoid(self.localOut1(Al1))

            Ag2 = F.dropout(self.batch_norm2(F.relu(self.global2(torch.cat([Ag1, x], dim=1)))), p=self.dropout)
            # Al2 = F.dropout(self.batch_normL2(F.relu(self.local2(Ag2))), p=self.dropout)
            # Pl2 = torch.sigmoid(self.localOut2(Al2))
        
            Ag3 = F.dropout(self.batch_norm3(F.relu(self.global3(torch.cat([Ag2, x], dim=1)))), p=self.dropout)
        else:
            Ag3 = F.dropout(self.batch_norm3(F.relu(self.global3(x))), p=self.dropout)
        
        # Al3 = F.dropout(self.batch_normL3(F.relu(self.local3(Ag3))), p=self.dropout)
        # Pl3 = torch.sigmoid(self.localOut3(Al3))
        
        Ag4 = F.dropout(self.batch_norm4(F.relu(self.global4(torch.cat([Ag3, x], dim=1)))), p=self.dropout)
        # Al4 = F.dropout(self.batch_normL4(F.relu(self.local4(Ag4))), p=self.dropout)
        # Pl4 = torch.sigmoid(self.localOut4(Al4))
        
        Pg = torch.sigmoid(self.globalOut(Ag4))
        
        if not self.reduced:
            return Pg# , Pl1, Pl2, Pl3, Pl4    # return all outputs to compute loss
        else:
            return Pg, Pl3, Pl4

def custom_loss(Pl4, target, weights):
    # This way all operation are made on Variables. Will this work?
    
    return F.binary_cross_entropy(Pl4, target[4].float(), weight=weights[4].float())# + F.binary_cross_entropy(Pl1, target[1].float(), weight=weights[1].float()) + F.binary_cross_entropy(Pl2, target[2].float(), weight=weights[2].float()) + F.binary_cross_entropy(Pl3, target[3].float(), weight=weights[3].float()) + F.binary_cross_entropy(Pl4, target[4].float(), weight=weights[4].float())


def train(model, device, train_loader, optimizer, epoch):
    model.train()
    loss_trace = []
    for batch_idx, (data, target, weights) in enumerate(train_loader):
        # data, target = data.to(device), [target[0].to(device), target[1].to(device), target[2].to(device), target[3].to(device), target[4].to(device)]    # fix this for all targets when using cuda
        optimizer.zero_grad()
        Pl4 = model(data.float())
        loss = custom_loss(Pl4, target, weights)
        loss.backward()
        optimizer.step()
        loss_trace.append(loss.item())
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))
    return loss_trace

def test(model, device, test_loader, beta):
    model.eval()
    predictions = []
    targets = []
    weights = []
    loss_trace = []
    with torch.no_grad():
        for data, target, weight in test_loader:
            # data, target = data.to(device), [target[0].to(device), target[1].to(device), target[2].to(device), target[3].to(device), target[4].to(device)]
            Pl4 = model(data.float())
            loss = custom_loss(Pl4, target, weight)
            loss_trace.append(loss.item())
            predictions.append(Pl4[0])
            targets.append(target[4][0].float())
            weights.append(weight[4][0].float())
        
    return predictions, targets, weights, loss_trace

########## MODEL CLASS AND FUNCTIONS ###############


########## TESTING UTILITIES #######################

def compute_results(predictions, targets, weights):
    results = {}
    target_results = {}
    target_weights = {}
    for i in range(1007):
        results[i] = []
        target_results[i] = []
        target_weights[i] = []

    for j, pred in enumerate(predictions):
        for i in range(1007):
            results[i].append(float(pred[i]))
            target_results[i].append(float(targets[j][i]))
            target_weights[i].append(float(weights[j][i]))

    PRs = {}
    for i in results:
        y_true = np.array(target_results[i])
        if y_true[y_true == 1.0].shape[0] == 0:
            continue
        PRs[i] = {}
        prec, rec, thr = sklearn.metrics.precision_recall_curve(target_results[i], results[i])
        PRs[i]["prec"] = prec
        PRs[i]["rec"] = rec
        PRs[i]["ap"] = sklearn.metrics.average_precision_score(target_results[i], results[i])

    rocs = {}
    for i in results:
        y_true = np.array(target_results[i])
        if y_true[y_true == 1.0].shape[0] == 0:
            continue
        rocs[i] = {}
        fpr, tpr, thr = sklearn.metrics.roc_curve(target_results[i], results[i])
        rocs[i]["fpr"] = fpr
        rocs[i]["tpr"] = tpr

    R_precs = {}
    for i in results:
        y_hat = np.array(results[i])
        y_true = np.array(target_results[i])
        if y_true[y_true == 1.0].shape[0] == 0:
            continue
        R = y_true[y_true == 1.0].shape[0]
        sorted_indices = np.argsort(y_hat)

        sorted_y_true = y_true[sorted_indices]
        top_R = sorted_y_true[-R:]
        R_precs[i] = float(top_R[top_R == 1.0].shape[0])/float(R)
    
    return results, target_results, target_weights, rocs, PRs, R_precs

def plot_roc_similarity(results, title):
    plt.figure(figsize=(9, 6))
    plt.title(title)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
             label='Chance', alpha=.8)
    mean_fpr = np.linspace(0, 1, 100)
    tprs = []
    aucs = []
    for enzyme in results:
#         plt.plot(results[enzyme]["fpr"], results[enzyme]["tpr"])
        if results[enzyme]["fpr"].shape[0] > 0:
            tprs.append(interp(mean_fpr, results[enzyme]["fpr"], results[enzyme]["tpr"]))
            roc_auc = sklearn.metrics.auc(results[enzyme]["fpr"], results[enzyme]["tpr"])
            aucs.append(roc_auc)

    mean_tpr = np.nanmean(tprs, axis=0)
    
    print(sklearn.metrics.auc(mean_fpr, mean_tpr))

    mean_auc = np.nanmean(aucs) #sklearn.metrics.auc(mean_fpr, mean_tpr)
    std_auc = np.nanstd(aucs)
    plt.plot(mean_fpr, mean_tpr,
         label=r'Mean ROC (AUC = %0.3f $\pm$ %0.3f)' % (mean_auc, std_auc),
         lw=2, alpha=.8)

    # standard deviation
    std_tpr = np.nanstd(tprs, axis=0)
    tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
    tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
    plt.fill_between(mean_fpr, tprs_lower, tprs_upper, alpha=.2,
                     label=r'$\pm$ 1 std. dev.')
    plt.legend()
    plt.show()
    
def plot_pr_curves(PRs, title):
    plt.figure(figsize=(9, 6))
    plt.title(title)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.xlim((-0.1, 1.1))
    plt.ylim((-0.1, 1.1))
    mean_rec = np.linspace(0, 1, 200)
    precs = []
    aucs = []
    aps = []
    count = 0
    for enzyme in PRs:
        plt.plot(PRs[enzyme]["rec"], PRs[enzyme]["prec"])
        if PRs[enzyme]["rec"].shape[0] > 0:
            precs.append(interp(mean_rec, PRs[enzyme]["rec"], PRs[enzyme]["prec"]))
            pr_auc = sklearn.metrics.auc(PRs[enzyme]["rec"], PRs[enzyme]["prec"])
            aucs.append(pr_auc)
            aps.append(PRs[enzyme]["ap"])
            count += 1
    
    print(count)
        
#     print(np.nanmean(aucs))
    
#     print(precs)
    
    mean_prec = np.nanmean(precs, axis=0)
    
#     print(mean_prec)

    print(sklearn.metrics.auc(mean_rec, mean_prec))
    mean_auc = np.nanmean(aucs) #sklearn.metrics.auc(mean_rec, mean_prec)
    std_auc = np.nanstd(aucs)
    mean_ap = np.nanmean(aps)
    std_ap = np.nanstd(aps)
#     print(aps)
    plt.plot(mean_rec, mean_prec,
         label=r'Mean PR-Curve (AUC = %0.3f $\pm$ %0.3f) (AP = %0.3f $\pm$ %0.3f)' % (mean_auc, std_auc, mean_ap, std_ap),
         lw=2, alpha=.8)

    # standard deviation
    std_prec = np.nanstd(precs, axis=0)
    precs_upper = np.minimum(mean_prec + std_prec, 1)
    precs_lower = np.maximum(mean_prec - std_prec, 0)
    plt.fill_between(mean_rec, precs_lower, precs_upper, alpha=.2,
                         label=r'$\pm$ 1 std. dev.')

    plt.legend()
    plt.show()
    
def get_mean_auroc(results):
    mean_fpr = np.linspace(0, 1, 100)
    tprs = []
    aucs = []
    for enzyme in results:
        tprs.append(interp(mean_fpr, results[enzyme]["fpr"], results[enzyme]["tpr"]))
        roc_auc = sklearn.metrics.auc(results[enzyme]["fpr"], results[enzyme]["tpr"])
        aucs.append(roc_auc)

    mean_tpr = np.nanmean(tprs, axis=0)
    mean_auc = sklearn.metrics.auc(mean_fpr, mean_tpr)
    std_auc = np.nanstd(aucs)
    return mean_auc, std_auc

def get_mean_ap(PRs):
    aps = []
    for enzyme in PRs:
        aps.append(PRs[enzyme]["ap"])
    
    mean_ap = np.nanmean(aps)
    std_ap = np.nanstd(aps)
    return mean_ap, std_ap

def get_mean_R_prec(table, thresh=0):
    R_precs = []
    for enzyme in table:
        # if table[enzyme]["num_pos_total"] > thresh:
        R_precs.append(table[enzyme])

    return np.mean(R_precs), np.std(R_precs)

def polyfit(x, y, degree):
    results = {"Coefficients": [], "R-squared": 0}

    coeffs = np.polyfit(x, y, degree)

    results["Coefficients"] = coeffs.tolist()

    # R-squared calculation
    p = np.poly1d(coeffs)
    y_fit = p(x)                        
    y_mean = np.sum(y)/len(y)
    ssreg = np.sum((y_fit-y_mean)**2)
    sstot = np.sum((y - y_mean)**2)
    
    results["R-squared"] = ssreg / sstot

    return results

########## TESTING UTILITIES #######################

########## GENERAL UTILITIES #######################

def pickle_load(filepath):
    f = open(filepath, "rb")
    data = pickle.load(f)
    f.close()
    return data

def pickle_dump(data, filepath):
    f = open(filepath, "wb")
    pickle.dump(data, f)
    f.close()

def get_data(filepath):
    data = dict()
    handle = open(filepath, 'r')
    for line in handle:
        line = line.split('\t')
        ecnumber = line[0]
        smiles = line[1].strip('\n').split('$')
        data[ecnumber] = smiles
    handle.close()
    return data

def get_dropout_list(low, high, num):
    dropout_list = []
    for i in range(num):
        dropout_list.append(np.random.uniform(low, high))
    return dropout_list

########## GENERAL UTILITIES #######################


if __name__ == '__main__':

    print("Getting data...")
    data = pickle_load("HMLCF_data/data.pkl")
    Pl1  = pickle_load("HMLCF_data/Pl1.pkl")
    Pl2  = pickle_load("HMLCF_data/Pl2.pkl")
    Pl3  = pickle_load("HMLCF_data/Pl3.pkl")
    Pl4  = pickle_load("HMLCF_data/Pl4.pkl")
    Pg   = pickle_load("HMLCF_data/Pg.pkl")
    Pl1_weights = pickle_load("HMLCF_data/Pl1_sim_bal_weights_inh.pkl")
    Pl2_weights = pickle_load("HMLCF_data/Pl2_sim_bal_weights_inh.pkl")
    Pl3_weights = pickle_load("HMLCF_data/Pl3_sim_bal_weights_inh.pkl")
    Pl4_weights = pickle_load("HMLCF_data/Pl4_sim_bal_weights_inh.pkl")
    Pg_weights  = pickle_load("HMLCF_data/Pg_sim_bal_weights_inh.pkl")
    print("Successfully gotten data.")

    # partition datainto training and testing
    print("Partitioning data...")
    partition = partition_data(data, Pl1, Pl2, Pl3, Pl4, Pg, Pl1_weights, Pl2_weights, Pl3_weights, Pl4_weights, Pg_weights)
    print("Successfully partitioned data.")

    # create dataset and data loaders
    print("Creating datasets...")
    training_set_all = Dataset(partition["training"]["X"], partition["training"]["Pg"], partition["training"]["Pl1"], partition["training"]["Pl2"], partition["training"]["Pl3"], partition["training"]["Pl4"], partition["training"]["Pg weights"], partition["training"]["Pl1 weights"], partition["training"]["Pl2 weights"], partition["training"]["Pl3 weights"], partition["training"]["Pl4 weights"])
    testing_set_all = Dataset(partition["testing"]["X"], partition["testing"]["Pg"], partition["testing"]["Pl1"], partition["testing"]["Pl2"], partition["testing"]["Pl3"], partition["testing"]["Pl4"], partition["testing"]["Pg weights"], partition["testing"]["Pl1 weights"], partition["testing"]["Pl2 weights"], partition["testing"]["Pl3 weights"], partition["testing"]["Pl4 weights"])

    train_loader_all = torch.utils.data.DataLoader(training_set_all, batch_size=12, shuffle=True)
    test_loader_all = torch.utils.data.DataLoader(testing_set_all, batch_size=1)
    print("Successfully created datasets.")

    # train model
    print("Training...")

    # data_t, Pl1_t, Pl2_t, Pl3_t, Pl4_t, Pg_t, Pl1_weights_t, Pl2_weights_t, Pl3_weights_t, Pl4_weights_t, Pg_weights_t = get_training_data_only(data, Pl1, Pl2, Pl3, Pl4, Pg, Pl1_weights, Pl2_weights, Pl3_weights, Pl4_weights, Pg_weights)

    # num_to_search = 12
    # num_folds = 3
    # partitions = partition_data_cv(data_t, Pl1_t, Pl2_t, Pl3_t, Pl4_t, Pg_t, Pl1_weights_t, Pl2_weights_t, Pl3_weights_t, Pl4_weights_t, Pg_weights_t, num_folds)

    # dropout_list = []
    # layer_list = []
    # results_aps = []
    # for n in range(num_to_search):
    #     dropout = np.random.uniform(0.01, 0.6)
    #     h_size = np.random.randint(128, 384)
    #     dropout_list.append(dropout)
    #     layer_list.append(h_size)
    #     folds_aps = []
    #     for fold in range(num_folds):
    #         part = partitions[fold]
    #         training_set = Dataset(part["training"]["X"], part["training"]["Pg"], part["training"]["Pl1"], part["training"]["Pl2"], part["training"]["Pl3"], part["training"]["Pl4"], part["training"]["Pg weights"], part["training"]["Pl1 weights"], part["training"]["Pl2 weights"], part["training"]["Pl3 weights"], part["training"]["Pl4 weights"])
    #         testing_set = Dataset(part["testing"]["X"], part["testing"]["Pg"], part["testing"]["Pl1"], part["testing"]["Pl2"], part["testing"]["Pl3"], part["testing"]["Pl4"], part["testing"]["Pg weights"], part["testing"]["Pl1 weights"], part["testing"]["Pl2 weights"], part["testing"]["Pl3 weights"], part["testing"]["Pl4 weights"])

    #         train_loader = torch.utils.data.DataLoader(training_set, batch_size=12, shuffle=True)
    #         test_loader = torch.utils.data.DataLoader(testing_set, batch_size=1)

    #         model = Net(1007, 0, 0, 0, 0, dropout=dropout, h_size=h_size)
    #         device = torch.device("cpu")
    #         optimizer = torch.optim.Adam(model.parameters(), lr=0.0002)

    #         num_epochs = 100
    #         for epoch in range(num_epochs):
    #             train_loader = torch.utils.data.DataLoader(training_set, batch_size=12, shuffle=True)
    #             loss_trace = train(model, device, train_loader, optimizer, epoch)

    #             predictions, targets, weights, loss_trace = test(model, device, test_loader, 0.5)
    #         results, target_results, target_weights, rocs, PRs, R_precs = compute_results(predictions, targets, weights)

    #         folds_aps.append(get_mean_ap(PRs))

    #     results_aps.append(np.mean(folds_aps))

    # best_ap_i = np.argmax(results_aps)
    # best_dropout = dropout_list[best_ap_i]
    # best_layer = layer_list[best_ap_i]
    # best_ap = results_aps[best_ap_i]

    best_dropout = 0.01
    best_layer = 175

    model = Net(1007, 0, 0, 0, 0, dropout=best_dropout, h_size=best_layer)
    device = torch.device("cpu")
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0002)

    traces_train = []
    traces_test = []
    rocs_list = []
    PRs_list = []
    R_precs_list = []
    results_list = []
    targets_list = []
    num_epochs = 150
    for epoch in range(num_epochs):
        train_loader_all = torch.utils.data.DataLoader(training_set_all, batch_size=12, shuffle=True)
        loss_trace = train(model, device, train_loader_all, optimizer, epoch)
        traces_train.append(loss_trace)

        predictions, targets, weights, loss_trace = test(model, device, test_loader_all, 0.5)
        traces_test.append(loss_trace)
        results, target_results, target_weights, rocs, PRs, R_precs = compute_results(predictions, targets, weights)
        rocs_list.append(rocs)
        PRs_list.append(PRs)
        R_precs_list.append(R_precs)
        results_list.append(results)
        targets_list.append(target_results)

    torch.save(model, "models/HMLCF_BEST_balancing_weights_biased_flat_inh_epoch_%d.pt" % (epoch))

    # # plot loss and save
    # t_train = []
    # for loss_trace in traces_train:
    #     t_train += loss_trace

    # t_test = []
    # for loss_trace in traces_test:
    #     t_test += loss_trace
        
    # plt.figure(figsize = (17, 6))
    # x = np.linspace(0, len(t_train)-1, len(t_train))
    # plt.plot(x, t_train, label="Train")
    # plt.xlabel("Batch Iteration")
    # plt.ylabel("Loss")
    # plt.legend()
    # plt.savefig("HMLCF_results/loss_train_balancing_weights_biased_flat_inh_best_drop%.2f_layer%d.pdf" % (best_dropout, best_layer))

    # plt.figure(figsize = (17, 6))
    # x = np.linspace(0, len(t_test)-1, len(t_test))
    # plt.plot(x, t_test, label="Test")
    # plt.xlabel("Batch Iteration")
    # plt.ylabel("Loss")
    # plt.legend()
    # plt.savefig("HMLCF_results/loss_test_balancing_weights_biased_flat_inh_best_drop%.2f_layer%d.pdf" % (best_dropout, best_layer))

    # # plot ap and auroc
    # aurocs = []
    # std_aurocs = []
    # for rocs in rocs_list:
    #     mean, std = get_mean_auroc(rocs)
    #     aurocs.append(mean)
    #     std_aurocs.append(std)

    # aps = []
    # std_aps = []
    # for PRs in PRs_list:
    #     mean, std = get_mean_ap(PRs)
    #     aps.append(mean)
    #     std_aps.append(std)

    # R_precs = []
    # std_R_precs = []
    # for R_prec in R_precs_list:
    #     mean, std = get_mean_R_prec(R_prec)
    #     R_precs.append(mean)
    #     std_R_precs.append(std)

    # plt.figure(figsize = (10, 7))
    # epochs = np.linspace(1, num_epochs + 1, num_epochs)
    # plt.plot(epochs, aurocs, label="AUROCS, final: %.3f +/- %.3f" % (aurocs[-1], std_aurocs[-1]))
    # plt.plot(epochs, aps, label="APS, final: %.3f +/- %.3f, at validation: %.3f" % (aps[-1], std_aps[-1], best_ap))
    # plt.plot(epochs, R_precs, label="R-PRECS, final: %.3f +/- %.3f" % (R_precs[-1], std_R_precs[-1]))
    # plt.fill_between(epochs, np.array(aps) + np.array(std_aps), np.array(aps) - np.array(std_aps), alpha=.2, color="orange")#, label="mean std: %.3f" % (np.mean(std_aps)))
    # plt.fill_between(epochs, np.array(aurocs) + np.array(std_aurocs), np.array(aurocs) - np.array(std_aurocs), alpha=.2, color="blue")#, label="mean std: %.3f" % (np.mean(std_aurocs)))
    # plt.fill_between(epochs, np.array(R_precs) + np.array(std_R_precs), np.array(R_precs) - np.array(std_R_precs), alpha=.2, color="green")#, label="mean std: %.3f" % (np.mean(std_R_precs)))
    # plt.title("Results at Testing across Epochs, Similarity-Weighted, Dropout %.2f." % (best_dropout))
    # plt.xlabel("Epochs")
    # plt.grid()
    # plt.legend()
    # plt.savefig("HMLCF_results/ap_and_auroc_train_balancing_weights_biased_flat_inh_best_drop%.2f_layer%d.pdf" % (best_dropout, best_layer))

    # pickle_dump(rocs_list, "HMLCF_results/rocs_list_balancing_weights_biased_flat_inh_best_drop%.2f._layer%dpkl" % (best_dropout, best_layer))
    # pickle_dump(PRs_list, "HMLCF_results/PRs_list_balancing_weights_biased_flat_inh_best_drop%.2f_layer%d.pkl" % (best_dropout, best_layer))
    # pickle_dump(R_precs_list, "HMLCF_results/R_precs_list_balancing_weights_biased_flat_inh_best_drop%.2f_layer%d.pkl" % (best_dropout, best_layer))
    # pickle_dump(results_list, "HMLCF_results/results_list_balancing_weights_biased_flat_inh_best_drop%.2f_layer%d.pkl" % (best_dropout, best_layer))
    # pickle_dump(targets_list, "HMLCF_results/targets_list_balancing_weights_biased_flat_inh_best_drop%.2f_layer%d.pkl" % (best_dropout, best_layer))