import streamlit as st

# Title and Header
st.title("👋 Hello World Streamlit App")
st.header("Welcome to Your First Streamlit App!")

# Display Basic Text
st.write("This is a simple Streamlit app that demonstrates how to display text, markdown, and basic formatting.")

# Markdown Example
st.markdown("""
## Markdown Formatting

- **Bold text**: `**text**` → **text**
- *Italic text*: `*text*` → *text*
- [Links](https://streamlit.io): `[Link Text](url)`
- Inline `code`: `` `code` ``
- Numbered lists:
    1. Item one
    2. Item two
- Blockquotes:
    > This is a blockquote
- Horizontal line: `---`
---
""")

# Cheatsheet / Quick Tutorial
st.subheader("Streamlit Cheatsheet")
st.markdown("""
```python
# Display text
""")
st.write("Hello, Streamlit!")

# Display markdown
st.markdown("**Bold** and _italic_ text")

# Display code
st.code("print('Hello, World!')", language='python')

# Display data as a table
import pandas as pd
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.table(df)
