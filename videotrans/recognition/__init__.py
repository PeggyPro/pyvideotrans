import logging

import torch

from videotrans.configure import config
# 判断各个语音识别模式是否支持所选语言
# 支持返回True，不支持返回错误文字字符串
from videotrans.winform import zh_recogn as zh_recogn_win, recognapi as recognapi_win, \
    openairecognapi as openairecognapi_win, doubao as doubao_win
from .all import recogn as all_recogn
from .avg import recogn as avg_recogn
from .doubao import recogn as doubao_recogn
from .google import recogn as google_recogn
from .openai import recogn as openai_recogn
from .openairecognapi import recogn as openairecogn_api
from .recognapi import recogn as recogn_api
from .zh import recogn as zh_recogn

logging.basicConfig()
logging.getLogger("faster_whisper").setLevel(logging.DEBUG)

# 数字代表界面中的现实顺序
FASTER_WHISPER = 0
OPENAI_WHISPER = 1
GOOGLE_SPEECH = 2
ZH_RECOGN = 3
DOUBAO_API = 4
CUSTOM_API = 5
OPENAI_API = 6

RECOGN_NAME_LIST = [
    config.uilanglist['faster model'],
    config.uilanglist['openai model'],
    "Google识别api" if config.defaulelang == 'zh' else "Google Speech API",
    "zh_recogn中文识别" if config.defaulelang == 'zh' else "zh_recogn only Chinese",
    "豆包模型识别" if config.defaulelang == 'zh' else "Doubao",
    "自定义识别API" if config.defaulelang == 'zh' else "Custom Recognition API",
    "OpenAI识别API" if config.defaulelang == 'zh' else "OpenAI Speech API"
]


def is_allow_lang(langcode: str = None, model_type: int = None):
    if model_type == ZH_RECOGN and langcode[:2] != 'zh':
        return 'zh_recogn 仅支持中文语音识别' if config.defaulelang == 'zh' else 'zh_recogn Supports Chinese speech recognition only'

    if model_type == DOUBAO_API and langcode[:2] not in ["zh", "en", "ja", "ko", "es", "fr", "ru"]:
        return '豆包语音识别仅支持中英日韩法俄西班牙语言，其他不支持'

    return True


# 自定义识别、openai-api识别、zh_recogn识别是否填写了相关信息和sk等
# 正确返回True，失败返回False，并弹窗
def is_input_api(model_type: int = None):
    if model_type == ZH_RECOGN and not config.params['zh_recogn_api']:
        zh_recogn_win.open()
        return False

    if model_type == CUSTOM_API and not config.params['recognapi_url']:
        recognapi_win.open()
        return False

    if model_type == OPENAI_API and not config.params['openairecognapi_key']:
        openairecognapi_win.open()
        return False
    if model_type == DOUBAO_API and not config.params['doubao_appid']:
        doubao_win.open()
        return False
    return True


# 统一入口
def run(*,
        type="all",
        detect_language=None,
        audio_file=None,
        cache_folder=None,
        model_name=None,
        set_p=True,
        inst=None,
        uuid=None,
        model_type: int = 0,
        is_cuda=None
        ):
    if config.exit_soft or (config.current_status != 'ing' and config.box_recogn != 'ing'):
        return False
    if model_name.startswith('distil-'):
        model_name = model_name.replace('-whisper', '')
    if model_type == OPENAI_WHISPER:
        rs = openai_recogn(
            detect_language=detect_language,
            audio_file=audio_file,
            cache_folder=cache_folder,
            model_name=model_name,
            set_p=set_p,
            uuid=uuid,
            inst=inst,
            is_cuda=is_cuda)
    elif model_type == GOOGLE_SPEECH:
        rs = google_recogn(
            detect_language=detect_language,
            audio_file=audio_file,
            cache_folder=cache_folder,
            set_p=set_p,
            uuid=uuid,
            inst=None)
    elif model_type == ZH_RECOGN:
        rs = zh_recogn(
            audio_file=audio_file,
            cache_folder=cache_folder,
            set_p=set_p,
            uuid=uuid,
            inst=None)
    elif model_type == DOUBAO_API:
        rs = doubao_recogn(
            detect_language=detect_language,
            audio_file=audio_file,
            cache_folder=cache_folder,
            set_p=set_p,
            uuid=uuid,
            inst=inst)
    elif model_type == CUSTOM_API:
        rs = recogn_api(
            audio_file=audio_file,
            cache_folder=cache_folder,
            set_p=set_p,
            uuid=uuid,
            inst=None)
    elif model_type == OPENAI_API:
        rs = openairecogn_api(
            detect_language=detect_language,
            audio_file=audio_file,
            set_p=set_p,
            uuid=uuid,
            inst=inst)
    elif type == 'avg':
        rs = avg_recogn(
            detect_language=detect_language,
            audio_file=audio_file,
            cache_folder=cache_folder,
            model_name=model_name,
            set_p=set_p,
            inst=inst,
            uuid=uuid,
            is_cuda=is_cuda)
    else:
        # 其他方式均为faster-whisper
        rs = all_recogn(
            detect_language=detect_language,
            audio_file=audio_file,
            cache_folder=cache_folder,
            model_name=model_name,
            set_p=set_p,
            uuid=uuid,
            inst=inst,
            is_cuda=is_cuda)
    try:
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except Exception:
        pass
    return rs
