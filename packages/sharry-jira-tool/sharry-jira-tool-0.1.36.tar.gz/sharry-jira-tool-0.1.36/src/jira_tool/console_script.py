# -*- coding: utf-8 -*-
"""
This module is used to provide the console program.
"""
import os
import pathlib
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace

from .excel_operation import process_excel_file

__all__ = ["sort_excel_file"]


def get_args() -> Namespace:
    parser = ArgumentParser(
        description="Jira tool: Used to sort stories",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "input_file", metavar="input_file", type=pathlib.Path, help="Source Excel file."
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        metavar="",
        type=pathlib.Path,
        required=False,
        help="Output folder.",
    )
    parser.add_argument(
        "--excel_definition_file",
        metavar="",
        type=pathlib.Path,
        required=False,
        help="Excel definition JSON file.",
    )
    parser.add_argument(
        "--sprint_schedule_file",
        metavar="",
        type=pathlib.Path,
        required=False,
        help="Milestone priority JSON file.",
    )
    parser.add_argument(
        "--over_write",
        metavar="",
        type=bool,
        required=False,
        help="Whether or not to over write existing file.",
    )

    args = parser.parse_args()

    return args


# TODO:
# 1. Create new script to generate excel (empty)


def sort_excel_file():
    try:
        args = get_args()

        # Pre-Process input file
        input_file_absolute_path: pathlib.Path = (
            pathlib.Path.cwd() / args.input_file.as_posix()
        ).resolve()

        if input_file_absolute_path.suffix.lower() != ".xlsx":
            print(f"Please provide an Excel file. File: {input_file_absolute_path}.")
            quit(1)

        if not os.path.exists(input_file_absolute_path):
            print(f"Input file is not exist. File: {input_file_absolute_path}.")
            quit(1)

        input_file_name_without_extension = input_file_absolute_path.stem

        # Pre-Process output file
        output_folder_absolute_path: pathlib.Path = (
            input_file_absolute_path.parent.absolute()
        )

        if args.output_folder is not None:
            temp = pathlib.Path(args.output_folder).resolve()
            if temp.is_dir():
                output_folder_absolute_path = temp.absolute()
            else:
                output_folder_absolute_path = temp.parent.absolute()

        if not output_folder_absolute_path.exists():
            output_folder_absolute_path.mkdir(parents=True, exist_ok=True)

        output_file_absolute_path: pathlib.Path = (
            output_folder_absolute_path
            / f"{input_file_name_without_extension}_sorted.xlsx"
        ).resolve()

        copy_count = 1
        while output_file_absolute_path.exists():
            output_file_absolute_path = (
                output_folder_absolute_path
                / f"{ output_file_absolute_path.stem }_{copy_count}.xlsx"
            )
            copy_count += 1

        excel_definition_file_absolute_path = None

        if args.excel_definition_file is not None:
            excel_definition_file_absolute_path = pathlib.Path(
                args.excel_definition_file
            ).resolve()

            if excel_definition_file_absolute_path.suffix.lower() != ".json":
                print(
                    f"Please provide an JSON file for Excel definition. File: {excel_definition_file_absolute_path}."
                )
                quit(1)

        sprint_schedule_file_absolute_path = None

        if args.sprint_schedule_file is not None:
            sprint_schedule_file_absolute_path = pathlib.Path(
                args.sprint_schedule_file
            ).resolve()

            if sprint_schedule_file_absolute_path.suffix.lower() != ".json":
                print(
                    f"Please provide an JSON file for sprint schedule. File: {sprint_schedule_file_absolute_path}."
                )
                quit(1)

        # Over write parameter.
        over_write = True
        if args.over_write is not None:
            over_write = args.over_write

        process_excel_file(
            input_file_absolute_path,
            output_file_absolute_path,
            excel_definition_file_absolute_path,
            sprint_schedule_file_absolute_path,
            over_write,
        )

        quit(0)
    except Exception as e:
        print(e)
        quit(1)
