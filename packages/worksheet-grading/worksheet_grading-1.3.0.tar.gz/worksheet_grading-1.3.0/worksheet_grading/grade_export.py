#!/usr/bin/env python

# stdlib imports
import argparse
import re
import datetime as dt
import os
import sys
import itertools

# external imports
import pandas as pd

# local imports
import worksheet_grading.config as config
from worksheet_grading.util import bright, print_warn, red, print_err, version_string
from worksheet_grading.gradelib import Frame, parse_config


# ========== FEEDBACK EXPORT ========== #

def get_grade(frame, group):
    if group in frame.data:
        act_pts, _ = frame.data[group].sheet.range_points()
        return act_pts


def get_feedback(frame, group, collapse):
    if group in frame.data:
        return frame.data[group].sheet.html_string(collapse)


def write_grades(frame: Frame, grade_file: str, outpath: str, collapse: bool):
    gf_head, gf_tail = os.path.split(grade_file)
    if gf_tail is None:
        print(f"{grade_file} is not a valid path", file=sys.stderr)
        exit(1)
    

    if outpath is None:
        ggf = os.path.join(gf_head, f"{gf_tail}")
    else:
        ggf = outpath

    if any([v.sheet.grade_status() != config.GRADED for _, v in frame.data.items()]):
        print_warn("Not all submissions are graded!")
        resp = input("Do you want to continue? [Y/n] ")
        if resp.lower() != "y":
            print("Exiting.")
            exit(0)

    print(bright(f"Exporting Moodle grades to {ggf}....."), end="")

    if not os.path.exists(grade_file):
        print(red(f"Grade file {grade_file} not found, exiting"))
        exit(1)

    gf = pd.read_csv(grade_file)
    for _, student in gf.iterrows():
        if student["Group"] in frame.data:
            _, max_pts = frame.data[student["Group"]].sheet.range_points()
            if max_pts != student["Maximum Grade"]:
                print(red(f"\nmaximum points in exercise range ({max_pts}) do not correspond to max points in grade file ({student['Maximum Grade']}), exiting"))
                exit(1)
        
    gf["Grade"] = [get_grade(frame, d["Group"]) for _,d in gf.iterrows()]
    gf["Feedback comments"] = [get_feedback(frame, d["Group"], collapse) for _,d in gf.iterrows()]
    now = dt.datetime.now().strftime("%A, %d %b %Y, %I:%M %p")
    gf["Last modified (grade)"] = [now if get_grade(frame, d["Group"]) is not None else "-" for _,d in gf.iterrows()]
    
    gf.to_csv(ggf, index=None)
    print(bright("done"))
            
        

# ========== MAIN ========== #

def main():
    # Parse arguments
    __program__ = 'Worksheet Grading Exporter'
    parser = argparse.ArgumentParser(__program__, description='Export grades and feedback to Moodle Grading Worksheet', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-s', '--suffix', help="File suffix for considered csv files")
    parser.add_argument('-c', '--config', default="config.json", help="Config file for the sheet data")
    parser.add_argument('-o', '--outfile', help="Path for grading worksheet output, defaults to the input file path (overwrite)")
    parser.add_argument('--no-collapse', help="Disable collapsing of HTML lists for exercises with single subexercise", action="store_true")
    parser.add_argument('grading_worksheet', help="Input Moodle grading worksheet")
    parser.add_argument('--version', action="version", help="Display version and license information", version=version_string(__program__))
    args = parser.parse_args()

    # parse exercise range
    first_ex = config.DEFAULT_FIRSTEX
    last_ex = config.DEFAULT_LASTEX

    # check whether json file exists
    if not os.path.exists(args.config):
        print_err("No configuration file found at path \"{}\", exiting".format(args.config))
        exit(1)

    # parse json and update globals

    parse_config(args.config, args.suffix)

    # Create Frame
    f = Frame(first_ex, last_ex)

    f.autosave()
    
    write_grades(f, args.grading_worksheet, args.outfile, not args.no_collapse)


if __name__ == "__main__":
    main()
