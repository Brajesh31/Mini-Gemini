# Mini Gemini
 
Mini Gemini is a Streamlit web application that utilizes Google's Generative AI models for various tasks including chat search, PDF reading, image analysis, and database analysis.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshot](#screenshot)
- [Requirements](#requirements)

## Features

### Chat Search
- Allows users to interact with a Generative AI chatbot.
- Users can input their queries and receive responses from the chatbot.

### PDF Reader
- Enables users to upload PDF files.
- Generates content based on the input text and the uploaded PDF file using Generative AI.

### Image Reader
- Allows users to input prompts and upload images.
- Generates textual descriptions or analysis of the uploaded image using Generative AI.

### Database Reader
- Enables users to input prompts about databases.
- Users can get the analysis of the database.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/mini-gemini.git
cd mini-gemini
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:
    - Obtain a Google API key and set it as `GOOGLE_API_KEY` in a `.env` file.

4. Run the Streamlit app:

```bash
streamlit run app.py
```

## Usage

1. Select the desired functionality from the sidebar menu.
2. Follow the prompts and provide necessary inputs (e.g., text, files, database name).
3. Click on the corresponding button to trigger the action (e.g., "Answer", "Tell me about the PDF").
4. View the results displayed on the app.

## Requirements

- Python
- Streamlit
- API Key (Google)
- streamlit
- google-generativeai
- python-dotenv
- pdf2image

## Screenshot

### Chat_Search
![Chat_Search](https://github.com/Karanchrish/Mini-Gemini/assets/124337511/34e9ccc2-905b-433a-9e6e-4da9e3a1b26a)

### History_of_Chat_Search
![History_of_Chat_Search](https://github.com/Karanchrish/Mini-Gemini/assets/124337511/adc568ae-6cf2-487a-bc86-6047af6642b1)

### PDF_Reader
![PDF_Reader](https://github.com/Karanchrish/Mini-Gemini/assets/124337511/6407a31f-f6fc-46f3-8e9f-d3894789d8d7)

### Image_Reader_1
![Image_Reader_1](https://github.com/Karanchrish/Mini-Gemini/assets/124337511/2bb67e24-4293-4fdd-a7f7-1174984a2b36)

### Image_Reader_2
![Image_Reader_2](https://github.com/Karanchrish/Mini-Gemini/assets/124337511/1b411931-b170-4f5d-8d75-e807f6c5d3ad)

---

Feel free to contact me.
