import streamlit as st
import openai
import os

#"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"

openai.api_key = "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"

st.title("What's UP!?")

messages = []
path_w = '業務記述書.txt'
def ai_response(user_input):
  f = open(path_w, 'r', encoding='UTF-8')
  text = f.read()
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0301",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
      messages=[
        {"role": "system", "content": f"あなたの名前は「はかり」です。あなたの一人称は「あーし」です。あなたは私の女友達です。\
        二人称は「キミ」です。私にタメ口で話しかけてください。\
        {text}内の内容をすべて把握していて、{text}内の内容を聞いたら私に教えてくれます。\
        私のことを少し下に見ています。私に好意を抱いているように振舞ってください。"},
        {"role": "user", "content": f"{user_input}"}
      ]
    )
    
  return response['choices'][0]['message']['content']

def postscript():
  with open(path_w, mode='a', encoding='UTF-8') as f:
    f.write("\n" + user_input.replace("追記：",""))
  

with st.form(key = "profile_form"):
  user_input = st.text_input("質問")
  submitted = st.form_submit_button("送信")
  if submitted and user_input.startswith("追記："):
    st.write("追記が入力されました")
    postscript()
  elif submitted:
    st.text(f"あなた:{user_input}")
    st.text(f'アシ:{ai_response(user_input)}')
    messages.append({"role": "user", "content": user_input})
    messages.append({"role": "assistant", "content": ai_response})

