# Course-recommender
# 📚 CourseRecBot - Your Telegram Course Recommender

## ✨ Project Overview

**CourseRecBot** is an intelligent Telegram chatbot designed to simplify the process of finding online course recommendations. Users can interact conversationally with the bot via Telegram, asking for courses on specific topics (e.g., "Python programming," "data science basics," "web development"), and the bot will instantly provide relevant suggestions from its curated knowledge base, complete with titles, institutions, and direct links.

This project showcases strong skills in conversational AI integration, webhook deployment, data processing, and API handling.

---

## 🚀 Key Features

* **Conversational Interface:** Interact with the bot naturally through Telegram.
* **Intelligent Topic Recognition:** Leverages Dialogflow's Natural Language Understanding (NLU) to interpret diverse user queries and extract course topics.
* **Course Recommendation:** Matches user requests to a comprehensive database of online courses.
* **Structured Responses:** Delivers course recommendations as clear, formatted messages (or rich cards) with clickable links, institutions, and titles.
* **Scalable Backend:** Built with Flask for robust webhook handling and efficient data processing.
* **Easy Deployment:** Designed for deployment on cloud platforms like Render.

---

## 🛠️ Technologies Used

* **Python:** Core programming language.
* **Flask:** Web framework for handling Dialogflow and Telegram webhooks.
* **Dialogflow ES:** For Natural Language Understanding (NLU) and intent management.
* **Telegram Bot API (via `python-telegram-bot` or direct API calls):** For Telegram integration.
* **Pandas:** For efficient data manipulation and querying of the course knowledge base (`.csv` file).
* **Render:** Cloud platform for continuous deployment and hosting.
* **Git:** Version control.

---

## 🏗️ Architecture & How It Works

The CourseRecBot operates on a webhook-driven architecture:

1.  **User Interaction:** A user sends a message to the bot on Telegram.
2.  **Telegram Webhook:** Telegram forwards the user's message to a specific webhook URL exposed by the deployed Flask application.
3.  **Dialogflow Integration:** The Flask application forwards the user's text to the Dialogflow agent for NLU processing. Dialogflow identifies the user's intent (e.g., `Recommend_Course`) and extracts relevant parameters (e.g., `course_topic`).
4.  **Fulfillment Webhook:** Dialogflow's fulfillment webhook (which is configured to point back to the Flask application's `/` endpoint) sends the processed intent and parameters back to the Flask app.
5.  **Course Recommendation Logic:** The Flask application (your Python backend) uses the extracted `course_topic` to query the `Coursera_courses.csv` database using Pandas to find the best course recommendations.
6.  **Response Generation:** The Flask app formats the recommendations and sends them back to Dialogflow.
7.  **Bot Response:** Dialogflow then sends the structured response back to Telegram, which delivers it to the user.
