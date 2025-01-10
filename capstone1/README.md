## Hotel Booking Cancellation Prediction Using RandomForest
- Purpose of this project is to develop a model that will predict whehter a given hotel boolking will be cacnelled or not
- The dataset used for this project is provided in the file hotel-booking.csv. It's taken from Kaggle [link](https://www.kaggle.com/datasets/muhammaddawood42/hotel-booking-cancelations?select=hotel_booking.csv)
- Each row of the dataset represents one booking, the dataset provides detailed information on hotel bookings and icludes various fields lead time, break down of number of guests into adults, children, duration the stay, whether the customer had previous cancellation history etc. 
- The field is_canceled represents whhether a booking is canceled [ denoted by value of 1] not canceled [ denoted by value of 0]. This field is the target variable and the model developed as part of this project predicts for a given random booking whether the booking may get canceled or not. 

### Data Analysis
- The dataset is mostly pre-cleaned with field names property normalized to remove spaces.
- The dataset contains guest related fields which do not hold any significance in the context of this prediction, hence all the guest specific fields like name, email, credit card etrc have been deleted before supplying the data to model
- Few fields like reservation_status,reservation_status_date are directly related to the target variable value. Hence these are removed as part of feature engineering
- The dataset contains various categorical variables and they have been encoded using LabelEncoder

### Model Selection
- Analyzed multiple models and finally decided to use a tuned RandomForestClassifier as the suitable algorithm based on the accuracy level
- Used GridSearchCV to evaluate and choose optimal hyperparameter values to be used for the RFC algorithm

### How to run the code
- The code follows the conventions as specified in the course project page. It code can be executed in multiple ways as explained below
    #### Execute locally
    - Clone or download the code from git repo [repo](https://github.com/bhaskarv/ml-zoomcamp-projects.git), navigate to the folder capstone1. Code for this project is available in the folder named capstone1
    - Pipenv is used to manage dependencies of this proejct, so the provided Pipfile has details of required libraries for this project
    - Install pipenv [if its not already installed on your machine ] and then from the capstone1 project folder run the command pipenv install. This downloads all the required libraries for the project. 
    - Then run train.py script. This creates a model that is trained on hotel bookings dataset and saves the model to a file capstone1.bin. Use the command <code>pipenv run python train.py</code>
    - Next step is to run the prediction service locally using waitress or gunicorm. Sample command using waitress <code>pipenv run waitress-serve --listen=0.0.0.0:9696 predict:app</code>. This makes prediction service endpoint available on local port 9696
    - Test the service by running predict-test.py script
    #### Use Docker to execute the code
    - After downloading the code navigate to the capstone1 folder and build a docker image. Sample command <code>docker build -t project1:v1</code>. This creates a docker image which contains an executable predic service
    - Create a docker container from the image project1:v1 using command <code>docker run --rm -p 9696:9696 project1:v1</code>. This brings up a docker container with an instance of prediction service running in it
    - Docker container created above exposes prediction service on local port 9696. Now test the service using using any HTTP clients like postman, HTTPie etc. Sample json is provided in the test.json file for use.
    - Alternatively predict-test.py can be used as well to test. This script use requests module, so it needs to be installed before running the script.
