import requests
import os
import json
import pandas as pd

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
#bearer_token = "AAAAAAAAAAAAAAAAAAAAAIQKSwEAAAAAYv7HdGUW3137xgksaaqGBb9F7Dg%3DygDxRH5F8SFqyrdQzXRKRrqr7x6lXBjf5JqX4xy0SmX46cwlie"
#bearer_token = "AAAAAAAAAAAAAAAAAAAAAFOzWAEAAAAAQH27GUd4xNyDXUGowdQU%2Bm8nDS0%3Ddumii0h3BJNWrwwVQb042zuqYUKvnzaFuHtNOzHd8vSbhWWq2U"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAF7fXwEAAAAAQj0hA1vC4h4AK3VaDWYdg1ZNeis%3DokmniUP95uHICEY5DgqFMjF8ts288VUsLYz7mURqgeIUyU2gQD"


def create_url(username):
    # Replace with user ID below
    #user_id = 1268939226231562242
    return "https://api.twitter.com/2/users/by?usernames={}".format(username)


def get_params(next_token="BLANK"):
    return {"user.fields": "name,username,created_at,description,public_metrics"}    

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
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


def main():
    
    df = pd.read_csv("ashoka_twitter_more.csv")
    usernames = list(df['username'])
    #print(usernames)
    
    desc = []
    username = []
    name = []
    idstr = []
    follower = []
    following = []
    tweet_count = []
 
    for i in range(0, len(usernames), 100):
        ids = ""
        for j in range(i, min(i+100, len(usernames))):
            ids += usernames[j]+","
        print(ids[:-1])
        url = create_url(ids[:-1])
        params = get_params()
        json_response = connect_to_endpoint(url, params)
        #print(json_response)
        if 'data' not in json_response:
            print("---No data---")
        else:
            data = json.dumps(json_response['data'], indent=4, sort_keys=True) 
            for item in json_response['data']:
                #print(item['description'])
                desc.append(item['description'])
                username.append(item['username'])
                name.append(item['name'])
                idstr.append(item['id'])
                follower.append(item['public_metrics']['followers_count'])
                following.append(item['public_metrics']['following_count'])
                tweet_count.append(item['public_metrics']['tweet_count'])
            #print(type(json_response['data']))  
        #out_file = open("influencers/users/"+str(i)+".json", "w") 
        #json.dump(json_response['data'], out_file, indent = 6) 
        #out_file.close()
        new_df = pd.DataFrame(list(zip(idstr, name, username, desc, follower, following, tweet_count)),
               columns =['id_str', 'name','username','description', 'followers', 'following', 'tweets'])
        new_df.to_excel('ashoka_twitter_more_desc.xlsx')

    print(len(desc))


if __name__ == "__main__":
    main()





