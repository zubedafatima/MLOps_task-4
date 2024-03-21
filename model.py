import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.metrics import accuracy_score
######################
####------------------Model code used: https://www.kaggle.com/code/scratchpad/notebook11e062f5d8/edit ------######
######################



df = pd.read_csv("fraud_test.csv")
df.drop(columns='Unnamed: 0', inplace=True)

date_time = pd.to_datetime(df['trans_date_trans_time'], format='%d/%m/%Y %H:%M')

df['trans_date'] = date_time.dt.date[0]
df['trans_time'] = date_time.dt.time[0]

df.drop(columns='trans_date_trans_time', inplace=True)

X = df.drop(columns=['is_fraud', 'trans_date', 'trans_time', 'dob', 'first', 'last', 'trans_num', 'cc_num'])
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

numerical_columns = [2, 7, 8, 9, 10, 12, 13, 14]
nominal = [0, 1, 3, 4, 5, 6, 11]

handle_numerical = Pipeline(steps=[
    ('impute_numerical', SimpleImputer(strategy='mean'))
])

handle_categorical = Pipeline(steps=[
    ('impute_cat', SimpleImputer(strategy='most_frequent')),
    ('encode_cat', OrdinalEncoder())
])

preprocessing = ColumnTransformer(transformers=[
    ('numerical', handle_numerical, numerical_columns),
    ('categorical', handle_categorical, nominal)
], remainder='passthrough')

model = DecisionTreeClassifier()

pipe = make_pipeline(preprocessing, model)

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

with open('model.pkl', 'wb') as f:
    pickle.dump(pipe, f)