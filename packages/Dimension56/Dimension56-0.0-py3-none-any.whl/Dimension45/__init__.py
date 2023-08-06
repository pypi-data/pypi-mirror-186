from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def reduce_dimension(data, n_components=None):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    numerical_cols = data.select_dtypes(include=[np.number]).columns
    numerical_data = data[numerical_cols]
    if n_components is None:
        n_components = int(input("Enter the number of dimensions to reduce to: "))
    if n_components <= 0 or n_components > numerical_data.shape[1]:
        raise ValueError("Invalid value for number of components")
    scaler = StandardScaler()
    numerical_data = scaler.fit_transform(numerical_data)
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(numerical_data)
    principal_df = pd.DataFrame(data = principal_components, columns = ['PC{}'.format(i) for i in range(n_components)])
    return pd.concat([data.drop(columns=numerical_cols), principal_df], axis=1)