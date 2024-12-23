# -*- coding: utf-8 -*-
import re
from typing import Union, List

import requests

from videotrans.configure import config
from videotrans.translator._base import BaseTrans
from videotrans.util import tools


class AI302(BaseTrans):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.proxies = {"http": "", "https": ""}
        self.prompt = tools.get_prompt(ainame='ai302',is_srt=self.is_srt).replace('{lang}', self.target_language_name)
        self.model_name=config.params['ai302_model']
        self.prompt=self._replace_prompt()

    def _item_task(self, data: Union[List[str], str]) -> str:
        payload = {
            "model": config.params['ai302_model'],
            "messages": [
                {'role': 'system',
                 'content': "You are a professional, helpful translation engine that translates only the content in <source> and returns only the translation results" if config.defaulelang != 'zh' else '您是一个有帮助的翻译引擎，只翻译<source>中的内容，并只返回翻译结果'},
                {'role': 'user',
                 'content': self.prompt.replace('[TEXT]', "\n".join([i.strip() for i in data]) if isinstance(data,list) else data)},
            ]
        }
        response = requests.post('https://api.302.ai/v1/chat/completions', headers={
                'Accept': 'application/json',
                'Authorization': f'Bearer {config.params["ai302_key"]}',
                'User-Agent': 'pyvideotrans',
                'Content-Type': 'application/json'
            }, json=payload, verify=False, proxies=self.proxies)
        config.logger.info(f'[302.ai]响应:{response.text=}')
        if response.status_code != 200:
            raise Exception(f'status_code={response.status_code} {response.reason}')
        res = response.json()
        if res['choices']:
            result = res['choices'][0]['message']['content']
            return re.sub(r'\n{2,}', "\n", result)
        raise Exception(f"No choices:{res=}")
