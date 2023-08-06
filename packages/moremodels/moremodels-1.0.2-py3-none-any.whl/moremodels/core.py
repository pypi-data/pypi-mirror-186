from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from inspect import isfunction

class WeightedModels:
    def __init__(self, models, trainSplit = 0.85, randomState = 42, error = None):
        '''
        Takes a list of models, and then gives each model a weight based on their performance.

        ``` models ``` Receives a list of models.
        ``` trainsplit ``` Determains the percentage of the data you want to train the model on.
        ``` randomState ``` Sets a random state you wish, such that it splits the data based on given number
        ``` error ``` Pass an error function, to set how you would want the model to predict
        
        '''
        if type(models) is list:
            self.__models = models
        else:
            raise TypeError("Initialization expected a list of models, instead got " + str(type(models)))

        if error is None:
            self.__error = mean_squared_error
        elif isfunction(error):
            self.__error = error
        else:
            raise TypeError("Initialization expected an error function, instead got " + str(type(models)))

        if trainSplit >= 1:
            raise Exception("trainSplit expected to be less than 1")

        self.trainSplit = trainSplit
        self.randomState = randomState
        self.__weights = []

    @property
    def models(self):
        return self.__models

    @property
    def modelWeights(self):
        if not self.__weights:
            raise Exception("Models are not fitted yet. Use .fit() before calling .showWeights()")            
        
        return self.__weights
            
    def fit(self, X, y, showScores = True):
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(X, y, train_size=self.trainSplit, random_state=self.randomState)
        
        for model in self.__models:
            model.fit(self.__X_train, self.__y_train)  
        
        self.__calculateWeights()

        if showScores:
            self.__showScores()  
        
    def __calculateWeights(self):
        preds = []
        acc = []
        for model in self.__models:
            preds.append(model.predict(self.__X_test))

        for pred in preds:
            acc.append(self.__error(self.__y_test, pred))
            
        tempo = list(map(lambda x: (sum(acc)-x),acc))
        self.__weights = list(map(lambda x: x/sum(tempo) ,tempo))

    def predict(self, X):
        if not self.__weights:
            raise Exception("Models are not fitted yet. Use .fit() before calling .predict()")
        
        preds = []
        for model in self.__models:
            preds.append(model.predict(X))
        
        for i in range(len(preds)):
            preds[i] = (list(map(lambda x: x * self.__weights[i], preds[i])))
            
        return [sum(x) for x in zip(*preds)]

    def setModelWeights(self, weights, showScores = True ,Silent = False):
        if not Silent:
            print('Warning: This function should be run after .fit(), since .fit() overwrites your new weights.')

        if sum(weights) <= 0:
            raise Exception("The sum of your weights cannot be below or equal to 0.")

        if len(weights) != len(self.__models):
            raise Exception("Expected weights inputed ("+ str(len(weights)) +") to be the same length as the number of models (" + str(len(self.__models)) +").")

        self.__weights = list(map(lambda x: x/sum(weights) ,weights))
        self.__showScores()

    def __showScores(self):
        preds = []
        for model in self.__models:
            preds.append(model.predict(self.__X_test))

        for i in range(len(preds)):
            preds[i] = (list(map(lambda x: x * self.__weights[i], preds[i])))
        
        print("Weighted model error is:", self.__error(self.__y_test,[sum(x) for x in zip(*preds)]))
    