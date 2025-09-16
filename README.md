# Programming-Assignment-3

### Problem 1
Using knowledge obtained from the experiment and demonstrations:<br/>
  a. Load the corresponding .csv file into a data frame named cars using pandas.<br/>
  b. Display the first five and last five rows of the resulting cars.<br/>

 **Code**

     import pandas as pd # import the Pandas library with the 'pd'

     # a. Load the corresponding .csv file into a data frame named cars using pandas.
     cars = pd.read_csv ('cars.csv') # Read a CSV file into a pandas DataFrame
     cars # print 
     
 **Output**
  
  <img width="474" height="343" alt="image" src="https://github.com/user-attachments/assets/5a470561-564d-4f87-a82c-c76e5bbb5d4e" /><br/> 

  <img width="475" height="404" alt="image" src="https://github.com/user-attachments/assets/a7068abc-f79c-429e-8925-75a79e7a8b5a" /><br/>


 **Code**

      # b. Display the first five rows of the resulting cars
      cars.head (5) # print the first 5 rows

 **Output**

  <img width="454" height="139" alt="image" src="https://github.com/user-attachments/assets/b7b42a89-21d2-4225-93d6-ac71cca95537" />


 **Code**

     # b. Display the last five rows of the resulting cars
     cars.tail (5) # print the last 5 rows


 **Ouput**

  <img width="679" height="230" alt="image" src="https://github.com/user-attachments/assets/b2b318ff-825e-40e8-b3cc-beda58d25352" />


 **Conclusion**
   
  To conclude, this Pandas program loads the cars.csv file into a DataFrame and displays its first five rows using .head() and last five rows using .tail(). These functions give a quick view of the dataset, helping us confirm that the file was read correctly and understand its basic structure.


### Problem 2
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and 
indexing operations.<br/>
  a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.<br/>
  b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.<br/>
  c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?<br/>
  d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.<br/>

**Code**

    import pandas as pd

    cars = pd.read_csv ('cars.csv')
    cars

**Output**
  
  <img width="474" height="343" alt="image" src="https://github.com/user-attachments/assets/5a470561-564d-4f87-a82c-c76e5bbb5d4e" /><br/> 

  <img width="475" height="404" alt="image" src="https://github.com/user-attachments/assets/a7068abc-f79c-429e-8925-75a79e7a8b5a" /><br/>


**Code**

    # a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…)
    odd_columns = cars.iloc[0:5, [1, 3, 5, 7, 9, 11]]  # Select all 5 rows and input odd number from 0-11
    odd_columns #print


**Output**

   <img width="449" height="288" alt="image" src="https://github.com/user-attachments/assets/530c7064-9a28-4aca-941a-4629637ca402" />


**Code**

    # b. Display the row that contains the 'Model' of 'Mazda RX4'
    mazda_rx4 = cars[cars['Model'] == 'Mazda RX4'] 
    mazda_rx4

**Output**
    
  <img width="528" height="61" alt="image" src="https://github.com/user-attachments/assets/e6064cf2-5cff-414d-9cf8-6c862103ac0e" />


**Code**

    # c. How many cylinders ('cyl') does the car model 'Camaro Z28' have?
    cars.loc[[23], ['Model', 'cyl']]

**Output**

   <img width="571" height="203" alt="image" src="https://github.com/user-attachments/assets/b10182b6-6f5c-4372-8e48-4f1ad275068e" />


**Code**

    # d. Determine how many cylinders ('cyl') and what gear type ('gear') do the car models 
    # 'Mazda RX4 Wag', 'Ford Pantera L' and 'Honda Civic' have
    models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
    result = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
    result


**Output**

   <img width="741" height="399" alt="image" src="https://github.com/user-attachments/assets/0a84e75a-fa95-48b7-ae26-3bd075dc3931" />


**Conclusion**
