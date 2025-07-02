from flask import Flask,request, jsonify
import pandas as pd
import os
app=Flask(__name__)
df=pd.read_csv('Coursera_courses.csv')
@app.route('/', methods=['POST'])
def webhook():
    data=request.get_json()
    topic=data['queryResult']['parameters']['course_topic']
    mod_topic=topic.replace(' ','-')
    req_details= {}
    for index, row in df.iterrows():
        if mod_topic.lower() in row['course_id'].lower():
            req_details[row['name']]=[row['institution'],row['course_url']]
    print(req_details)
    if req_details=={}:
        fulfillment_text = [f" Sorry, I couldn't find any course recommendations related to '{topic}'. Can you try a different topic?"]
        response_json = {
            "fulfillmentText": fulfillment_text,
            "fulfillmentMessages": [
                {"text": {"text": [fulfillment_text]}}
            ]
        }
    else:

        fulfillment_text_parts = [f"Here are some courses related to '{topic}':"]

        for course_id_key, course_details_list in req_details.items():
            institution = course_details_list[1]
            url = course_details_list[0]
            title = course_id_key
            fulfillment_text_parts.append(
                f"✨ {title}:\n"
                f"   Link: {institution}\n"
                f"   Institution: {url}\n"
            )
            fulfillment_text = "\n".join(fulfillment_text_parts)
    response_json = {
        "fulfillmentText": fulfillment_text,
        "fulfillmentMessages": [
            {"text": {"text": [fulfillment_text]}}
        ]
    }
    print("Sending response to Dialogflow:")
    print(response_json)
    return jsonify(response_json)


if __name__== "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)