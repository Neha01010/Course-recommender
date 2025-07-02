from flask import Flask,request, jsonify
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
app=Flask(__name__)
df=pd.read_csv('Coursera_courses.csv')

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    data = request.get_json()
    print("Received Telegram update:", data)

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        user_message = data['message'].get('text', '').lower().strip()

        # Format topic
        mod_topic = user_message.replace(' ', '-')

        # Search in DataFrame
        req_details = {}
        for index, row in df.iterrows():
            if mod_topic in row['course_id'].lower():
                req_details[row['name']] = [row['institution'], row['course_url']]

        # Prepare reply
        if not req_details:
            reply_text = f"❌ Sorry, I couldn't find any courses related to '{user_message}'. Try another topic?"
        else:
            lines = [f"📚 Courses for *{user_message}*:"]
            for title, (institution, url) in req_details.items():
                lines.append(f"✨ *{title}*\n🔗 [Course Link]({institution})\n🏛 Institution: {url}\n")
            reply_text = "\n\n".join(lines)

        # Send reply back to Telegram
        payload = {
            "chat_id": chat_id,
            "text": reply_text,
            "parse_mode": "Markdown",  # Allows bold/italic/links
            "disable_web_page_preview": True
        }
        requests.post(TELEGRAM_API_URL, json=payload)

    return "OK", 200

'''def webhook():
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
                f"✨ {title}:"
                f"   Link: {institution}"
                f"   Institution: {url}"
            )
            fulfillment_text = .join(fulfillment_text_parts)
    response_json = {
        "fulfillmentText": fulfillment_text,
        "fulfillmentMessages": [
            {"text": {"text": [fulfillment_text]}}
        ]
    }
    print("Sending response to Dialogflow:")
    print(response_json)
    return jsonify(response_json)
'''

if __name__== "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)