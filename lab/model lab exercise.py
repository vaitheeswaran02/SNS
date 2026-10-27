Take a real-world dataset. First, clean the data by handling any missing values or inconsistencies, then perform analysis to identify at least two significant patterns or insights relevant to the business. Finally, visualize the key findings using appropriate graphs or charts and summarize how big data analysis helps in making better business decisions.


First Exp

Run: !pip install -q plotly scikit-learn
Next: !pip install -q plotly scikit-learn
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns, plotly.express as px
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
df=pd.read_csv('/content/healthcare_dataset.csv')
df.columns=df.columns.str.strip().str.replace(' ','_',regex=False)
df.fillna('Unknown',inplace=True)
df['Date_of_Admission']=pd.to_datetime(df['Date_of_Admission'],errors='coerce')
df['Discharge_Date']=pd.to_datetime(df['Discharge_Date'],errors='coerce')
df['Stay_Duration']=(df['Discharge_Date']-df['Date_of_Admission']).dt.days.fillna(0).astype(int)
print(df.describe(include='all'))
print(df['Medical_Condition'].value_counts().head(10))
sns.countplot(data=df,x='Medical_Condition',hue='Gender')
plt.xticks(rotation=45); plt.show()
sns.barplot(data=df,x='Medical_Condition',y='Billing_Amount',estimator=np.mean)
plt.xticks(rotation=45); plt.show()
sns.heatmap(df[['Age','Billing_Amount','Stay_Duration']].corr(),annot=True)
plt.show()
for c in ['Medical_Condition','Insurance_Provider','Admission_Type']:
    df[c]=LabelEncoder().fit_transform(df[c].astype(str))
X=df[['Age','Stay_Duration','Medical_Condition','Insurance_Provider','Admission_Type']]
y=df['Billing_Amount']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression().fit(X_train,y_train)
pred=model.predict(X_test)
print('MAE:',mean_absolute_error(y_test,pred),'R2:',r2_score(y_test,pred))
px.scatter(df,x='Stay_Duration',y='Billing_Amount',color='Medical_Condition').show()
df.to_csv('/content/healthcare_processed.csv',index=False)
print('Processed dataset saved successfully!')
