import numpy as np
from typing import List, Tuple
### YOU MANY NOT ADD ANY MORE IMPORTS (you may add more typing imports)

class MinMaxScaler:
    def __init__(self):
        self.minimum = None
        self.maximum = None
        
    def _check_is_array(self, x:np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)
            
        assert isinstance(x, np.ndarray), "Expected the input to be a list"
        return x
        
    
    def fit(self, x:np.ndarray) -> None:   
        x = self._check_is_array(x)
        self.minimum=x.min(axis=0)
        self.maximum=x.max(axis=0)
        
    def transform(self, x:np.ndarray) -> np.ndarray:
        """
        MinMax Scale the given vector
        """
        x = self._check_is_array(x)
        diff_max_min = self.maximum - self.minimum
        scaled_x = (x - self.minimum)/ diff_max_min
        # TODO: There is a bug here... Look carefully! 

        return (x-self.minimum)/(self.maximum-self.minimum)

        return scaled_x

    
    def fit_transform(self, x:list) -> np.ndarray:
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)
    
    
class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None
        
    def fit(self, x:np.ndarray) -> None:
        """
        Compute the mean and standard deviation of the input data.

        Args:
            x (np.ndarray): Input data.

        Returns:
            None
        """
        self.mean = np.mean(x, axis=0)
        self.std = np.std(x, axis=0)

    def transform(self, x:np.ndarray) -> np.ndarray:
        """
        Standardize the given vector.
        """
        return (x - self.mean) / self.std

    def fit_transform(self, x:np.ndarray) -> np.ndarray:
        """
        Fit to data, then transform it.

        Args:
            x (np.ndarray): Input data.

        Returns:
            np.ndarray: Transformed data.
        """
        self.fit(x)

        return self.transform(x)

        return self.transform(x)


