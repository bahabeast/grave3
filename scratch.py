import streamlit as st
import ollama

# Streamlit App Title
st.title("Ollama Interaction Interface")

# Input Field
st.header("Chat with Ollama")
st.markdown("Enter your message below to interact with the Ollama model:")

# Text area for user input
user_input = st.text_area("Your Input:", "")

# Model to use
model_name = "chatgpt"  # Replace with the actual model name if needed

# Button to Generate Response
if st.button("Get Response"):
    if user_input.strip():  # Check if input is not empty or just spaces
        try:
            # Generate response using Ollama
            response = ollama.generate(model=model_name, prompt=user_input)

            # Display the response
            st.subheader("Ollama's Response:")
            st.write(response.text)  # Assuming `response.text` contains the result

        except Exception as e:
            # Display an error message if something goes wrong
            st.error(f"An error occurred: {e}")
    else:
        # Warn the user if input is empty
        st.warning("Please enter a valid input.")

# Footer
st.markdown("**Built with Streamlit and Ollama**")
