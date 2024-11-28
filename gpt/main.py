import streamlit as st
import time
import backend

st.markdown("""
    <style>
    .stApp {
   
    background-color: #f4f4f9;
 }
    </style>
    """, unsafe_allow_html=True)

# Add this line to create a header
st.header("Welcome to YURI - Your AI Assistant")

st.title("YURI")



def response_generator(prompt):
    try:
        response = backend.GenerateResponse(prompt)
        lines = response.split('\n')
        for line in lines:
            words = line.split()
            for word in words:
                yield word + " "
                time.sleep(0.05)
            yield "\n"  # Preserve line breaks
    except Exception as e:
        yield f"An error occurred: {str(e)}"
        
      



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("ask questions"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
