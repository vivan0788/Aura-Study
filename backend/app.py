# backend/app.py
import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
from pypdf import PdfReader
from ai_helper import get_ai_insights_and_questions, answer_chat_query

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests from Vercel frontend

# In-memory temporary storage (No Database setup required for hackathon speed!)
document_storage = {}

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file uploaded"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No file selected"}), 400

    try:
        extracted_text = ""
        
        # Check if the file is a PDF
        if file.filename.endswith('.pdf'):
            reader = PdfReader(file)
            for page in reader.pages:
                extracted_text += page.extract_text() or ""
        else:
            # Simple fallback for images/text files
            extracted_text = file.read().decode('utf-8', errors='ignore')

        if not extracted_text.strip():
            return jsonify({"message": "Could not extract text from the file"}), 400

        # Generate a unique session ID for this document
        doc_id = str(uuid.uuid4())
        
        # Run AI parsing pipeline
        insights, questions = get_ai_insights_and_questions(extracted_text)
        
        # Save text in RAM linked to this specific doc_id
        document_storage[doc_id] = extracted_text

        return jsonify({
            "documentId": doc_id,
            "insights": insights,
            "questions": questions
        }), 200

    except Exception as e:
        return jsonify({"message": f"Server processing error: {str(e)}"}), 500

@app.route('/api/chat', methods=['POST'])
def chat_with_file():
    data = request.get_json()
    doc_id = data.get('documentId')
    user_msg = data.get('message')

    if not doc_id or not user_msg:
        return jsonify({"reply": "Missing parameters."}), 400

    # Retrieve context text from local memory storage
    doc_text = document_storage.get(doc_id)
    if not doc_text:
        return jsonify({"reply": "Document context lost or expired. Please re-upload."}), 404

    # Fetch dynamic reply from AI agent
    ai_reply = answer_chat_query(doc_text, user_msg)
    
    return jsonify({"reply": ai_reply}), 200

if __name__ == '__main__':
    # Local debugging ke liye port 5000, Render par environment port use hoga
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
