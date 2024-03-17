from collections import Counter

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
pio.templates.default = "plotly_white"


# loading the dataset
df = pd.read_csv('D:/EDA internship/Instagram data.csv',encoding='latin1')
# Show column names and have a look at their info.
# column names
print(df.columns)
# info
print(df.info)

# Show the descriptive statistics of the data.
print(df.describe())
# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)
# exploring the Impressions
impressions_count=df['Impressions'].value_counts()
# Create a histogram for the 'Impressions' column
fig = px.histogram(df, x='Impressions', title='Impressions Distribution')

# Show the plot
fig.show()

# Q.5: Have a look at the number of impressions on each post over time as shown below
df['Index']=df.index
fig2= px.line(df, x='Index', y='Impressions', title='Number of Impressions on Each Post Over Time')
fig2.show()
#  Have a look at all the metrics like Likes, Saves, and Follows from each post over time as
# shown below
fig3= px.line(df, x='Index', y=['Likes','Saves','Follows'], title='Number of Impressions on Each Post Over Time')
fig3.show()
# Q.7: Have a look at the distribution of reach from different sources as shown below
reach_sources=df.iloc[:,1:6].sum()
fig4=px.pie(names=reach_sources.index,values=reach_sources,title="Distribution of Impressions")
fig4.show()

reach_sources2=df.iloc[:,5:9].sum()
fig5=px.pie(names=reach_sources2.index,values=reach_sources2,title="Engangments")
fig5.show()

#  Have a look at the relationship between the number of profile visits and follows as shown
# below
fig6=px.scatter(df,x='Profile Visits',y='Follows',color_continuous_scale='blues',title="Relationship between the number of profile visits and follows")
fig6.show()

# Combine all hashtags into a single string
all_hashtags = ' '.join(df['Hashtags'])

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_hashtags)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud of Hashtags')
plt.axis('off')
plt.show()

# Q.11: Have a look at the correlation between all the features as shown below
# Select only numeric columns
numeric_df = df.select_dtypes(include=['int', 'float'])
corr_matrix=numeric_df.corr()
# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()


print(corr_matrix)

#  Havea look at the distribution of hashtags to see which hashtag is used the most in all the
# posts as shown below
# Extract hashtags from the "Hashtags" column
hashtags_list = df['Hashtags'].str.split().sum()

# Count the frequency of each hashtag
hashtags_counts = Counter(hashtags_list)

# Get the top 10 most used hashtags
top_hashtags = hashtags_counts.most_common(25)

# Extract hashtags and their frequencies
top_hashtags, frequencies = zip(*top_hashtags)

# Plot the distribution of hashtags
plt.figure(figsize=(10, 6))
plt.bar(top_hashtags, frequencies, color='skyblue')
plt.xlabel('Hashtags')
plt.ylabel('Frequency')
plt.title('Distribution of Hashtags')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()