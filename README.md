# GOOGLE-CLOUD-ENGINEERING

Developed a microservice using Python, Flask for Google Cloud Functions which takes two sets of arrays as an input from HTTP request in the form of JSON payload, sorts both the arrays and combine them using 'merge sort algorithm'(both the arrays are first sorted and then merged in order to reduce the overall time complexity).   
Lastly, the function returns the resultant array(sorted and merged) in JSON format. 

By default the timeout of Cloud Functions is 60 seconds but as per the problem statement, the timeout was set to 180 seconds/3 minutes.

Finaly, deployed the microservice on Google Cloud Functions (https://asia-south1-the-outcome-307018.cloudfunctions.net/GCE)
![image](https://user-images.githubusercontent.com/45229737/119220303-85452b00-bb07-11eb-97d0-ca1071200398.png)


The service was thoroughly tested using Postman software 
![image](https://user-images.githubusercontent.com/45229737/119220345-b02f7f00-bb07-11eb-88ab-39d96dcdf77d.png)
