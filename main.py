
import streamlit as st
import cohere
from dotenv import load_dotenv
import os

load_dotenv()

co = cohere.Client(os.getenv('COHERE_API_KEY'))

# Initialization
if 'output' not in st.session_state:
    st.session_state['output'] = 'Output:'


def supportbot(input):
    if len(input) == 0:
        return None
    response = co.generate(
        model='xlarge',
        prompt='You are a party planner bot.You help others figure out planning for their party.You will recommend fun party ideas according to the details entered.Try to give upbeat answers.\n\nPost:I am a girly girl.I want a fun party.\nAnswer:You should organise a party centered around the barbie movie released in 2023.You can buy multiple bento cakes and serve the guests  \n--\nPost:I am a big fan of comics.I want to hold a birthday.\nAnswer:Maybe you can cosplay one of your favourite characters and ask others to dress up like their favourite comic character and play dumbcharades. \n--\nPost:What should I do for my sister who is moving abroad after her graduation?\nAnswer:Maybe a hold a small party with closed folks where you can cook her favorite family dish and decorate with you did it posters. \n--\nPost: {}\nAnswer:'.format(
            input),
        max_tokens=90,
        temperature=0.5,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')

    st.session_state['output'] = response.generations[0].text
    st.balloons()


st.title('PartyMate,Inc')
st.subheader('Your favorite party planner!')
st.write('''This is a simple app that gives you recommendations or tips for the kind of party you want to plan''')

input = st.text_area('Tell us what your looking for', height=100)
st.button('Help me plan!', on_click=supportbot(input))
st.write(st.session_state.output)