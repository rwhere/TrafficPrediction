# TrafficPrediction

For testing purpose, SVM is used. 
http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html


## For this simple exercise, 3 parameters are focused
### kernel
Kernel type of the algorithm. 

 possible values: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
 
 Default: rbf (radial basis function kernel). It is a non-linear function which works well with lots of input data.
 
 Tested: linear (simple and fast). But it doesn't work well with lots of input data. Since this is a test and output is the same, this is used.
  
 Used: rbf (mainly to test gamma value)

### C
Error Term.

Based on this source, 
https://www.quora.com/What-are-C-and-gamma-with-regards-to-a-support-vector-machine
&
http://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel
The higher the value of C, the smaller the margin plane is and the better the result. 

But it doesn't make a difference with only 5 sample input data. 

During the experiment, C=10 or higher does much better job than C=1

Used: C=100 just to be safe. 

### gamma
Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’.

The smaller gamma is the more accurate the model is. 

Gamma = 1: model produces bad result.
Gamma = 0.1 to 0.0001 => model produce better result.

Used: Gamma=0.001

