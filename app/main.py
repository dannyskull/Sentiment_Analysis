import requests
import pandas as pd
from textblob import TextBlob

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Classification Model

def polar(text):
            """
            description : define polarity score of a text using Text Blob
            (https://textblob.readthedocs.io/en/dev/)
            """
            res = TextBlob(text)
            return res.sentiment.polarity


#FastAPI


class Item(BaseModel):
      topic_name : str
      start_dt : str
      end_dt : str

app  = FastAPI()

@app.post("/classify/")
async def classify_subfeddit(item :Item):
    payload = {"skip":0,"limit":25}
    r = requests.get('http://feddit:8080/api/v1/subfeddits/',params=payload)
    print("Status Code:",r.status_code)
    response = r.json()
    user_input = item.topic_name
    user_input = str.lower(user_input)

    # Separate the info of subfeddits and their properties from the rest. 
    subfeddits = response["subfeddits"]
    # print(subfeddits)

    # Fetching the Topic Names and their respective ids
    topic_ids = {}
    for i in subfeddits:
        topic_ids[str.lower(i['title'])]=i['id']
    # print(topic_ids)

    search_subfeddit = topic_ids.get(user_input,False)
    if not search_subfeddit:
        # raise ValueError("Subfeddit not found")
        raise HTTPException(status_code=404, detail="Item not found")
    else :
        payload_2 = {"skip":0,"limit":25,"subfeddit_id":search_subfeddit}
        r_2 = requests.get('http://feddit:8080/api/v1/comments/',params=payload_2)
        print("Status Code:",r_2.status_code)
        response_2 = r_2.json()
        # print(type(response_2))
        # print(response_2)

        # Separate comments from the rest of the info
        subfeddits_comments = response_2['comments']
        # print("\n\n",subfeddits_comments)

        # Convert the json data to pandas dataframe
        df = pd.DataFrame(subfeddits_comments)


        # Step 3 classify the comments
        # Sentiment Analysis
        

        # print(df)

        df['polarity_score'] = df['text'].map(lambda x: polar(x)) # using the classification model here to classify

        # Classify sentiment positive and negative based on polarity score(-1,1)
        df['sentiment'] = df['polarity_score'].map(lambda x:"positive" if x >=0 else "negative")


        print(df)



        # Filter the comments on specific time range
        ###############################################
        # Step convert the Unix Epochs into datetime format
        df['created_at'] = pd.to_datetime(df['created_at'], unit='s')

        print(df)

        # Get user input for start date and end date
        if not item.start_dt == "" and item.end_dt == "":
            start_date_str = item.start_dt 
            
            end_date_str = item.end_dt 

            # Parse user input dates
            start_day, start_month, start_year = map(int, start_date_str.split('-'))
            end_day, end_month, end_year = map(int, end_date_str.split("-"))

            # Convert to standard 'YYYY-MM-DD' format
            start_date = pd.Timestamp(start_year, start_month, start_day)
            end_date = pd.Timestamp(end_year, end_month, end_day)

            # Filter DataFrame based on user input dates
            filtered_df = df[(df['created_at'].dt.date >= start_date.date()) & (df['created_at'].dt.date <= end_date.date())]
            # print("\n\n")
            # print(filtered_df)



            # Sort By Polarity Score Asceding
            ###################################
            # print("\n\n")
            # print(df.sort_values(by='polarity_score', ascending=False))
            final_df = filtered_df.sort_values(by='polarity_score', ascending=False)
            final_df.drop(columns=["username","created_at"],inplace=True)
            json_data = final_df.to_dict('records')
            print(json_data)
            print(type(json_data))
            return json_data
        else :
            final_df = df.sort_values(by='polarity_score', ascending=False)
            final_df.drop(columns=["username","created_at"],inplace=True)
            json_data = final_df.to_dict('records')
            print(json_data)
            print(type(json_data))
            return json_data
