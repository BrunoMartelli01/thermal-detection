# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import os
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.chdir("anomalib")
    a = np.load("./datasets/harbor_anomaly_dataset/test_annotations_anomalies/20200820/clip_23_1043.npy")
    print("clip: ",a)

    for i in range(len(a)):
        print(i, a[i])
    print(os.getcwd())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
