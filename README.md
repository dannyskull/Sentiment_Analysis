# Sentiment_Analysis
RestAPI for Sentiment Classification

# Introduction
The `docker-compose.yml` file provides access to `Feddit` which is a fake reddit API built to complete the Allianz challenge. 
The `backend.yaml` file provides accedd to `Sentiment Ananlysis` which is mentioned in the Engineering Challange

# How-to-run
1. Please make sure you have docker installed.
2. To run `Feddit` and `Sentiment Analysis` API locally in the terminal, replace `<path-to-docker-compose.yml>` by the actual path of the given `docker-compose.yml` file in `docker compose -f docker-compose.yml -f backend.yaml up -d`.
3. `Feddit` should be available in [http://localhost:8080](http://localhost:8080).
4. `Sentiment Analysis` should be available in [http://localhost:8000](http://localhost:8000)
5. To stop `Feddit` and `Sentiment Analysis` API in the terminal,  use  `docker compose -f docker-compose.yml -f backend.yaml down  `.

# API Specification
`Feddit`
Please visit either [http://localhost:8080/docs](http://localhost:8080/docs) or [http://127.0.0.1:8080/redoc](http://0.0.0.0:8080/redoc) for the documentation of available endpoints and examples of the responses.
`Sentiment Analysis`
Please visit either [http://localhost:8000/docs](http://localhost:8000/docs) or [http://l27.0.0.1:8000/redoc](http://localhost:8000/redoc) for the documentation of available endpoints and examples of the responses.
There are 3 subfeddits available. For each subfeddit there are more than 20,000 comments, that is why we use pagination in the JSON response with the following parameters:
+ `skip` which is the number of comments to be skipped for each query
+ `limit` which is the max returned number of comments in a JSON response.

## Testing Classfify API
### input paraments
+ `topic_name` which the subfeddit topic name
+ `star_dt` which is the start date of the date range filter
+ `end_dt` which is the start date of the date range filter

### sample request body for classify
`{
  "topic_name": "dummy topic 1",
  "start_dt": "",
  "end_dt": ""
}`
#### NOTE : Please leave the date range blank if you do not want to filter by date as shown in the sample request body 
#### NOTE : If using the date range filter use this format "dd-mm-yyyy" as shown below. Use "-" hyphen as a separator between dd, mm, and yyyy.
`{
  "topic_name": "dummy topic 1",
  "start_dt": "17-04-2024",
  "end_dt": "20-04-2024"
}`

# Data Schemas
## Classify

+ **id**: unique identifier of the comment.
+ **text**: content of the comment in free text format.
+ **polarity_score**: polarity score of the comment
+ **sentiment**: classification of the comment [postive/negative] based on polarity score [-1,1]

# Run Pytest on Local machine
To run pytest on local machine follow these steps:
0. Install the dependencies using requirements.txt in your virtual environment.
1. Run the docker image of feddit api which you provided me with (I have not included the original feddit in this repo to avoid confusion) in a terminal.
2. Do these changes in main.py as show below :
+ Change line number 33 :
  + 33 `r = requests.get('http://feddit:8080/api/v1/subfeddits/',params=payload)`
  + TO
  + 33 `r = requests.get('http://localhost:8080/api/v1/subfeddits/',params=payload)`

+ AND

+ Change line number 55 :
  + 55 `r_2 = requests.get('http://feddit:8080/api/v1/comments/',params=payload_2)`
  + TO 
  + 55 `r_2 = requests.get('http://localhost:8080/api/v1/comments/',params=payload_2)`
3. Run this on a separate terminal `uvicorn app.main:app`
4. Run this on a separate terminal `pytest`


