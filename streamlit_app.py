import streamlit as st
import toml
from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="meta/llama-3.1-405b-instruct",
  messages=[{"role":"user","content":"today weather in salt lake, kolkata"}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    st.write(chunk.choices[0].delta.content, end="")
