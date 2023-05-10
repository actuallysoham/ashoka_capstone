# Followings Collector

import pandas as pd
import requests
import os
import json

#EVELATED:
#bearer_token = "AAAAAAAAAAAAAAAAAAAAAF7fXwEAAAAAQj0hA1vC4h4AK3VaDWYdg1ZNeis%3DokmniUP95uHICEY5DgqFMjF8ts288VUsLYz7mURqgeIUyU2gQD"

#ACAD:
#bearer_token = "AAAAAAAAAAAAAAAAAAAAAO28XgEAAAAAnFqck6mNOk8DA3uHDMlx19i32qU%3DX2o5kB2tU7fqKSjBXIYguE9iZJQKVrear235Nfn8lhDCPgVp0G"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOjSdQEAAAAAWgvbsx35I3FrjWt9Df2StS0vh5M%3Dsq7BwxftiTmmAFqmkL8c9MoGaeYtaManNT6f5l8T6nZ9iiauvc"

def create_url(user_id):
    # Replace with user ID below
    return "https://api.twitter.com/2/users/{}/following".format(user_id)


def get_params(next_token="BLANK"):
    if next_token == "BLANK":
        return {"user.fields": "created_at,public_metrics,description","max_results":1000}
    else:
        return {"user.fields": "created_at,public_metrics,description","max_results":1000, "pagination_token": next_token}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FollowingLookupPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

df = pd.read_csv("final_users.csv")
print(df)

seed_usernames = list(df['username'])
seed_ids = list(df['id_str'])


for i in range(0,15): # skipped nums: 4,5,6
	print("Index: ", i)
	user_id = seed_ids[i]
	filename = seed_usernames[i]
	print("current user: "+str(filename))
	username = []
	name = []
	followers = []
	following = []
	tweets = []
	twitter_id = []
	url = create_url(int(user_id))
	params = get_params()
	json_response = connect_to_endpoint(url, params)
	#print(json_response)
	if 'data' in json_response.keys():
		for record in json_response['data']:
			username.append(record['username'])
			name.append(record['name'])
			twitter_id.append(str(record['id']))
			followers.append(record['public_metrics']['followers_count'])
			following.append(record['public_metrics']['following_count'])
			tweets.append(record['public_metrics']['tweet_count'])
		print("Data, no next token")
		
	print(len(username))

	df = pd.DataFrame(twitter_id)
	df['id_str'] = twitter_id
	df['name'] = name
	df['username'] = username
	df['followers'] = followers
	df['following'] = following
	df['tweets'] = tweets

	df.to_excel("new_follows/"+ str(filename) +".xlsx")

