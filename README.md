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


# Data Schemas
## Classify

+ **id**: unique identifier of the comment.
+ **text**: content of the comment in free text format.
+ **polarity_score**: polarity score of the comment
+ **sentiment**: classification of the comment [postive/negative] based on polarity score [-1,1]

