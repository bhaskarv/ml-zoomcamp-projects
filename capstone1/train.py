
import pickle
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer

from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


df = pd.read_csv('hotel_booking.csv')

# Data cleanup
# Deleting these features are they do not influence the outcome 
del df['email']
del df['name']
del df['phone-number']
del df['credit_card']
del df['company']
del df['reservation_status']
del df['reservation_status_date']

# Handle missing values 
df.children = df.children.fillna(0).astype(int)
df.country = df.country.fillna(df.country.mode()[0])
df.agent = df.agent.fillna(df.agent.median()).astype(int)


# Month is stored as string, convert it to integer for supplying it to model
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
df.arrival_date_month = df.arrival_date_month.map(month_map)

# Columns with string values should be convereted to int for the model to do effective prediction
obj_columns = df.columns[df.dtypes=='object'].to_list()
encoder = LabelEncoder();
for col in obj_columns:
    df[col] = encoder.fit_transform(df[col])

# Split the dataset and then train the model
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)

y_train = df_train.is_canceled
y_test = df_test.is_canceled
y_val = df_val.is_canceled

del df_train['is_canceled']
del df_val['is_canceled']
del df_test['is_canceled']

dv = DictVectorizer(sparse=False)
train_dict = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

model = RandomForestClassifier(max_depth=20, min_samples_leaf=10, n_estimators=50,n_jobs=-1, random_state=42)
model.fit(X_train, y_train)

print('Model training is completed')

print('Validating the model')
val_dict = df_val.to_dict(orient='records')
X_val = dv.transform(val_dict)
y_pred = model.predict(X_val)

print(f'Accuracy Score',accuracy_score(y_val, y_pred))


# Save the model to a bin file for later use
output_file = 'capstone1.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'The model is saved to file {output_file}')
