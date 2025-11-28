import pandas as pd
from surprise import SVD, Dataset, accuracy
from surprise.model_selection import train_test_split

data = Dataset.load_builtin('ml-100k')
df = pd.DataFrame(data.raw_ratings,
                  columns=['user', 'item', 'rating', 'timestamp'])

print("User–Item Rating Matrix:")
print(df.pivot(index='user', columns='item', values='rating'))

train, test = train_test_split(data, test_size=0.2, random_state=42)

model = SVD().fit(train)

print("\nRMSE on Test Data:")
accuracy.rmse(model.test(test))
