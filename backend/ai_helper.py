# backend/ai_helper.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Client object nahi banayenge, direct legacy config key set karenge
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_insights_and_questions(text):
    """
    Document ke text se key insights aur mock questions generate karta hai.
    """
    try:
        prompt = f"""
        Analyze the following text from a document and provide two things in strict structured format:
        1. A list of 4-5 important key points/insights.
        2. A list of 3 relevant practice questions based on the content.

        Text Content:
        {text[:4000]}
        """

        # Purani stable initialization direct syntax call
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert AI academic assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        raw_output = response['choices'][0]['message']['content']
        lines = [line.strip() for line in raw_output.split('\n') if line.strip()]
        
        insights = [line for line in lines if line.startswith(('-', '*', '1.', '2.', '3.', '4.', '5.'))][:5]
        questions = [line for line in lines if '?' in line][:3]
        
        if not insights:
            insights = ["Document parsed successfully.", "Main summary concepts extracted."]
        if not questions:
            questions = ["What is the main theme of this document?", "Can you summarize the core argument?"]

        return insights, questions
    except Exception as e:
        print(f"[AI Helper Error]: {e}")
        return [f"Error generating insights: {str(e)}"], ["Error generating questions."]

def answer_chat_query(doc_text, user_message):
    """
    Document ke text ke context mein user ke question ka answer deta hai.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a helpful AI agent. Answer the user's questions strictly based on this document text:\n\n{doc_text[:3000]}"},
                {"role": "user", "content": user_message}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Sorry, I couldn't process that query. (Error: {str(e)})"
