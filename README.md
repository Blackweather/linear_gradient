# linear_gradient
Linear regression with gradient descent

Simple python script using gradient descent to calculate linear regression for random generated data and show it using matplotlib.

I'm not using any python modules here, just pure maths :)

# How do I go about calculating linear regression
  The hypothesis will be:  ![Hypothesis equation](http://latex.codecogs.com/gif.latex?h_%7B%5CTheta%7D%28x%29%3D%5CTheta_%7B0%7D&plus;%5CTheta_%7B1%7Dx)
  
  **To find the correct hypothesis we need to minimize the cost function**
  
The cost function is: ![Cost function](http://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B2m%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%7B%5CTheta%7D%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29%5E%7B2%7D)
    
We need to find the correct Theta values so that the cost function is minimized

How to do this?
  
  **Repeatably update theta values until we end up at global minimum (convergence)**

The equation for updating every iteration:
![Gradient descent](http://latex.codecogs.com/gif.latex?%5CTheta_%7Bj%7D%3A%3D%5CTheta_%7Bj%7D-%5Calpha%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20%5CTheta_%7Bj%7D%7DJ%28%5CTheta_%7B0%7D%2C%5CTheta%7B1%7D%29)
 - Alpha is the learning rate which I set at 0.001 for now.
 
 We calculate this equation (for j=0 and j=1) and then **simultaneously** update Theta values in our hypothesis.
 
 The equations for calculating the partial derivatives:
 
 ![Theta0](http://latex.codecogs.com/gif.latex?j%3D0%3A%20%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%5CTheta_%7B0%7D%7DJ%28%5CTheta_%7B0%7D%2C%5CTheta_%7B1%7D%29%3D%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%7B%5CTheta%7D%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29)
 
 ![Theta1](http://latex.codecogs.com/gif.latex?j%3D1%3A%20%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%5CTheta_%7B1%7D%7DJ%28%5CTheta_%7B0%7D%2C%5CTheta_%7B1%7D%29%3D%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%7B%5CTheta%7D%28x%5E%7B%28i%29%7D%29-y%5E%7B%28i%29%7D%29*x%5E%7B%28i%29%7D)
 
 # What do I need to work on?
 > solve convergence problem (not working for some cases)
 
 > change number of data to be inputtable
 
 > animate the plot with every step of gradient descent
 
 > show the hypothesis on plot
