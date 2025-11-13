from functools import lru_cache
from os import path

__all__ = ['get_settings']

ENV_FILES = ('.env',)
ROOT_PATH = path.dirname(path.abspath(path.join(__file__, '..')))


class BaseSettings:
    class Config:
        env_file = ENV_FILES
        env_file_encoding = 'utf-8'


class Settings(BaseSettings):
    version: str = 'v2.4.3'
    # dev test staging prod
    serv_env: str = 'dev'
    serv_name: str = 'grantit-risk-model'
    auth_server_url: str = "http://localhost:3005"

    """数据源配置"""
    db_hostname: str = 'localhost'
    db_user: str = 'postgres'
    db_pass: str = '123456'
    db_post: int = 5432
    db_name: str = 'grantit-dev'
    db_pool_min_size: int = 1
    db_pool_max_size: int = 10
    db_timeout: int = 60  # 秒
    db_statement_timeout: int = 60 * 1000  # 毫秒
    db_lock_timeout: int = 60 * 1000  # 毫秒
    db_idle_in_transaction_session_timeout: int = 60 * 1000  # 毫秒
    db_timezone: str = 'Asia/Shanghai'

    mq_host: str = 'localhost'
    mq_port: int = 5672
    mq_virtual_host: str = '/'
    mq_username: str = 'guest'
    mq_password: str = 'guest'
    mq_exchange: str = 'userExchange'
    mq_queue: str = 'riskUserQueue'

    # 是否启用静态资源
    enabled_static: bool = True
    # 静态资源URL路径
    static_path: str = '/static'
    # 静态资源本地路径
    static_directory: str = path.join(ROOT_PATH, 'static')

    # CORS 跨域资源共享
    # 允许跨域的源列表 eg. '["*"]'   '["http://localhost", "http://localhost:8080", "https://www.example.org"]'
    cors_allow_origins: str = '["*"]'

    white_list_path: list = [
        "/healthy",
    ]

    # 项目根路径
    root_path: str = ROOT_PATH
    # 默认请求超时
    request_timeout: int = 60
    # 时区
    timezone: str = 'Asia/Shanghai'
    # 日期时间格式
    datetime_fmt: str = '%Y-%m-%d %H:%M:%S'

    # risk amount strategy
    a_amount_strategy_tail_loan: str = '1,3,4,5,6,7,8,9'  # new loan
    a_amount_strategy_tail_reloan: str = '1,3,5,7,9'  # reloan
    a_amount_strategy_tail_reapply: str = ''  # reapply and reapply180

    # logger
    logger_name: str = "risk"

    def __str__(self):
        return f"env:{self.serv_env},version:{self.version}"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
