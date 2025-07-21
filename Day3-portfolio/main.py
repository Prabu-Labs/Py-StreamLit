import streamlit as st

st.set_page_config(page_title="Prabu N - Portfolio", page_icon="💼", layout="centered")

# Layout with columns for image and name/title
col1, col2 = st.columns([1, 3])
with col1:
    st.image("FB_IMG_1753091428619.jpg", width=130)
with col2:
    st.title("Prabu N")
    st.subheader("Technical Lead | Cloud Architecture | Atlassian Expert")
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/prabu-n/)")

st.markdown("---")  # Section divider

# Summary
st.header("Summary")
st.write("""
Experienced Technical Lead with expertise in cloud architecture, Atlassian tools, and full-stack development. Proven track record in leading technical teams, implementing cloud migrations, and managing large-scale Jira environments.
""")

st.markdown("---")

# Skills
st.header("Skills")
st.write("""
- Technical Leadership & Team Management  
- Cloud Architecture & Migration  
- Full Stack Development (React.js, Node.js, .NET, Java)  
- Atlassian Tools (Jira, Forge, Rovo, Analytics)  
- DevOps & Automation  
- Python, VBA  
- Generative AI  
""")

st.markdown("---")

# Experience
st.header("Experience")
st.write("""
**Technical Lead**  
Wipro | Present  
- Leading cloud migration initiatives and architectural design  
- Managing Jira Cloud governance for 15,000+ users  
- Implementing Atlassian tool integrations and automation  
- Developing Python automation scripts for organizational housekeeping  
- Architecting solutions for Jira integrations  
- Expertise in Forge, Rovo, and Analytics  
""")

st.markdown("---")

# Education
st.header("Education")
st.write("""
M.C.A, Computer Science  
MK University  
""")

st.markdown("---")

# Certifications
st.header("Certifications")
st.write("""
- AWS Certified Cloud Practitioner  
""")

st.markdown("---")

# Contact
st.header("Contact")
st.write("Email: prabu.n.2023@gmail.com")
