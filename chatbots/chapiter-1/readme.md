# 第一章：从零开始构建AI对话机器人 - BaseBot实战教程

## 1. 项目背景与目标
在AI快速发展的今天，掌握如何调用大语言模型API并构建自己的AI应用变得越来越重要。本章节将带领大家从零开始，构建一个基础但功能完整的AI对话机器人。

## 2. 环境准备

### 2.1 必要的依赖
```bash
pip install langchain langchain-community openai loguru
```

### 2.2 API准备
- 注册OpenRouter账号（https://openrouter.ai/）
- 获取免费的API密钥
- 了解可用的免费模型列表

## 3. 核心概念讲解

### 3.1 LangChain框架
LangChain是一个强大的AI应用开发框架，它提供了：
- 灵活的提示词管理
- 结构化输出解析
- 链式调用支持

### 3.2 结构化输出
我们的BaseBot使用了结构化输出，包含两个关键字段：
- result：最终答案
- think：思考过程

## 4. 代码实现详解

### 4.1 类的初始化
```python
def __init__(self, openai_api_key: str, ...):
```
这里使用了Python的类型注解，提高了代码的可读性和可维护性。参数说明：
- openai_api_key：API访问密钥
- openai_api_base：API端点地址
- model_name：使用的模型名称

### 4.2 核心配置设置
```python
def setup(self, openai_api_key: str, ...):
```
setup方法是整个类的核心，它完成了：
1. 定义输出格式（ResponseSchema）
2. 创建输出解析器
3. 设置提示词模板
4. 初始化LLM实例
5. 构建处理链

### 4.3 查询处理机制
```python
def single_query(self, question: str):
```
- 实现了无限重试机制
- 异常捕获确保程序稳定性
- 返回结构化的响应结果

## 5. 关键技术点深入

### 5.1 提示词工程
```python
template = """please strictly follow the format bellow:
{format_instructions}
Question: {query}"""
```
- 使用了格式化字符串
- 包含了格式说明和问题输入
- 确保AI输出符合预期格式

### 5.2 输出格式控制
```python
response_schemas = [
    ResponseSchema(name="result", type="string", ...),
    ResponseSchema(name="think", type="string", ...)
]
```
- 定义了严格的输出结构
- 便于后续处理和展示
- 提高了输出的可靠性

## 6. 实战练习

1. 修改输出格式，添加confidence（置信度）字段
2. 添加模型切换功能
3. 实现多轮对话功能

## 7. 小问题

1. 为什么需要捕获异常？有哪些因素可能会导致程序出现异常？

通过本章的学习，你将掌握构建AI对话机器人的基础知识，为后续开发更复杂的AI应用打下坚实的基础。但是目前，我们的机器人只能够给出截至训练日期的数据，怎样才能让机器人的回答具备有时效性呢？下一章，我们将探讨如何扩展BaseBot的功能，实现联网搜索的功能。