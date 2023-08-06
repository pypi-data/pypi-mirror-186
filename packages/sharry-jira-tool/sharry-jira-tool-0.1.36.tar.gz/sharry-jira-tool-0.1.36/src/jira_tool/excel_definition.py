# -*- coding: utf-8 -*-
"""
This module is used to store excel column definition information.
"""
import json
import pathlib
from datetime import datetime
from pathlib import Path

from .milestone import Milestone
from .priority import Priority

__all__ = ["Exceldefinition"]


class Exceldefinition:
    def __init__(self) -> None:
        self.store: list[tuple] = []
        self.sort_strategy_priority: list = []

    def load(self, content: str):
        """
        Load json string to generate the excel definition

        :param content:
            JSON string content
        """

        if content is None:
            raise ValueError("The content is invalid")

        try:
            raw_data = json.loads(content)

            for item in raw_data[0]["SortStrategyPriority"]:
                self.sort_strategy_priority.append(item)

            for item in raw_data[1]["Columns"]:
                column_index = 0
                column_name = None
                column_type = None
                column_require_sort = False
                column_sort_order = False
                column_inline_weights = -1
                column_raise_ranking = -1

                for key, value in item.items():
                    if key.lower() in "index":
                        column_index = value
                    if key.lower() in "name":
                        column_name = value
                    if key.lower() in "type":
                        column_type = Exceldefinition.convert_str_to_type(value)
                    if key.lower() in "RequireSort".lower():
                        column_require_sort = value
                    if key.lower() in "SortOrder".lower():
                        column_sort_order = value
                    if key.lower() in "InlineWeights".lower():
                        column_inline_weights = value
                    if key.lower() in "RaiseRanking".lower():
                        column_raise_ranking = value

                self.store.append(
                    (
                        column_index,
                        column_name,
                        column_type,
                        column_require_sort,
                        column_sort_order,
                        column_inline_weights,
                        column_raise_ranking,
                    )
                )
        except Exception:
            raise ValueError(
                "The JSON file structure is invalid. Please check the documentation: https://github.com/SharryXu/jira-tool"
            )

    def load_file(self, file: "str | Path"):
        """
        Load json file to generate the excel definition

        :param file:
            JSON file location
        """

        if file is None or not pathlib.Path(file).is_absolute():
            raise ValueError("The file is invalid.")

        if not pathlib.Path(file).exists():
            raise ValueError(f"The file is not exist. File: {file}")

        with open(file=file, mode="r") as table_definition_file:
            try:
                self.load(table_definition_file.read())
            finally:
                table_definition_file.close()

    def validate(self) -> "list":
        invalid_definitions = []

        exist_indexes = []
        exist_inline_weights = []
        for (
            column_index,
            column_name,
            column_type,
            column_require_sort,
            column_sort_order,
            column_inline_weights,
            column_raise_ranking,
        ) in self.get_columns():
            # Check Name cannot be empty
            if type(column_name) is not str or len(column_name) == 0:
                invalid_definitions.append(
                    f"Column name cannot be empty. Index: {column_index}"
                )
                continue
            # Check Missing/Duplicate Index
            if type(column_index) is not int:
                invalid_definitions.append(
                    f"Column Index can only be number. Column: {column_name}"
                )
            elif column_index is None:
                invalid_definitions.append(f"Missing Index. Column: {column_name}")
            elif column_index in exist_indexes:
                invalid_definitions.append(f"Duplicate Index. Column: {column_name}")
            else:
                exist_indexes.append(column_index)
            # Check Property Type
            if column_type not in (
                str,
                bool,
                datetime,
                Priority,
                Milestone,
                float,
            ):
                invalid_definitions.append(
                    f"Invalid Column Type. Column: {column_name}"
                )

            # Check Sort
            if type(column_require_sort) is not bool:
                invalid_definitions.append(
                    f"Require Sort can only be True/False. Column: {column_name}"
                )

            if type(column_sort_order) is not bool:
                invalid_definitions.append(
                    f"Sort Order can only be True(Descending)/False(Ascending). Column: {column_name}"
                )

            # TODO: Currently only support different line weights.
            if type(column_inline_weights) is not int:
                invalid_definitions.append(
                    f"Inline Weights can only be number. Column: {column_name}"
                )
            else:
                if (
                    column_inline_weights > 0
                    and column_inline_weights in exist_inline_weights
                ):
                    invalid_definitions.append(
                        f"Duplicate Inline Weights. Column: {column_name}"
                    )
                exist_inline_weights.append(column_inline_weights)

            if type(column_raise_ranking) is not int:
                invalid_definitions.append(
                    f"Raise Ranking can only be number. Column: {column_name}"
                )
            else:
                # Check Support RaiseRanking or not
                if column_type not in (bool,) and column_raise_ranking > 0:
                    invalid_definitions.append(
                        f"Column do not support Raise Ranking feature. Column: {column_name}"
                    )

        if len(invalid_definitions) == 0:
            self.store.sort(key=lambda c: c[0], reverse=False)

            if len(self.store) > 0 and (
                self.store[0][0] != 1
                or self.store[len(self.store) - 1][0] != len(self.store)
            ):
                invalid_definitions.append(
                    f"Column Index must be in continuation and starts from 1."
                )

        return invalid_definitions

    @staticmethod
    def convert_str_to_type(type_str: str) -> "type | None":
        if type_str is None or type(type_str) is not str:
            return None
        type_str = str(type_str).strip().lower()
        if type_str.lower() == "str":
            return str
        elif type_str.lower() == "bool":
            return bool
        elif type_str.lower() == "datetime":
            return datetime
        elif type_str.lower() == "priority":
            return Priority
        elif type_str.lower() == "milestone":
            return Milestone
        # Currently, only support float/double
        elif type_str.lower() == "number":
            return float
        else:
            return None

    def __iter__(self):
        for item in self.store:
            yield item

    def get_columns(self) -> "list[tuple]":
        result = []
        for item in self.store:
            result.append(item)
        return result

    @property
    def max_column_index(self) -> int:
        return self.store[len(self.store) - 1][0]

    def get_sort_strategy_priorities(self) -> "list":
        return self.sort_strategy_priority

    def total_count(self):
        return len(self.store)
