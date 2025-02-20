#! python3
# -*- encoding: utf-8 -*-
"""
@File    :   basebot.py
@Time    :   2025/02/20 23:42:14
@Author  :   lidashan
@Version :   1.0
"""

# 导入要用到的库
import json
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
from loguru import logger

import warnings

warnings.filterwarnings("ignore")


class BaseBot:
    def __init__(
        self,
        openai_api_key: str,
        openai_api_base: str = "https://openrouter.ai/api/v1",
        model_name: str = "deepseek/deepseek-r1-distill-llama-70b:free",
    ):
        """初始化BaseBot

        Args:
            openai_api_key (str): 在openrouter.ai注册后免费获取。
            openai_api_base (_type_, optional): 模型来源. Defaults to "https://openrouter.ai/api/v1".
            model_name (str, optional): 模型名字，带`free`后缀的可免费使用. Defaults to "deepseek/deepseek-r1-distill-llama-70b:free".
        """
        self.setup(openai_api_key, openai_api_base, model_name)

    def setup(self, openai_api_key: str, openai_api_base: str, model_name: str):
        response_schemas = [
            ResponseSchema(
                name="result",
                type="string",
                description="the final answer for the questin",
            ),
            ResponseSchema(
                name="think", type="string", description="thinking procedure"
            ),
        ]
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        template = """please strictly follow the format bellow:
        {format_instructions}
        Question: {query}"""
        prompt = PromptTemplate(
            template=template,
            input_variables=["query"],
            partial_variables={"format_instructions": format_instructions},
        )
        llm = ChatOpenAI(
            openai_api_key=openai_api_key,
            openai_api_base=openai_api_base,
            model_name=model_name,
            temperature=0,
        )
        self.chain = prompt | llm | output_parser

    def single_query(self, question: str):
        while True:
            try:
                response = self.chain.invoke({"query": question})
                return response
            except:
                continue

    def run(self, question: str):
        response = self.single_query(question)
        return response


if __name__ == "__main__":
    bot = BaseBot(
        openai_api_key="sk-or-v1-xxxxxxxx",
        openai_api_base="https://openrouter.ai/api/v1",
        model_name="deepseek/deepseek-r1-distill-llama-70b:free",
    )
    logger.info(json.dumps(bot.run("what's meaning of life ?"), indent=2))
    logger.info(json.dumps(bot.run("what date is today ?"), indent=2))
