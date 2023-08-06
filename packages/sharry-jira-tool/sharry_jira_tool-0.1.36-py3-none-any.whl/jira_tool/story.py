import re
from datetime import datetime
from decimal import Decimal
from operator import attrgetter
from typing import Any

from dateutil import parser

from .excel_definition import Exceldefinition
from .milestone import *
from .priority import *
from .sprint_schedule import SprintScheduleStore

__all__ = [
    "Story",
    "StoryFactory",
    "convert_to_bool",
    "convert_to_datetime",
    "convert_to_decimal",
    "sort_stories_by_property_and_order",
    "sort_stories_by_raise_ranking",
]


def convert_to_bool(raw: Any) -> bool:
    if type(raw) is bool:
        return raw
    value = str(raw).strip().upper()
    if value == "YES" or value == "TRUE":
        return True
    else:
        return False


def convert_to_decimal(raw: Any) -> Decimal:
    if type(raw) is Decimal:
        return raw
    raw = str(raw).strip()
    pattern = re.compile("[0-9.]{1,10}")
    result = pattern.search(raw)
    if result is not None:
        return Decimal(result.group())
    else:
        return Decimal(0)


def convert_to_datetime(raw: Any) -> "datetime | None":
    if type(raw) is datetime:
        return raw
    if raw is None:
        return
    raw = str(raw).strip()
    return parser.parse(raw)


class Story(object):
    def __init__(self, factory: "StoryFactory") -> None:
        if factory is None:
            raise ValueError("Story must be created from a specific factory!")
        self.factory = factory
        for column in self.factory.columns:
            if column[2] is str:
                setattr(self, column[1], "")
            elif column[2] is bool:
                setattr(self, column[1], False)
            elif column[2] is Priority:
                setattr(self, column[1], Priority.NA)
            elif column[2] is Milestone:
                setattr(self, column[1], None)
            elif column[2] is datetime:
                setattr(self, column[1], None)
            else:
                setattr(self, column[1], None)

    def __getitem__(self, property_name) -> Any:
        return getattr(self, property_name)

    def format_value(self, property_name: str) -> str:
        property = getattr(self, property_name, None)
        if property is None:
            return ""
        elif type(property) is datetime:
            return property.date().isoformat()
        elif type(property) is bool:
            if property:
                return "Yes"
            else:
                return "No"
        # TODO: Support customized format string in JSON.
        elif type(property) is float:
            return str(property)
        else:
            return str(property)

    def set_value(self, property_type: Any, property_name: str, property_value: Any):
        if property_type is str:
            setattr(self, property_name, property_value)
        elif property_type is bool:
            setattr(self, property_name, convert_to_bool(property_value))
        elif property_type is Priority:
            setattr(self, property_name, convert_to_priority(property_value))
        elif property_type is datetime:
            setattr(self, property_name, convert_to_datetime(property_value))
        elif property_type is Milestone:
            milestone = Milestone(property_value)
            setattr(self, property_name, milestone)
        else:
            setattr(self, property_name, property_value)

    def __setitem__(self, property_name, property_value):
        self.set_value(type(property_value), property_name, property_value)

    def calc_sprint_schedule(self, sprint_schedule: SprintScheduleStore):
        for _, column_name, column_type, _, _, _, _ in self.factory.columns:
            if column_type is Milestone:
                self[column_name].calc_priority(sprint_schedule)

    # Currently, comparing story only consider the Priority properties.
    def __lt__(self, __o: "Story | None") -> bool:
        return self.factory.compare_story(self, __o) < 0

    def __le__(self, __o: "Story | None") -> bool:
        return self.factory.compare_story(self, __o) <= 0

    def __gt__(self, __o: "Story | None") -> bool:
        return self.factory.compare_story(self, __o) > 0

    def __ge__(self, __o: "Story | None") -> bool:
        return self.factory.compare_story(self, __o) >= 0

    def __eq__(self, __o: "Story | None") -> bool:
        return self.factory.compare_story(self, __o) == 0

    # For CSV consideration.
    def __str__(self):
        result = ""
        if self is None:
            return result

        separator = ", "
        for _, column_name, _, _, _, _, _ in self.factory.columns:
            if hasattr(self, column_name):
                result += f"{str(getattr(self, column_name))}{separator}"
        return result


class StoryFactory(object):
    def __init__(self, columns: "list[tuple]") -> None:
        if columns is None:
            raise ValueError("Columns must be provided!")
        self._columns = columns
        self._compare_rules = self.__generate_compare_rules()

    def __generate_compare_rules(self) -> "list[tuple[str, int]]":
        compare_rules = []
        for _, column_name, _, _, _, inline_weights, _ in self._columns:
            if inline_weights > 0:
                compare_rules.append((column_name, inline_weights))
        compare_rules.sort(key=lambda r: r[1], reverse=True)
        return compare_rules

    @property
    def columns(self):
        return self._columns

    @property
    def compare_rules(self) -> "list[tuple[str, int]]":
        return self._compare_rules

    def create_story(self) -> Story:
        return Story(self)

    # TODO: Need to include all sort strategies.
    def compare_story(self, a: "Story | None", b: "Story | None") -> int:
        """
        Compare two stories.

        :parm a:
            First story
        :parm b:
            Second story
        :parm sort_rule:
            Priority information
        :return
            1: means a > b
            0: means a == b
            -1: means a < b
        """
        if a is None or b is None:
            raise ValueError("The compare stories cannot be None.")

        if a.factory != b.factory or a.factory != self or b.factory != self:
            raise ValueError("The compare stories were built by different factory.")

        rules_count = len(self.compare_rules)

        if rules_count == 0:
            return 0

        skip_index_of_a = []
        skip_index_of_b = []
        count = rules_count
        while count > 0:
            # property_value, property_location
            highest_property_of_a = None
            highest_property_of_b = None
            for i in range(len(self.compare_rules)):
                if i in skip_index_of_a:
                    continue

                if highest_property_of_a is None:
                    # property_value, property_location
                    highest_property_of_a = (a[self.compare_rules[i][0]], i)

                if a[self.compare_rules[i][0]] > highest_property_of_a[0]:
                    highest_property_of_a = (a[self.compare_rules[i][0]], i)

            for i in range(len(self.compare_rules)):
                if i in skip_index_of_b:
                    continue

                if highest_property_of_b is None:
                    highest_property_of_b = (b[self.compare_rules[i][0]], i)

                if b[self.compare_rules[i][0]] > highest_property_of_b[0]:
                    highest_property_of_b = (b[self.compare_rules[i][0]], i)

            if highest_property_of_a is None:
                highest_property_of_a = (Priority.NA, count)
            else:
                skip_index_of_a.append(highest_property_of_a[1])

            if highest_property_of_b is None:
                highest_property_of_b = (Priority.NA, count)
            else:
                skip_index_of_b.append(highest_property_of_b[1])

            # priority value
            if highest_property_of_a[0] > highest_property_of_b[0]:
                return 1
            elif highest_property_of_a[0] == highest_property_of_b[0]:
                if highest_property_of_a[1] < highest_property_of_b[1]:
                    return 1
                elif highest_property_of_a[1] > highest_property_of_b[1]:
                    return -1
            else:
                return -1

            # property location
            if highest_property_of_a[1] > highest_property_of_b[1]:
                return 1
            elif highest_property_of_a[1] == highest_property_of_b[1]:
                if highest_property_of_a[0] > highest_property_of_b[0]:
                    return 1
                elif highest_property_of_a[0] < highest_property_of_b[0]:
                    return -1
            else:
                return -1

            count -= 1
            continue
        return 0


def sort_stories_by_property_and_order(
    stories: "list[Story]", excel_definition: Exceldefinition
):
    sort_rules = []
    excel_definition_columns = excel_definition.get_columns()

    for _, column_name, _, require_sort, sort_order, _, _ in excel_definition_columns:
        if require_sort is True:
            sort_rules.append((column_name, sort_order))

    _internal_sort_stories_by_property_and_order(stories, sort_rules)


def _internal_sort_stories_by_property_and_order(
    stories: "list[Story]", sort_rules: "list[tuple]"
):
    for column_name, sort_order in reversed(sort_rules):
        stories.sort(key=attrgetter(column_name), reverse=sort_order)


def sort_stories_by_raise_ranking(
    stories: "list[Story]", excel_definition: Exceldefinition
) -> "list[Story]":
    if stories is None:
        return []
    sort_rules = []
    excel_definition_columns = excel_definition.get_columns()

    for (
        _,
        column_name,
        _,
        _,
        _,
        _,
        ranking,
    ) in excel_definition_columns:
        if ranking > 0:
            sort_rules.append((column_name, ranking))

    if len(sort_rules) == 0:
        return stories

    sort_rules.sort(key=lambda x: x[1], reverse=True)

    result = []

    for property_name, _ in sort_rules:
        result = _raise_story_ranking_by_property(stories, property_name)

    return result


def _raise_story_ranking_by_property(
    stories: "list[Story]", property_name: str
) -> "list[Story]":
    if stories is None or len(stories) == 0:
        return stories
    # Use first story as example
    if not hasattr(stories[0], property_name):
        return stories
    # Only bool indicator for now
    if type(getattr(stories[0], property_name)) is not bool:
        return stories
    result: list[Story] = [stories[0]] * len(stories)
    j = 0
    for i in range(len(stories)):
        if getattr(stories[i], property_name) is True:
            result[j] = stories[i]
            j += 1
    for i in range(len(stories)):
        if getattr(stories[i], property_name) is False:
            result[j] = stories[i]
            j += 1
    return result
