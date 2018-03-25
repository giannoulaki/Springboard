Submissions for unit 2 
<<Three ideas for your Capstone Project 1: Note that these ideas are quite preliminary, and you'll work with your mentor closely to refine them.

These ideas can be quite broad and high-level. Review them with your mentor. Your writeup should contain a short blurb for each of your ideas. The blurb should, at high level, describe the problem and the data you’ll be using to solve it. At this point, there’s no need to talk about specific methods and techniques.>>

 

## [Autism ]
Data set:
http://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult

In xl format 
https://docs.google.com/spreadsheets/d/1fCQiIaDTTgk0EVMsYI3WcoBjyEssL73KHOJI7i6h0TE/edit#gid=0

Task: Classification
Attribute Type: Categorical, continuous and binary  
Area: Medical, health and social science
Format Type: Non-Matrix
Does your data set contain missing values? Yes
Number of Instances (records in your data set): 704
Number of Attributes (fields within each record): 21

This dataset conatins ten behavioural features (AQ-10-Adult) plus ten individuals characteristics that have proved to be effective in detecting the ASD cases from controls in behaviour science. 

### Objective

To predict whether a person has the Autism or not.


### Exploratory data analysis

Visualising the data should give some insight into certain particularities of this dataset.
Some of attributes will not influence the response. 
Select features that would be useful in the context of the objective.
 
### Model building

Arter data been prepared ran regression analysis. 
Assess the quality of the model.



## [Predict whether income exceeds $50K/yr based on census data.]

https://archive.ics.uci.edu/ml/datasets/Adult

Task: Classification
Attribute Type: Categorical, continuous and binary  
Area: Social science
Format Type: Non-Matrix
Does your data set contain missing values? Yes
Number of Instances (records in your data set): 48842
Number of Attributes (fields within each record): 14

### Objective

Prediction task is to determine whether a person makes over 50K a year. .

### Exploratory data analysis

Data Mining and Visualization
Some of attributes will not influence the response. 
Select features that would be useful in the context of the objective.
Split into train-test 

 
### Model building

After preparing data run regression analysis.
Important features need to be selected for predictions as per the objective.
Assess the quality of the model.




## [ Trending YouTube videos]
https://www.kaggle.com/datasnaek/youtube-new/data


This dataset includes several months (and counting) of data on daily trending YouTube videos. Data is included for the US, GB, DE, CA, and FR regions (USA, Great Britain, Germany, Canada, and France, respectively), with up to 200 listed trending videos per day.
Each region’s data is in a separate file. Data includes the video title, channel title, publish time, tags, views, likes and dislikes, description, and comment count.The data also includes a category_id field, which varies between regions. The categories for a specific video can be retrieved from the associated JSON. 


### Objective
#### Analysing what factors affect how popular a YouTube video will be.

Statistical analysis over time.

Sentiment analysis.

Categorising YouTube videos based on their comments and statistics.

Train ML algorithm.

### Exploratory data analysis
How long usually a video can trend in different countries?
How many likes, dislikes, views and comments get by different countries?
Correlation of trending video in between countries
Videos from which category has longer trend?
Correlation between Days of Publish to Trend v/s Trending Duration
Users like videos from which CATEGORY the most?
What is the ratio of Likes-Dislikes and Views-Comments in different categories?
What's the tags in the most negative and most positive category? What's the most discuss words for Science & Technology?
How much time passes between published and trending by countries?

### Model building

After preparing data run regression analysis.
Important features need to be selected for predictions as per the objective.
Assess the quality of the model.




