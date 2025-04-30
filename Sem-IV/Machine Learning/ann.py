import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("Raisin_Dataset.csv") 
df.head() 
x = df.iloc[:,:-1] 
y = df.iloc[:,-1] 
print(y) 
from sklearn.preprocessing import LabelEncoder 
le = LabelEncoder() 
y = le.fit_transform(y) 
print(y) 
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler() 
x = scaler.fit_transform(x) 
print(x) 
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) 
class simpleAnn: 
def __init__(self,input_size,output_size,learning_rate= 0.01): 
self.weights = np.random.rand(input_size,output_size)* np.sqrt(1/input_size) 
self.learning_rate = learning_rate 
self.loss_history = [] 
self.accuracy_history = [] 
def sigmoid(self,x): 
return 1/(1+np.exp(-x)) 
def sigmoid_derivative(self,x): 
return x*(1-x) 
def predict(self,x): 
return self.sigmoid(np.dot(x,self.weights)) 
def compute_accuracy(self,x,y): 
predictions = self.predict(x) 
binary_prediction = (predictions>=0.5).astype(int) 
accuracy = np.mean(binary_prediction == y)*100 
return accuracy 
def plot_accuracy_curve(self): 
plt.plot(range(1,len(self.accuracy_history)+1),self.accuracy_history,label = "Accuarcy Curve",color 
= 'green') 
plt.xlabel("Epochs") 
plt.ylabel("Accuracy(%)") 
plt.title("Accuracy Curve") 
plt.legend() 
plt.show() 
def train(self,x,y,epochs = 100): 
for epoch in range(epochs): 
y_pred = self.predict(x) 
error = y-y_pred 
gradient = np.dot(x.T,error*self.sigmoid_derivative(y_pred))/len(x) 
self.weights += self.learning_rate*gradient 
loss = np.mean(error)**2 
self.loss_history.append(loss) 
accuracy = self.compute_accuracy(x,y) 
self.accuracy_history.append(accuracy) 
if epoch%100 == 0: 
print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.6f}") 
def plot_loss_curve(self): 
plt.plot(range(1, len(self.loss_history) + 1), self.loss_history, label="Loss Curve") 
plt.xlabel("Epochs") 
plt.ylabel("Loss (MSE)") 
plt.title("Loss Curve") 
plt.legend() 
plt.show() 
y_train = y_train.reshape(-1, 1) 
y_test = y_test.reshape(-1, 1) 
input_size = x.shape[1] 
output_size =1 
learning_rate = 0.01 
ann = simpleAnn(input_size,output_size,learning_rate) 
ann.train(x_train,y_train,epochs = 1000) 
predictions = ann.predict(x_test) 
binary_predictions = (predictions >= 0.5).astype(int) 
print(binary_predictions) 
predictions = ann.predict(x_test) 
binary_predictions = (predictions >= 0.5).astype(int) 
correct_predictions = np.sum(binary_predictions == y_test) 
total_samples = y_test.shape[0] 
accuracy = (correct_predictions / total_samples) * 100 
print(f"Accuracy: {accuracy:.2f}%") 
ann.plot_loss_curve() 
ann.plot_accuracy_curve()