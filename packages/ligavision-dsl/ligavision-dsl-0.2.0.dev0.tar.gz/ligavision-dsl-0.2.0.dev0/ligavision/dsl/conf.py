try:
    from pandas._config.config import (
        get_option,
        register_option,
        reset_option,
        set_option,
    )
except ModuleNotFoundError:
    from pandas.core.config import (
        get_option,
        register_option,
        reset_option,
        set_option,
    )

import pandas as pd

options = pd.options

CONF_RIKAI_VIZ_COLOR = "ligavision.dsl.color"
DEFAULT_RIKAI_VIZ_COLOR = "red"
register_option(CONF_RIKAI_VIZ_COLOR, DEFAULT_RIKAI_VIZ_COLOR)

CONF_RIKAI_IMAGE_DEFAULT_FORMAT = "ligavision.image.default.format"
DEFAULT_IMAGE_DEFAULT_FORMAT = "PNG"
register_option(CONF_RIKAI_IMAGE_DEFAULT_FORMAT, DEFAULT_IMAGE_DEFAULT_FORMAT)

# The hack for Databricks Notebook breaks the Github Notebook Preview
CONF_RIKAI_NOTEBOOK_PLATFORM = "ligavision.notebook.platform"
DEFAULT_NOTEBOOK_PLATFORM = "databricks"
register_option(CONF_RIKAI_NOTEBOOK_PLATFORM, DEFAULT_NOTEBOOK_PLATFORM)
