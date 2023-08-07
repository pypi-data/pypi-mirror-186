from sklearn.decomposition import PCA as pca_sklearn
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

class PCA(pca_sklearn):
    def __init__(self):
        super().__init__()

    def plot_contribute(self,figsize = (9,6),**kwargs):
        value = self.explained_variance_
        value = value.cumsum()/value.sum()
        plt.figure(figsize = figsize)
        plt.scatter(range(1,len(value)+1),value,**kwargs)
        plt.plot(range(1,len(value)+1),value,**kwargs)
        plt.title('Principal Component Cumulative Contribution Graph')
        plt.show()

    def plot_extract(self,data,figsize = (6,6),**kwargs):
        contri = np.array(self.explained_variance_).reshape(-1, 1)
        vec = np.array(self.components_)
        extract = contri * vec * vec
        extract = pd.DataFrame(extract.cumsum(axis=0),columns = data.columns)
        sn.heatmap(extract, annot=True, cmap=plt.cm.Blues,**kwargs)
        plt.title('Pca Variable Extraction Heat Map')
        plt.show()
