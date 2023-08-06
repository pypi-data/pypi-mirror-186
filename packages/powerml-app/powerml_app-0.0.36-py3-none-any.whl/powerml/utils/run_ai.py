import requests
from ratelimit import limits, sleep_and_retry
import logging
from powerml.utils.config import get_config
import backoff
from powerml.utils.constants import N_LOGPROBS

logger = logging.getLogger(__name__)


def query_powerml(prompt="Say this is a test",
                  stop="",
                  model="llama",
                  max_tokens=128,
                  temperature=0,
                  key="",
                  allowed_tokens=None,
                  ):
    if key == "":
        cfg = get_config()
        key = cfg['powerml.key']
    params = {
        "prompt": prompt,
        "model": model,
        "max_tokens": max_tokens,
        "stop": stop,
        "temperature": temperature,
    }
    if not allowed_tokens is None:
        params["allowed_tokens"] = allowed_tokens
    # if the model is one of our models, then hit our api
    resp = powerml_completions(params, key)
    resp = resp.json()
    if 'error' in resp:
        raise Exception(str(resp))
    text = resp['completion']
    return text


def query_openai(prompt="Say this is a test",
                 stop="",
                 model="llama",
                 max_tokens=128,
                 temperature=0,
                 key="",
                 allowed_tokens=None,
                 ):
    text, _ = query_openai_with_logprobs(
        prompt, stop, model, max_tokens, temperature, key, allowed_tokens)
    return text


def batch_query_openai(prompt="Say this is a test",
                       stop="",
                       model="llama",
                       max_tokens=128,
                       temperature=0,
                       key="",
                       allowed_tokens=None,
                       ):
    text, _ = batch_query_openai_with_logprobs(
        prompt, stop, model, max_tokens, temperature, key, allowed_tokens)
    return text


def query_openai_with_logprobs(prompt="Say this is a test",
                               stop="",
                               model="llama",
                               max_tokens=128,
                               temperature=0,
                               key="",
                               allowed_tokens=None,
                               n_logprobs=N_LOGPROBS,
                               ):
    resp = query_openai_helper(
        prompt, stop, model, max_tokens, temperature, key, allowed_tokens, n_logprobs)
    text = resp['choices'][0]['text']
    logprobs = resp['choices'][0]['logprobs']
    return text, logprobs


def batch_query_openai_with_logprobs(prompt="Say this is a test",
                                     stop="",
                                     model="llama",
                                     max_tokens=128,
                                     temperature=0,
                                     key="",
                                     allowed_tokens=None,
                                     ):
    resp = query_openai_helper(
        prompt, stop, model, max_tokens, temperature, key, allowed_tokens)
    text = [chosen['text'] for chosen in resp['choices']]
    logprobs = resp['choices'][0]['logprobs']
    return text, logprobs


def query_openai_helper(prompt="Say this is a test",
                        stop="",
                        model="llama",
                        max_tokens=128,
                        temperature=0,
                        key="",
                        allowed_tokens=None,
                        n_logprobs=None,
                        ):
    if key == "":
        cfg = get_config()
        key = cfg['openai.key']
    params = {
        "prompt": prompt,
        "model": model,
        "max_tokens": max_tokens,
        "stop": stop,
        "temperature": temperature,
        "logprobs": n_logprobs,
    }
    if not allowed_tokens is None:
        params["allowed_tokens"] = allowed_tokens
    resp = openai_completions(params, key)
    resp = resp.json()
    if 'error' in resp:
        raise Exception(str(resp))
    return resp


@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_time=20)
def powerml_completions(params, key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + key,
    }
    response = requests.post(
        url="https://api.staging.powerml.co/v1/completions",
        headers=headers,
        json=params)
    if response.status_code != 200:
        raise requests.exceptions.RequestException
    return response


@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_time=20)
def openai_completions(params, key):
    headers = {
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json", }
    response = requests.post(
        url="https://api.openai.com/v1/completions",
        headers=headers,
        json=params)
    if response.status_code == 429:
        raise requests.exceptions.RequestException
    return response
