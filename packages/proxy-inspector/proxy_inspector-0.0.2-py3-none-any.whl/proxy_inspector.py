import logging
import random
from urllib.parse import urlparse
import requests
from useragents import user_agents


class ProxyInspector:
    """
    a simple tool for verify proxy
    """

    def __init__(self):
        pass

    def validate(self, target_url: str, proxy_url: str, include_text: str = None, exclude_text: str = None) -> bool:
        """
        An Simple Tool for Validate Proxy | 验证代理
        :param target_url: Target URL, like "https://www.bing.com/robots.txt" | 目标 URL , 形如 "https://www.bing.com/robots.txt"
        :param proxy_url: Proxy URL, like "http://127.0.0.1:7777" | 代理的URL, 形如 "http://127.0.0.1:7777"
        :param include_text: response must include text, like "User-agent", can be None | 响应体内必须包含的文本, 可以为空, 形如 "User-agent"
        :param exclude_text: response must not include text, like "I'm Robots", can be None | 响应体内不可以包含的文本, 可以为空, 形如 "I'm Robots"
        :return: return True if the condition is met | 满足条件返回 True

        """

        # ----------------------------------------
        # Preparation
        # ----------------------------------------
        if include_text:
            include_text = include_text.strip()
        if exclude_text:
            exclude_text = exclude_text.strip()

        result_include = False
        result_exclude = False

        proxy_url_obj = urlparse(proxy_url)
        proxy_scheme = proxy_url_obj.scheme
        proxy_netloc = proxy_url_obj.netloc

        target_url_obj = urlparse(target_url)
        target_scheme = target_url_obj.scheme
        target_netloc = target_url_obj.netloc

        # ----------------------------------------
        # Parameter Check
        # ----------------------------------------
        if proxy_scheme != target_scheme:
            return False

        # ----------------------------------------
        # Request Network
        # ----------------------------------------
        user_agent = random.choice(user_agents)
        headers = {
            'Referer': 'https://www.google.com/',
            'user-agent': user_agent,
        }
        try:
            req = requests.get(target_url, timeout=15, stream=True,
                               proxies={proxy_scheme: proxy_netloc}, headers=headers)
            if req.status_code == 200:

                if include_text:
                    if include_text in req.text:
                        result_include = True
                    else:
                        result_include = False
                else:
                    result_include = True

                if exclude_text:
                    if exclude_text not in req.text:
                        result_exclude = True
                    else:
                        result_exclude = False
                else:
                    result_exclude = True
            else:
                # logging.debug(f"Can not get {target_url} by {proxy_url} code:{req.status_code}  "
                #               f"headers:{req.headers}, text:{req.text}")
                logging.error(f"Can not get {target_url} by {proxy_url} code:{req.status_code}")
        except requests.exceptions.ProxyError as ex:
            logging.error(f"Cannot connect to proxy:{proxy_url}")
        except requests.exceptions.SSLError as ex:
            logging.error(f"Not a safe proxy:{proxy_url}")
        except requests.exceptions.ConnectTimeout as ex:
            logging.error(f"Timeout when connect to {target_url} with {proxy_url}")
        except Exception as ex:
            logging.exception(f"Can not get {target_url} using proxy:{proxy_url}")

        return result_include and result_exclude
