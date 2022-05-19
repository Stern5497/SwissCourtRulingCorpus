from __future__ import annotations
from typing import Any, TYPE_CHECKING

import pandas as pd
from sqlalchemy.engine.base import Engine
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import MetaData, Table

from scrc.preprocessors.extractors.abstract_extractor import AbstractExtractor
from scrc.enums.section import Section
from scrc.utils.main_utils import get_config
from scrc.utils.sql_select_utils import delete_stmt_decisions_with_df, join_decision_and_language_on_parameter, \
    join_file_on_decision, where_decisionid_in_list, where_string_spider

if TYPE_CHECKING:
    from pandas.core.frame import DataFrame


class BgeReferenceExtractor(AbstractExtractor):
    """
    Extracts the reference to a bger from bge header section. This is part of the criticality prediction task.
    """

    def __init__(self, config: dict):
        super().__init__(config, function_name='bge_reference_extracting_functions', col_name='bge_reference')
        self.processed_file_path = self.progress_dir / "bge_reference_extracted.txt"
        self.logger_info = {
            'start': 'Started extracting the court compositions',
            'finished': 'Finished extracting the court compositions',
            'start_spider': 'Started extracting the court compositions for spider',
            'finish_spider': 'Finished extracting the court compositions for spider',
            'saving': 'Saving chunk of court compositions',
            'processing_one': 'Extracting the court composition from',
            'no_functions': 'Not extracting the court compositions.'
        }


if __name__ == '__main__':
    config = get_config()
    bge_reference_extractor = BgeReferenceExtractor(config)
    bge_reference_extractor.start()
