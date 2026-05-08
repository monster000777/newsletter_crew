# AI Newsletter Crew

基于 [CrewAI](https://crewai.com/) 的 AI 新闻简报生成团队。

## 项目概述

三个 AI Agent 组成团队分工协作：
- **研究员 (Researcher)** - 搜索最新 AI 新闻（需要配置搜索工具）
- **作家 (Writer)** - 撰写新闻摘要
- **审核员 (Reviewer)** - 审核内容准确性

## 项目结构

```
newsletter_crew/
├── main.py                           # 入口文件
├── src/newsletter_crew/
│   ├── __init__.py
│   ├── agents/__init__.py            # Agent 定义
│   ├── tasks/__init__.py             # Task 定义
│   └── crew.py                       # Crew 配置
├── .env                              # 环境变量（不提交）
├── .env.example                      # 环境变量模板
├── pyproject.toml                    # 项目配置
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
OPENAI_API_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o

# 可选：搜索工具（获取实时新闻）
SERPER_API_KEY=your-serper-api-key
```

### 3. 运行

```bash
uv run python main.py
```

结果会保存到 `newsletter_output.md`

## 配置搜索工具

要获取实时新闻，需要配置搜索 API：

### Serper (推荐)
1. 注册 [Serper.dev](https://serper.dev)
2. 获取 API Key
3. 在 `.env` 中添加 `SERPER_API_KEY=your-key`

## 修改主题

编辑 `main.py` 中的 `topic` 参数：

```python
result = crew.kickoff(inputs={"topic": "AI"})  # 改成你想要的新闻主题
```

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
- python-dotenv >= 1.0.0

## License

MIT
