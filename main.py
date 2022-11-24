# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

from rdflib import Graph


def calculate(true_path, predict_path):
    true_set = set()
    predict_set = set()
    with open(true_path, 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            true_set.add(line)

    with open(predict_path, 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            predict_set.add(line)

    overlap = len(true_set & predict_set)

    precision = overlap / len(predict_set)
    recall = overlap / len(true_set)
    f1 = 0.0
    if precision != 0.0 and recall != 0.0:
        f1 = precision * recall * 2.0 / (precision + recall)
    else:
        f1 = 0.0

    return precision, recall, f1


def calculate_dbpedia_top5(index, true_path, pred_path):
    allPrecision = 0.0
    allRecall = 0.0
    allF1 = 0.0
    true_paths = []
    for i in range(6):
        true_paths.append(os.path.join(true_path, "{}_gold_top5_{}.nt".format(index, i)))

    for path in true_paths:
        top5_path = os.path.join(pred_path, "{}_top5.nt".format(index))
        precision, recall, f1 = calculate(path, top5_path)
        allPrecision += precision
        allRecall += recall
        allF1 += f1

    return allPrecision/6.0, allRecall/6.0, allF1/6.0

def dbpedia_top5(ground_path, algo_path):
    allPrecision = 0.0
    allRecall = 0.0
    allF1 = 0.0
    index = [i for i in range(1, 101)]
    index += [i for i in range(141, 166)]

    for i in index:
        true_path = os.path.join(ground_path, "dbpedia_data", str(i))
        pred_path = os.path.join(algo_path, "dbpedia", str(i))
        precision, recall, f1 = calculate_dbpedia_top5(i, true_path, pred_path)
        allPrecision += precision
        allRecall += recall
        allF1 += f1

    return allPrecision/125.0, allRecall/125.0, allF1/125.0

def calculate_dbpedia_top10(index, true_path, pred_path):
    allPrecision = 0.0
    allRecall = 0.0
    allF1 = 0.0
    true_paths = []
    for i in range(6):
        true_paths.append(os.path.join(true_path, "{}_gold_top10_{}.nt".format(index, i)))

    for path in true_paths:
        top10_path = os.path.join(pred_path, "{}_top10.nt".format(index))
        precision, recall, f1 = calculate(path, top10_path)
        allPrecision += precision
        allRecall += recall
        allF1 += f1

    return allPrecision/6.0, allRecall/6.0, allF1/6.0

def dbpedia_top10(ground_path, algo_path):
    allPrecision = 0.0
    allRecall = 0.0
    allF1 = 0.0
    index = [i for i in range(1, 101)]
    index += [i for i in range(141, 166)]

    for i in index:
        true_path = os.path.join(ground_path, "dbpedia_data", str(i))
        pred_path = os.path.join(algo_path, "dbpedia", str(i))
        precision, recall, f1 = calculate_dbpedia_top10(i, true_path, pred_path)
        allPrecision += precision
        allRecall += recall
        allF1 += f1

    return allPrecision/125.0, allRecall/125.0, allF1/125.0

def calculate_lmdb_top5(index, true_path, pred_path):
    allPrecision = 0.0
    allRecall = 0.0
    allF1 = 0.0
    true_paths = []
    for i in range(6):
        true_paths.append(os.path.join(true_path, "{}_gold_top5_{}.nt".format(index, i)))

    for path in true_paths:
        top5_path = os.path.join(pred_path, "{}_top5.nt".format(index))
        precision, recall, f1 = calculate(path, top5_path)
        allPrecision += precision
        allRecall += recall
        allF1 += f1

    return allPrecision/6.0, allRecall/6.0, allF1/6.0

def lmdb_top5(ground_path, algo_path):
    allPrecision = 0.0
    allRecall = 0.0
    allF1 = 0.0
    index = [i for i in range(101, 141)]
    index += [i for i in range(166, 176)]
    for i in index:
        true_path = os.path.join(ground_path, "lmdb_data", str(i))
        pred_path = os.path.join(algo_path, "lmdb", str(i))
        precision, recall, f1 = calculate_lmdb_top5(i, true_path, pred_path)
        allPrecision += precision
        allRecall += recall
        allF1 += f1

    return allPrecision / 50.0, allRecall / 50.0, allF1 / 50.0

def calculate_lmdb_top10(index, true_path, pred_path):
    allPrecision = 0.0
    allRecall = 0.0
    allF1 = 0.0
    true_paths = []
    for i in range(6):
        true_paths.append(os.path.join(true_path, "{}_gold_top10_{}.nt".format(index, i)))

    for path in true_paths:
        top10_path = os.path.join(pred_path, "{}_top10.nt".format(index))
        precision, recall, f1 = calculate(path, top10_path)
        allPrecision += precision
        allRecall += recall
        allF1 += f1

    return allPrecision/6.0, allRecall/6.0, allF1/6.0

def lmdb_top10(ground_path, algo_path):
    allPrecision = 0.0
    allRecall = 0.0
    allF1 = 0.0
    index = [i for i in range(101, 141)]
    index += [i for i in range(166, 176)]
    for i in index:
        true_path = os.path.join(ground_path, "lmdb_data", str(i))
        pred_path = os.path.join(algo_path, "lmdb", str(i))
        precision, recall, f1 = calculate_lmdb_top10(i, true_path, pred_path)
        allPrecision += precision
        allRecall += recall
        allF1 += f1

    return allPrecision / 50.0, allRecall / 50.0, allF1 / 50.0


def generate_f1(ground_path, algo_path):
    dbpedia_top5_precision, dbpedia_top5_recall, dbpedia_top5_f1 = dbpedia_top5(ground_path, algo_path)
    dbpedia_top10_precision, dbpedia_top10_recall, dbpedia_top10_f1 = dbpedia_top10(ground_path, algo_path)
    lmdb_top5_precision, lmdb_top5_recall, lmdb_top5_f1 = lmdb_top5(ground_path, algo_path)
    lmdb_top10_precision, lmdb_top10_recall, lmdb_top10_f1 = lmdb_top10(ground_path, algo_path)

    return dbpedia_top5_f1, dbpedia_top10_f1, lmdb_top5_f1, lmdb_top10_f1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ground_path = "/Users/huangcheng/Documents/EABMEval/ESBM_benchmark_v1.2"
    pred_path = "/Users/huangcheng/Documents/EABMEval/remove_top2_frequent_esbm/removetop2raltion_k_6_m_5"
    dbpedia_top5_f1, dbpedia_top10_f1, lmdb_top5_f1, lmdb_top10_f1 = generate_f1(ground_path, pred_path)
    print("dbpedia_top5_f1 = ", dbpedia_top5_f1)
    print("dbpedia_top10_f1 = ", dbpedia_top10_f1)
    print("lmdb_top5_f1 = ", lmdb_top5_f1)
    print("lmdb_top10_f1 = ", lmdb_top10_f1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
