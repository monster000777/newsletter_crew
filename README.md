# AI Newsletter Crew

基于 [CrewAI](https://crewai.com/) 的 AI 新闻简报生成团队。

## 项目概述

三个 AI Agent 组成团队分工协作：
- **研究员 (Researcher)** - 搜索最新 AI 新闻
- **作家 (Writer)** - 撰写新闻摘要
- **审核员 (Reviewer)** - 审核内容准确性

## 项目结构

```
newsletter_crew/
├── main.py                           # CLI 入口
├── streamlit_app.py                  # 可视化界面
├── src/newsletter_crew/
│   ├── config.py                     # 配置管理（统一）
│   ├── agents/__init__.py            # Agent 定义
│   ├── tasks/__init__.py             # Task 定义
│   └── crew.py                       # Crew 配置
├── .env                              # 环境变量
├── .env.example                      # 环境变量模板
└── uv.lock                           # 依赖锁定
```

## 快速开始

### 1. 安装依赖

```bash
cd newsletter_crew
uv sync
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env`，填入你的配置：

```env
OPENAI_API_KEY=sk-your-key
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o
SERPER_API_KEY=your-serper-api-key
```

### 3. 运行

**命令行模式：**
```bash
uv run python main.py
```

**可视化界面模式：**
```bash
uv run streamlit run streamlit_app.py
```

## 可视化界面

运行可视化界面：

```bash
uv run streamlit run streamlit_app.py
```

浏览器会自动打开 http://localhost:8501

界面功能：
- 输入新闻主题
- 一键生成简报
- 实时进度显示
- 下载 Markdown 文件

## Agent 工作流程

| 阶段 | Agent | 任务 |
|------|-------|------|
| 1 | 研究员 | 搜索当日最重要的 5 条 AI 新闻 |
| 2 | 作家 | 撰写 300 字中文摘要 |
| 3 | 审核员 | 审核内容准确性和质量 |

## 环境要求

- Python >= 3.10, < 3.14
- CrewAI >= 1.0.0
- crewai-tools
- streamlit >= 1.57.0
- python-dotenv >= 1.0.0

## License

MIT
