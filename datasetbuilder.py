# from llama_index.llms import GradientModelAdapterLLM
# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
# )
# from langchain.chains import RetrievalQAWithSourcesChain
# from llama_hub.file.pymu_pdf.base import PyMuPDFReader
# from langchain_community.document_loaders import PyPDFLoader
# from langchain.schema import Document
# from pathlib import Path
# from llama_index.llms import GradientBaseModelLLM
# from llama_index.finetuning.gradient.base import GradientFinetuneEngine
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# import re
# from langchain_community.llms import GradientLLM
# import warnings
# from langchain_community.embeddings import HuggingFaceEmbeddings
# import jsonlines
import os
from datasets import Dataset
from datetime import datetime

import json

class DataSetBuilder():
    def __init__(self):
        self.dataset = {}

    def is_valid_json_lines(self, data):
        lines = data.strip().split('\n')
        for line in lines:
            try:
                json_obj = json.loads(line)
                if not isinstance(json_obj, dict):
                    print("JSON 객체가 dictionary가 아닙니다.")
                    return False  # JSON 객체가 dictionary가 아닌 경우
            except json.JSONDecodeError:
                print("JSON 객체가 dictionary가 아닙니다.")
                return False  # JSON 포맷이 아닌 경우
            
        print("정상적인 Dataset입니다.")            
        return True
    
    def build(self, data, name = ""):
        if self.is_valid_json_lines(data):
            lines = data.strip().split('\n')
            self.new_dataset = []
            for line in lines:
                data = json.loads(line)
                self.new_dataset.append(f'<s>### Instruction: \n{data["inputs"]} \n\n### Response: \n{data["response"]}</s>')
            
            self.dataset = Dataset.from_dict({"text": self.new_dataset})
            if name == "":
                name = "dataset_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            print("Dataset을 저장합니다. >> ", name)
            if not os.path.exists("datasets"):
                print("datasets 폴더가 없습니다. 생성합니다.")
                os.makedirs("datasets")
            self.dataset.save_to_disk(os.path.join('datasets', name))
            return self.dataset
        else:
            return None