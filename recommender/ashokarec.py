import pandas as pd
import os
import json
import random


'''
usernames = []
userids = []
names = []
tweets = []
followers = []

for file in os.listdir("../datasets/following"):
	#print(file)
	df = pd.read_excel("../datasets/following/"+file)
	usernames.extend(list(df['username']))
	userids.extend(list(df['id_str']))
	names.extend(list(df['name']))
	tweets.extend(list(df['tweets']))
	followers.extend(list(df['followers']))

for file in os.listdir("../datasets/follower"):
	#print(file)
	df = pd.read_excel("../datasets/follower/"+file)
	usernames.extend(list(df['username']))
	userids.extend(list(df['id_str']))
	names.extend(list(df['name']))
	tweets.extend(list(df['tweets']))
	followers.extend(list(df['followers']))


df = pd.DataFrame(list(zip(usernames, userids, names, tweets, followers)),columns =['username', 'id','name', 'tweets', 'followers'])
print(len(df))
df = df.drop_duplicates(subset=['username'])
print(len(df))
df = df[df['tweets']>100]
df = df[df['followers']>100]
print(len(df))

df.to_excel('../datasets/all_ashoka.xlsx')
'''
ashokanet = pd.read_excel('../datasets/all_ashoka.xlsx')
ashokanet_users = list(ashokanet['username'])

df2 = pd.read_csv('../datasets/ashoka_twitter_more.csv')
users = list(df2['username'])

init_row = ['username','rec_1','rec_2','rec_3','rec_4','rec_5']
data = []
data.append(init_row)
#print(data)

for user in users:
	#print(user)
	curr_row = [user]
	following = list(pd.read_excel("../datasets/following/"+str(user)+".xlsx")['username'])
	#print(following)
	feasible = list(set(ashokanet_users).difference(set(following)))
	#print(feasible)
	recs = random.choices(feasible, k=5)
	curr_row.extend(recs)
	#print(recs)
	data.append(curr_row)

#print(data)

df = pd.DataFrame(data[1:],columns=data[0])
print(df)
df.to_excel('recommendations/day7.xlsx')
