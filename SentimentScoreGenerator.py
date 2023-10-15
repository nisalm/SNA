class SentimentScoreGenerator:
    def get_sentiment(comment):
        MODEL = "gpt-3.5-turbo"

        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a sentiment analysis model."},
                {"role": "user", "content": f"Rate the sentiment of following text in the scale of 0 to 1 in two decimal places and give the answer in as one number, '{comment}'"},
            ],
            temperature=0,
        )
        return response["choices"][0]["message"]["content"]

    def get_sentiment_json(comments):
        MODEL = "gpt-3.5-turbo"

        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a sentiment analysis model."},
                {"role": "user", "content": f"Rate the sentiment of text in 'comment' key of json objects of array given below. Rate it in the scale of 0 to 1 in two decimal places where 0 mean highly negative , give the answer as a key 'sentiment' in same as a single json object.\n ```{json.dumps(comments)}```"},
            ],
            temperature=0,
        )
        return response["choices"][0]["message"]["content"]

    def Combiner():
        comments = []
        for i , row  in comments_data.iterrows():

        comments.append({
            "id": row["id"],
            "comment": row["comment"]
        })

        BATCH_SIZE = 10
        all_data = []
        sentiment_data = []
        for i in range(0, len(comments), BATCH_SIZE):
        data = comments[i:i+BATCH_SIZE]
        print(data)
        try:
            content = get_sentiment_json(data)
            print(content)
            s_array = json.loads(content)["sentiment"]
            sentiment_data += s_array
        except Exception as e:
            print(f"Can't find sentiment {str(e)}")
            continue
        if len(sentiment_data) == 200:
            pd.DataFrame(sentiment_data).to_csv(f"/content/gdrive/MyDrive/nisal/sentiment/{i+BATCH_SIZE}.csv")
            all_data += sentiment_data
            sentiment_data = []