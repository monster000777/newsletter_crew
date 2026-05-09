import streamlit as st

from src.newsletter_crew.runner import normalize_topic, run_newsletter


DEFAULT_TOPIC = "AI"

st.set_page_config(
    page_title="AI Newsletter Crew",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Newsletter Crew")
st.markdown("---")

topic = st.text_input("📰 输入新闻主题", value=DEFAULT_TOPIC, placeholder="例如：AI、人工智能、机器学习...")

if "result" not in st.session_state:
    st.session_state.result = None

if "error" not in st.session_state:
    st.session_state.error = None

if st.button("🚀 生成简报", type="primary", use_container_width=True):
    if not topic.strip():
        st.session_state.result = None
        st.session_state.error = None
        st.error("请输入新闻主题")
    else:
        try:
            st.session_state.result = None
            st.session_state.error = None
            normalized_topic = normalize_topic(topic)

            progress_bar = st.progress(0, text="准备中...")

            # Stage 1: Researcher
            progress_bar.progress(20, text="🔍 研究员搜索新闻...")

            # Stage 2: Writing
            progress_bar.progress(50, text="✍️ 作家撰写摘要...")

            # Stage 3: Review
            progress_bar.progress(75, text="✅ 审核员审核中...")

            result = run_newsletter(normalized_topic)

            progress_bar.progress(100, text="完成！")

            st.session_state.result = str(result)
            st.success("🎉 简报生成完成！")

        except Exception as e:
            st.session_state.error = str(e)

if st.session_state.error:
    st.error(f"错误：{st.session_state.error}")

if st.session_state.result:
    st.markdown("---")
    st.markdown("### 📋 生成的简报")
    st.markdown(st.session_state.result)

    st.download_button(
        "📥 下载 Markdown",
        st.session_state.result,
        file_name="newsletter_output.md",
        mime="text/markdown",
        use_container_width=True
    )
    st.code(st.session_state.result, language=None)
    st.info("复制上方代码块中的内容")

st.markdown("---")
st.caption("💡 由 AI Newsletter Crew 生成 | 基于 CrewAI")
