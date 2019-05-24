

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
from scipy.stats import skew, skewtest


df = pd.read_csv('../../Documents/ece657a/data/DataA.csv')
df = df.astype(float)
df = df.drop(['Unnamed: 0'], axis=1)  # remove id row
# print(df)

null_col_thresh = df.shape[0] * 0.999

print("Before cleaning -----------------------------")
print("Dataset shape: " + str(df.shape))
print("Total nan values: " + str(df.isna().sum().sum()))
null_rows = df.isna().all(axis=1).sum()
print("Nan rows (all): " + str(null_rows))
null_rows = df.isna().any(axis=1).sum()
print("Nan rows (any): " + str(null_rows))
nulls_per_col = df.isna().sum()
null_cols = []
for i in range(nulls_per_col.shape[0]):
    if nulls_per_col[i] >= null_col_thresh:
        null_cols.append(i)
print("Nan cols (>=" + str(null_col_thresh) + " are nan): " + str(null_cols))
print()


print("After cleaning -----------------------------")
# remove any row that has less than 2 columns that are not nan
df = df.dropna(thresh=2)
df = df.drop(df.columns[null_cols], axis=1)
# fill missing with mean of columns
df = df.fillna(df.mean())
print("Dataset shape: " + str(df.shape))
print("Total nan values: " + str(df.isna().sum().sum()))
null_rows = df.isna().all(axis=1).sum()
print("Nan rows (all): " + str(null_rows))
null_rows = df.isna().any(axis=1).sum()
print("Nan rows (any): " + str(null_rows))
nulls_per_col = df.isna().sum()
null_cols = []
for i in range(nulls_per_col.shape[0]):
    if nulls_per_col[i] >= null_col_thresh:
        null_cols.append(i)
print("Nan cols (>=" + str(null_col_thresh) + " are nan): " + str(null_cols))
print()

minmax_scaler = MinMaxScaler()
minmax = minmax_scaler.fit_transform(df.values)
zscore_scaler = StandardScaler()
zscore = zscore_scaler.fit_transform(df.values)


def makeHist(col, raw, minmax, zscore):
    fig, axs = plt.subplots(3, 1, constrained_layout=True)
    fig.suptitle("Feature " + str(col+1))
    axs[0].hist(raw.values[:, col])
    axs[1].hist(minmax[:, col])
    axs[2].hist(zscore[:, col])
    axs[0].set_title("Before Normalization")
    axs[1].set_title("After Min-Max")
    axs[2].set_title("After ZScore")
    axs[2].set_xticks(np.arange(-4, 5, 1))
    plt.show()


def countOutliers(zscore, col=-1):
    outliers = 0
    scores = zscore[:, :]
    if col != -1:
        scores = scores[:, col]
    for row in scores:
        if col == -1:
            for score in row:
                if abs(score) > 3:
                    outliers += 1
        else:
            if abs(row) > 3:
                outliers += 1
    return outliers


def dropOutliers(zscore, col=-1):
    result = []
    for row in zscore:
        keep = True
        for score in row:
            if abs(score) > 3:
                keep = False
                break
        if keep:
            result.append(row)
    return np.array(result)


print("Before drop outliers --------------------------")
print("Total outliers: " + str(countOutliers(zscore)))
print("Feature 9 outliers: " + str(countOutliers(zscore, 8)))
print("Feature 24 outliers: " + str(countOutliers(zscore, 23)))
print()

makeHist(8, df, minmax, zscore)
makeHist(23, df, minmax, zscore)

zscore = (dropOutliers(zscore))
print("After drop outliers --------------------------")
print("Total outliers: " + str(countOutliers(zscore)))
print("Feature 9 outliers: " + str(countOutliers(zscore, 8)))
print("Feature 24 outliers: " + str(countOutliers(zscore, 23)))
print()


# Question 2

import pandas as pd
import numpy as np
#import matlibplot as mp
from sklearn import preprocessing
from sklearn.decomposition import PCA
from numpy import linalg as LA
import matplotlib.pyplot as plt


missing_values = ['na', '', 'null']
raw = pd.io.parsers.read_csv('../../Documents/ece657a/data/DataB.csv', header = 0, delimiter = ',', na_values = missing_values, usecols = [x for x in range(1,786)], engine = 'python')
raw = raw.astype(float)
obj = raw.iloc[:, :784]
#print(obj)
#print(obj.shape)


# In[25]:


# cols = obj.columns
# for col in cols:
#     print obj[col].isnull()
obj_normed = StandardScaler().fit_transform(obj)


# In[53]:


pca = PCA(n_components = 784)
pca.fit(obj_normed)
obj_pca = pca.transform(obj_normed)
#get the eigenvectors
print(pca.components_)
#get the eigenvalues
print(pca.explained_variance_)


# 1. Use PCA as a dimensionality reduction technique to the data, compute the eigenvectors and eigenvalues.

# In[29]:


tar = raw.iloc[:, 784]
plt.scatter(obj_pca[:, 0], obj_pca[:, 1], c = tar, edgecolor = 'none')
plt.xlabel('PCA component 1')
plt.ylabel('PCA component 2')
#plt.legend()
plt.colorbar()
plt.show()

plt.scatter(obj_pca[:, 4], obj_pca[:, 5], c = tar)
plt.xlabel('PCA component 5')
plt.ylabel('PCA component 6')
plt.colorbar()
plt.show()


# 3. Plot a 2 dimensional representation of the data points based on the 5th and  6th principal components.

# In[50]:


from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
y_true = raw.iloc[:, 784]
gnb = GaussianNB()
mission = [2, 4, 10, 30, 60 ,200, 500, 784]
error = []
ret_var = []
for x in mission:
    obj_fit = obj_pca[:, 0: x]
    print(obj_fit.shape)
    #print(obj_fit)
    y_pred = gnb.fit(obj_fit, y_true).predict(obj_fit)
    #compute the error
    #error.append(accuracy_score(y_true, y_pred))
    error.append((y_true != y_pred).sum())
    ret_var.append(pca.explained_variance_ratio_.cumsum()[x-1])
print(ret_var)


# In[49]:


#plot error against the retained variance
plt.plot(ret_var, error)
plt.xlabel('retained variance')
plt.ylabel('errors')
plt.show()


#use LDA to classify
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components = 2) #reduce it to 2 dimensions
obj_lda = lda.fit(obj, y_true).transform(obj)
print(obj_lda.shape)


# In[34]:



#y_lda_pred = lda.predict(obj_lda)
#LinearDiscriminantAnalysis(n_components = 784, solver = 'svd')
plt.scatter(obj_lda[:, 0], obj_lda[:, 1], c = y_true)
plt.xlabel('LDA component 1')
plt.ylabel('LDA component 2')
plt.colorbar()
plt.show()


# As we can see from the above diagram, the result of LDA is much better than that of PCA. 3 of the classes are widely separated.

# Question 3

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import ShuffleSplit, cross_val_score, train_test_split
from sklearn.manifold import LocallyLinearEmbedding, Isomap

def get_image(im_df, row, zoom):
    p = im_df.values[row, 1: len(im_df.columns) - 1]
    p = p.reshape(28, 28)
    off_image = OffsetImage(p, zoom=zoom, cmap=plt.cm.binary)
    return off_image


def plot_three(prefix, df, col1, col2, im_df, zoom):
    fig, ax = plt.subplots(1, 1)
    x = df.values[:, col1]
    y = df.values[:, col2]
    ax.scatter(x, y, alpha=0)
    ax.set_title(prefix + " - Comp " + str(col1+1) +
                 " vs Comp " + str(col2+1))
    ax.set_xlabel("Comp " + str(col1+1))
    ax.set_ylabel("Comp " + str(col2 + 1))
    i = 0
    for x0, y0 in zip(x, y):
        ab = AnnotationBbox(get_image(im_df, i, zoom), (x0, y0), frameon=False)
        ax.add_artist(ab)
        i += 1
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()


df = pd.read_csv('../../Documents/ece657a/data/DataB.csv')
df = df.astype(float)
target = df['gnd']
data = df.values[:, 1: len(df.columns) - 1]
threes_df = df.loc[df['gnd'] == 3]
threes_data = threes_df.values[:, 1: len(df.columns) - 1]
threes_data = (threes_data - threes_data.min()) / \
    (threes_data.max() - threes_data.min())
n_neighbors = 5
n_components = 4

# 1. Apply LLE

lle = LocallyLinearEmbedding(n_neighbors=n_neighbors,
                             n_components=n_components)
lle_data = lle.fit_transform(threes_data)
lle_df = pd.DataFrame(lle_data)
plot_three("LLE", lle_df, 0, 1, threes_df, 0.45)

# 2. Apply ISOMAP
iso = Isomap(n_neighbors=n_neighbors, n_components=n_components)
iso_data = iso.fit_transform(threes_data)
iso_df = pd.DataFrame(iso_data)
plot_three("Isomap", iso_df, 0, 1, threes_df, 0.45)


# 3. Use the Naive Bayes classier to classify the dataset based on the projected 4-dimension representations of the LLE and ISOMAP.
df_data = df.values[:, 1: len(df.columns) - 1]
test_size = 0.3


def calc_mean_accuracy(data, threshold=0.00015, miniter=500):
    print("Diff threshold {}".format(thresh))
    i = 0
    scores = []
    mean_accuracy = 0
    gnb = GaussianNB()
    cols = data.shape[1]
    diff = 0
    while True:
        train, test = train_test_split(data, test_size=test_size)
        gnb.fit(train[:, 0:cols - 1], train[:, cols - 1])
        score = gnb.score(test[:, 0:cols - 1], test[:, cols - 1])
        i += 1
        scores.append(score)
        mean = np.mean(scores)
        diff = (abs(mean_accuracy - mean))
        mean_accuracy = mean
        if diff < threshold and i > miniter:
            break
    return mean_accuracy, i

scaler = StandardScaler()
scaler.fit(data)
norm_data = scaler.transform(data)
norm_df = pd.DataFrame(norm_data)
norm_df.columns = df.columns[1:len(df.columns)-1]
pca = PCA()
pca.fit(norm_df.values)
principal_comps = pca.transform(norm_df.values)

thresh = 0.00000005

start = time.time()
lle_data = lle.fit_transform(df_data)
lle_df = pd.DataFrame(lle_data)
end = time.time()
acc, it = calc_mean_accuracy(
    pd.concat([lle_df, target], axis=1).values, thresh)
print("LLE - mean accuracy {} in {} iterations with thresh. {} ({}s)".format(acc,
                                                                             it, thresh, end-start))

start = time.time()
iso_data = iso.fit_transform(df_data)
iso_df = pd.DataFrame(iso_data)
end = time.time()
acc, it = calc_mean_accuracy(
    pd.concat([iso_df, target], axis=1).values, thresh)
print("Isomap - mean accuracy {} in {} iterations with thresh. {} ({}s)".format(acc,
                                                                                it, thresh, end-start))

start = time.time()
pca.fit_transform(norm_df.values)
pca_df = pd.DataFrame(principal_comps)
end = time.time()
acc, it = calc_mean_accuracy(
    pd.concat([pca_df, target], axis=1).values, thresh)
print("PCA - mean accuracy {} in {} iterations with thresh. {} ({}s)".format(acc,
                                                                             it, thresh, end-start))
start = time.time()
lda_comps = lda.fit_transform(norm_df.values, target.values)
lda_df = pd.DataFrame(lda_comps)
end = time.time()
acc, it = calc_mean_accuracy(
    pd.concat([lda_df, target], axis=1).values, thresh)
print("LDA - mean accuracy {} in {} iterations with thresh. {} ({}s)".format(acc,
                                                                             it, thresh, end-start))
