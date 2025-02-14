import streamlit as st

def show_policy():
    st.title("🔒 Privacy Policy")
    st.write("**Effective Date:** [14/02/2025]")
    st.markdown("---")

    st.header("1. Introduction")
    st.write("Welcome to **Local-AI-Interface**. This chatbot runs **entirely on your local machine** and does not collect, store, or share any user data. Your privacy is our priority.")
    
    st.header("2. Data Collection & Usage")
    st.markdown("""
    - **No Data Collection:** We do **not** collect, store, or transmit any personal data, chat history, or interactions.
    - **Local Execution:** All AI processing happens **on your device**, using local models via **Ollama**.
    - **No Cloud Dependencies:** No external API calls or cloud-based services are involved.
    """)
    
    st.header("3. Security")
    st.write("Since this chatbot runs **completely offline**, your conversations remain **private and secure**. You are responsible for securing your device.")
    
    st.header("4. Third-Party Services")
    st.write("The application may use **open-source AI models** (DeepSeek, LLaMA, Mistral) hosted locally. Any models downloaded from third-party sources (e.g., Ollama) are subject to their respective privacy policies.")
    
    st.header("5. User Control & Data Deletion")
    st.markdown("""
    - **No stored data**: All interactions are cleared when you close the app.
    - **Conversation history (if enabled)** is stored locally and can be deleted at any time.
    """)
    
    st.header("6. Changes to This Policy")
    st.write("We may update this Privacy Policy. Any updates will be available in the GitHub repository.")
    
    st.header("7. Contact Information")
    st.write("For any questions, contact us at:")
    st.write("🔗 **GitHub:** [---]")

if __name__ == "__main__":
    show_policy()
