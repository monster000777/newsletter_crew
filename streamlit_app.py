import streamlit as st
from src.newsletter_crew.crew import create_crew

st.set_page_config(
    page_title="AI Newsletter Crew",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Newsletter Crew")
st.markdown("---")

topic = st.text_input("📰 输入新闻主题", value="AI", placeholder="例如：AI、人工智能、机器学习...")

if "result" not in st.session_state:
    st.session_state.result = None

if "error" not in st.session_state:
    st.session_state.error = None

if st.button("🚀 生成简报", type="primary", use_container_width=True):
    if not topic.strip():
        st.error("请输入新闻主题")
    else:
        try:
            st.session_state.result = None
            st.session_state.error = None

            progress_bar = st.progress(0, text="初始化...")

            progress_bar.progress(10, text="🔍 研究员正在搜索新闻...")
            progress_bar.progress(40, text="✍️ 作家正在撰写...")

            crew = create_crew()
            result = crew.kickoff(inputs={"topic": topic})

            progress_bar.progress(80, text="✅ 审核员正在审核...")

            st.session_state.result = str(result)
            progress_bar.progress(100, text="完成！")

            st.success("🎉 简报生成完成！")

        except Exception as e:
            st.session_state.error = str(e)
            st.error(f"生成失败：{e}")

if st.session_state.error:
    st.error(f"错误：{st.session_state.error}")

if st.session_state.result:
    st.markdown("---")
    st.markdown("### 📋 生成的简报")
    st.markdown(st.session_state.result)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "📥 下载 Markdown",
            st.session_state.result,
            file_name="newsletter_output.md",
            mime="text/markdown",
            use_container_width=True
        )
    with col2:
        st.code(st.session_state.result, language=None)
        st.info("复制上方代码块中的内容")

st.markdown("---")
st.caption("💡 由 AI Newsletter Crew 生成 | 基于 CrewAI")
