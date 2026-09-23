import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sub_data = pd.read_csv("machine learning competition\sample_submission.csv")
#visualization
plt.figure(figsize=(10, 6))
plt.title("Predicted House: Sale Price")
sns.regplot(x=sub_data['Id'], y=sub_data.SalePrice)
plt.xlabel("House ID")
plt.ylabel("House's Price")



