import requests
import os
import json
import pandas as pd

# To set your environment variables in your terminal run the following line:
#bearer_token = "AAAAAAAAAAAAAAAAAAAAAIQKSwEAAAAAYv7HdGUW3137xgksaaqGBb9F7Dg%3DygDxRH5F8SFqyrdQzXRKRrqr7x6lXBjf5JqX4xy0SmX46cwlie"
#bearer_token = "AAAAAAAAAAAAAAAAAAAAAFOzWAEAAAAAQH27GUd4xNyDXUGowdQU%2Bm8nDS0%3Ddumii0h3BJNWrwwVQb042zuqYUKvnzaFuHtNOzHd8vSbhWWq2U"

# Academic API
bearer_token = "AAAAAAAAAAAAAAAAAAAAAO28XgEAAAAAnFqck6mNOk8DA3uHDMlx19i32qU%3DX2o5kB2tU7fqKSjBXIYguE9iZJQKVrear235Nfn8lhDCPgVp0G"

def create_url(user_id):
    # Replace with user ID below
    #user_id = 1268939226231562242
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params(next_token="BLANK"):
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    #print(type(next_token))
    max_num = 100
    if next_token == "BLANK":
        return {"tweet.fields": "created_at,entities,public_metrics",
        "user.fields": "name,username,public_metrics", 
        "exclude": "retweets,replies", 
        "start_time": "2023-01-01T00:00:00.000Z",
        "expansions": "entities.mentions.username,referenced_tweets.id.author_id",
        "max_results": max_num}
    else:
        return {"tweet.fields": "created_at,entities,public_metrics",
        "user.fields": "name,username,public_metrics", 
        "exclude": "retweets,replies", 
        "start_time": "2023-01-01T00:00:00.000Z",
        "expansions": "entities.mentions.username,referenced_tweets.id.author_id",
        "max_results": max_num,
        "pagination_token": next_token}


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
    
    df = pd.read_excel("ashoka_twitter_more_desc.xlsx", index_col=0, dtype=object).reset_index()
    print(len(df))

    for i in range(0,len(df)) : # till (651 - 972)
        print("Sl No: ",i)
        user_id = df.at[i,'id_str']
        filename = df.at[i,'username']
        print(filename)
        tweets = []
        url = create_url(user_id)
        params = get_params()
        json_response = connect_to_endpoint(url, params)
        if 'data' not in json_response:
            print("---No data---")
            continue
        data = json.dumps(json_response['data'], indent=4, sort_keys=True)
        #print(data)
        tweets = json_response['data']
        #print(tweets)

        # the json file where the output must be stored 
        out_file = open("tweets/"+filename+".json", "w") 
        json.dump(tweets, out_file, indent = 6) 
        #print()
        out_file.close()
        print(f"Update: {len(tweets)} tweets from username:{filename} have been saved") 


if __name__ == "__main__":
    main()





