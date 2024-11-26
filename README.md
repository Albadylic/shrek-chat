# **Shrek Chatbot API**

## **Overview**

The **Shrek Chatbot API** is a FastAPI-powered application that utilises Retrieval-Augmented Generation (RAG) to answer questions about _Shrek_. It leverages the LlamaIndex framework and OpenAI's GPT model to create an intelligent agent capable of parsing and responding to queries based on provided text data.

This project features:

- An asynchronous back-end API built with FastAPI.
- Integration with OpenAI GPT models via the LlamaIndex framework.
- A robust query engine trained on a markdown file about _Shrek_.
- Support for cross-origin requests, making it easy to integrate with a React front-end.

---

## **Features**

- Query the chatbot with specific questions about _Shrek_.
- Powered by OpenAI's GPT-4 model for natural language understanding.
- Fully asynchronous to handle multiple requests efficiently.
- CORS-enabled, allowing communication from different front-end origins.

---

## **Requirements**

- Python 3.8+
- Node.js (optional, if integrating with a front-end)
- OpenAI API key

---

## **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/shrek-chatbot.git
cd shrek-chatbot
```

### **2. Set Up the Python Back-end**

#### **a. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

#### **b. Install Dependencies**

```bash
pip install -r requirements.txt
```

#### **c. Add the OpenAI API Key**

- Create a `.env` file in the `backend/` directory:
  ```bash
  cd backend
  touch .env
  ```
- Add the following line to the `.env` file:
  ```bash
  OPENAI_API_KEY=your_openai_api_key_here
  ```

#### **d. Verify Resources**

Ensure that the `resources/Shrek.txt` file exists and contains the data you want to use for training the query engine.

---

## **Running the Application**

1. Start the back-end server:

   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser or a tool like Postman and navigate to the API documentation:

   ```
   http://127.0.0.1:8000/docs
   ```

3. Use the `/ask` endpoint to submit questions about _Shrek_. For example:
   - **Endpoint**: `POST /ask`
   - **Body**:
     ```json
     {
       "question": "Describe Shrek's personality."
     }
     ```

---

## **Project Structure**

```
shrek-chatbot/
├── backend/               # Python back-end
│   ├── main.py            # FastAPI application
│   ├── requirements.txt   # Python dependencies
│   ├── resources/         # Text data for training
│   └── .env               # API key configuration
├── frontend/              # (Optional) React front-end
│   ├── src/               # React source code
│   └── ...
├── README.md              # Project documentation
└── .gitignore             # Ignored files for Git
```

---

## **Using the API**

### **Endpoints**

1. **`GET /`**

   - Test endpoint to check if the API is running.
   - **Response**:
     ```json
     { "message": "Hello World" }
     ```

2. **`POST /ask`**
   - Accepts a question and returns an intelligent response.
   - **Request Body**:
     ```json
     {
       "question": "What does Shrek look like?"
     }
     ```
   - **Response**:
     ```json
     {
       "response": "Shrek is a large green ogre with a gruff yet kind personality."
     }
     ```

---

## **Development Notes**

### **Debugging Common Issues**

- **CORS Errors**:
  Ensure the front-end and back-end are configured correctly to handle cross-origin requests. Refer to the `CORSMiddleware` section in `main.py`.

- **Missing API Key**:
  Double-check your `.env` file for the `OPENAI_API_KEY`.

- **Async Errors**:
  If you encounter `RuntimeError` regarding nested event loops, ensure `nest_asyncio` is applied at the top of your script.

---

## **Future Enhancements**

- Add a front-end for a user-friendly interface.
- Extend support for other documents besides _Shrek_.
- Deploy the app to cloud platforms like AWS or Heroku.

---

## **Contributing**

Contributions are welcome! Feel free to open issues or submit pull requests. Please adhere to the project's code of conduct.

---

## **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

Let me know if you need further adjustments to the README!
