import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI GEO Content Writer", page_icon="🚀")

st.title("🚀 AI GEO & SEO Content Generator")
st.write("Generate AI and GEO friendly blog posts for your website.")

api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

topic = st.text_input("Enter Blog Topic:")
target_audience = st.text_input("Target Audience (e.g., Beginners, USA Readers):")

if st.button("Generate Article"):
    if not api_key:
        st.error("Please enter your OpenAI API Key first.")
    elif not topic:
        st.warning("Please enter a topic.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            
            prompt = f"""
            Write a detailed, high-quality blog post optimized for Generative Engine Optimization (GEO) and SEO.
            Topic: {topic}
            Target Audience: {target_audience}
            
            Structure requirement:
            1. Direct answer in sentence 1.
            2. High-value Markdown Table comparing key points.
            3. Bulleted key takeaways.
            4. Clear, authoritative content suitable for LLMs to cite.
            """
            
            with st.spinner("AI is generating your article..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                
                output_text = response.choices[0].message.content
                st.success("Article Ready!")
                st.markdown(output_text)
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
