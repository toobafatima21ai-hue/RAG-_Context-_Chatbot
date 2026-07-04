import os
import streamlit as st

from modules.chatbot import chatbot_response
from modules.vectorstore import build_vector_db
from modules.export_utils import export_txt, export_pdf

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Context-Aware RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #E3F2FD,
            #F5F5F5
        );
    }

    .big-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #1565C0;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------
# HEADER
# --------------------------------

st.markdown(
    """
    <div class='big-title'>
        🤖 Context-Aware RAG Chatbot
    </div>

    <div class='subtitle'>
        LangChain • FAISS • Ollama • Mistral
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------
# SIDEBAR
# --------------------------------
with st.sidebar:

    st.header("📚 Knowledge Base")

    st.info(
        """
Upload your own PDF document.

Examples:
- Research Papers
- Lecture Notes
- Company Manuals
- Books
- Documentation

The chatbot will answer questions using the uploaded document.
"""
    )

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if "processed_file" not in st.session_state:
        st.session_state.processed_file = None

    if uploaded_file is not None:

        if st.session_state.processed_file != uploaded_file.name:

            os.makedirs(
                "data",
                exist_ok=True
            )

            pdf_path = os.path.join(
                "data",
                uploaded_file.name
            )

            with open(pdf_path, "wb") as f:
                f.write(
                    uploaded_file.getbuffer()
                )

            with st.spinner(
                "Building knowledge base..."
            ):
                build_vector_db(pdf_path)

            st.session_state.processed_file = uploaded_file.name

            st.success(
                "✅ Knowledge Base Updated Successfully"
            )

    st.divider()

    st.subheader("⚙ System Status")

    st.success("LLM: Mistral (Ollama)")
    st.success("Retriever: FAISS")
    st.success("Status: Online")
# --------------------------------
# CHAT HISTORY
# --------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.write(
            message["content"]
        )

# --------------------------------
# CHAT INPUT
# --------------------------------

user_input = st.chat_input(
    "Ask anything about your document..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    try:

        response, context, sources = chatbot_response(
            user_input
        )

        with st.chat_message("assistant"):

            st.write(response)

            with st.expander(
                "📚 Retrieved Context"
            ):
                st.text(context)

            with st.expander(
                "📄 Sources"
            ):
                for source in sources:
                    st.write(source)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

# --------------------------------
# EXPORT SECTION
# --------------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "⬇ Export TXT"
    ):

        path = export_txt(
            st.session_state.messages
        )

        st.success(
            f"Saved: {path}"
        )

with col2:

    if st.button(
        "⬇ Export PDF"
    ):

        path = export_pdf(
            st.session_state.messages
        )

        st.success(
            f"Saved: {path}"
        )

# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.caption(
    "Built with LangChain • FAISS • Ollama • Streamlit • Mistral"
)