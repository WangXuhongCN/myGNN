import numpy as np

def one_class_processing(args,data,normal_class:int):
    labels,normal_idx,abnormal_idx=one_class_labeling(data.labels,normal_class)
    return one_class_masking(labels,normal_idx,abnormal_idx)


def one_class_labeling(labels,normal_class:int):
    normal_idx=np.where(labels==normal_class)[0]
    abnormal_idx=np.where(labels!=normal_class)[0]

    labels[normal_idx]=0
    labels[abnormal_idx]=1
    np.random.shuffle(normal_idx)
    np.random.shuffle(abnormal_idx)
    return labels,normal_idx,abnormal_idx

#训练集60%正常、验证集15%正常、测试集25%正常，验证集测试集中的正常异常样本1:1
def one_class_masking(labels,normal_idx,abnormal_idx):
    train_mask=np.zeros(labels.shape)
    val_mask=np.zeros(labels.shape)
    test_mask=np.zeros(labels.shape)

    train_mask[normal_idx[:int(0.6*normal_idx.shape[0])]]=1

    val_mask[normal_idx[int(0.6*normal_idx.shape[0]):int(0.75*normal_idx.shape[0])]]=1
    val_mask[abnormal_idx[:int(0.15*normal_idx.shape[0])]]=1

    test_mask[normal_idx[int(0.75*normal_idx.shape[0]):]]=1
    test_mask[abnormal_idx[-int(0.25*normal_idx.shape[0]):]]=1

    return labels,train_mask,val_mask,test_mask  

'''
全部节点都用于分类
def one_class_masking(labels,normal_idx,abnormal_idx):
    train_mask=np.zeros(labels.shape)
    val_mask=np.zeros(labels.shape)
    test_mask=np.zeros(labels.shape)

    train_mask[normal_idx[:int(0.7*normal_idx.shape[0])]]=1

    val_mask[normal_idx[int(0.7*normal_idx.shape[0]):int(0.8*normal_idx.shape[0])]]=1
    val_mask[abnormal_idx[:int(0.3*abnormal_idx.shape[0])]]=1

    test_mask[normal_idx[int(0.8*normal_idx.shape[0]):]]=1
    test_mask[abnormal_idx[int(0.3*abnormal_idx.shape[0]):]]=1

    return labels,train_mask,val_mask,test_mask  
'''