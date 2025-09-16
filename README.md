# Programming-Assignment-3

### Problem 1
Using knowledge obtained from the experiment and demonstrations:
  a. Load the corresponding .csv file into a data frame named cars using pandas
  b. Display the first five and last five rows of the resulting cars.

 **Code**

     import pandas as pd

     cars = pd.read_csv ('cars.csv')
     cars
     
 **Output**
  
  <img width="474" height="343" alt="image" src="https://github.com/user-attachments/assets/5a470561-564d-4f87-a82c-c76e5bbb5d4e" /><br/> 

  <img width="475" height="404" alt="image" src="https://github.com/user-attachments/assets/a7068abc-f79c-429e-8925-75a79e7a8b5a" /><br/>


 **Code**

      cars.head (5)


 **Output**

  <img width="454" height="139" alt="image" src="https://github.com/user-attachments/assets/b7b42a89-21d2-4225-93d6-ac71cca95537" />


 **Code**

     cars.tail (5)


 **Ouput**


 **Conclusion**



### Problem 2
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and 
indexing operations.
  a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
  b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
  c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
  d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

**Code**

    import pandas as pd

    cars = pd.read_csv ('cars.csv')
    cars

**Output**
  
  <img width="474" height="343" alt="image" src="https://github.com/user-attachments/assets/5a470561-564d-4f87-a82c-c76e5bbb5d4e" /><br/> 

  <img width="475" height="404" alt="image" src="https://github.com/user-attachments/assets/a7068abc-f79c-429e-8925-75a79e7a8b5a" /><br/>


**
