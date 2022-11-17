import os
import sys
sys.path.append(os.path.abspath('..'))
from configs.database import DatabaseConfig
from configs.batch import BatchEnvConfig
from utils.util import Util


DATABASES = {
    'mysql': Util.get_database_config_dict(
        database_config=DatabaseConfig(), batch_env_config=BatchEnvConfig()
    )
}
