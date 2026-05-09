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
├── tests/
│   └── test_runner.py                # 基础单元测试
├── src/newsletter_crew/
│   ├── config.py                    # 配置管理
│   ├── agents.py                    # Agent 定义
│   ├── tasks.py                     # Task 定义
│   ├── crew.py                      # Crew 装配
│   ├── runner.py                    # 共享运行逻辑
│   └── __init__.py                  # 包入口
├── .env                             # 环境变量
├── .env.example                     # 环境变量模板
├── pyproject.toml                   # 项目配置
├── uv.lock                          # 依赖锁定
└── LICENSE                          # MIT 许可
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

说明：
- `OPENAI_BASE_URL` 用于 OpenAI 兼容接口地址
- `SERPER_API_KEY` 可选；未配置时研究任务会降级为无实时搜索模式

### 3. 运行

**命令行模式：**
```bash
uv run python main.py
uv run python main.py AI
uv run python main.py 机器人
```

默认主题为 `AI`。

**可视化界面模式：**
```bash
uv run streamlit run streamlit_app.py
# 浏览器打开 http://localhost:8501
```

界面功能：输入主题、生成简报、下载 Markdown

### 4. 运行测试

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
```

### 5. 输出文件

- CLI 运行后会生成 `newsletter_output.md`
- 该文件已在 `.gitignore` 中忽略

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
