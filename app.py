import streamlit as st
from recommender import recommend, match_condition

st.title("💊 Drug Recommendation Chatbot")
st.caption("Tell me your condition and I'll suggest the best-rated medications from real patient reviews.")
# the chat box at the bottom of the page
user_input = st.chat_input("e.g. I have a headache")
# this block runs only when the user types something and hits enter
if user_input:
    # show the user's message as a chat bubble
    st.chat_message("user").write(user_input)
    # figure out which condition they mean
    matches = match_condition(user_input)
    # build the assistant's reply
    with st.chat_message("assistant"):
        if not matches:
            st.write("Sorry, I couldn't match that to a condition I know. Try different wording.")
        else:
            condition = matches[0]                       # best match
            st.write(f"Top medications for **{condition}**:")
            st.dataframe(recommend(condition, top_n=5))  # the ranked table
            if len(matches) > 1:
                st.caption("Did you mean: " + ", ".join(matches[1:]) + "?")
            st.warning("⚠️ Educational project only — NOT medical advice.")
