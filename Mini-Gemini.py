import streamlit as st
import os
import io
import base64
import sqlite3
from PIL import Image 
import pdf2image
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model_gemini_pro=genai.GenerativeModel("gemini-pro") 
model_gemini_pro_vision = genai.GenerativeModel('gemini-pro-vision')

#Chat Search
def get_gemini_chat(input):
    response=chat.send_message(input, stream=True)
    return response
chat = model_gemini_pro.start_chat(history=[])


#Pdf Reader
def get_gemini_pdf(input, pdf):
    try:
        if input != "":
            response = model_gemini_pro_vision.generate_content([input, pdf[0]])
        else:
            response = model_gemini_pro_vision.generate_content(pdf[0])
        if response:
            return response.text
    except Exception as e:
        return f"Error: {str(e)}"
 
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        # Selecting the first page image
        page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

#Image Reader
def get_gemini_image(input, image):
    try:
        if input != "":
            response = model_gemini_pro_vision.generate_content([input, image])
        else:
            response = model_gemini_pro_vision.generate_content(image)
        if response:
            return response.text
    except Exception as e:
        return f"Error: {str(e)}"

#Database Reader
def get_gemini_db(input,prompt):
    response=model_gemini_pro.generate_content([prompt[0],input])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has Some Columns. You have to Identify it and Answer the Question.
    \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]




#Streamlit APP
st.set_page_config(page_title="Mini Gemini")
st.header("Mini Gemini")

selection = st.sidebar.selectbox("Select what you Needed", ["Chat Search", "PDF Reader", "Image Reader", "Database Reader"])


# Chat Search
if selection == "Chat Search":
    st.subheader("Chat Search")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input=st.text_input("Input: ", key="input")
    submit=st.button("Answer")

    if submit and input:
        response=get_gemini_chat(input)

        st.session_state['chat_history'].append(("You", input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))


    if st.sidebar.checkbox("Show Chat History"):
        st.sidebar.subheader("Chat History")
        for role, text in st.session_state['chat_history']:
            st.sidebar.write(f"{role}: {text}")

#PDF Reader
if selection == "PDF Reader":
    st.subheader("PDF Reader")

    input = st.text_area("Input: ", key="input")
    uploaded_file = st.file_uploader("Upload your PDF...", type=["pdf"])

    if uploaded_file is not None:
        st.write("PDF Uploaded Successfully")
        pdf = input_pdf_setup(uploaded_file)

    submit = st.button("Tell me about the PDF")
    if submit:
        response = get_gemini_pdf(input, pdf)
        st.write(response)


#Image Reader
if selection == "Image Reader":
    st.subheader("Image Reader")
    input=st.text_input("Input Prompt: ",key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit=st.button("Tell me about the image")
    if submit:
        response=get_gemini_image(input,image)
        st.write(response)

#Database Reader
if selection == "Database Reader":
    st.subheader("Database Reader")
   database_name = st.text_input("Database Name: ", key="database")
    input=st.text_input("Input: ",key="input")

    submit=st.button("Answer me")

    if submit:
        response=get_gemini_db(input,prompt)
        if database_name:
            data = read_sql_query(response, f"{database_name}.db")
            st.header("The Response is")
           for row in data:
                st.subheader(row)
        else:
            st.error("Please enter a database name.")
