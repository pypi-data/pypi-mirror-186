#!/usr/bin/env python

# stdlib imports
import argparse
import datetime as dt
import os
from typing import Optional

# external imports
import pandas as pd

# local imports
import worksheet_grading.config as config
from worksheet_grading.util import bright, print_warn, red, print_err, version_string
from worksheet_grading.gradelib import Frame, parse_config
from worksheet_grading.moodle_util import MoodleCSV as MC


# ========== FEEDBACK EXPORT ========== #

def get_grade(frame : Frame, group):
    if group in frame.data:
        act_pts, _ = frame.data[group].sheet.range_points()
        return act_pts


def get_feedback(frame : Frame, group, collapse):
    if group in frame.data:
        return frame.data[group].sheet.html_string(collapse)


def write_grades(frame: Frame, grade_file: str, outfile: Optional[str], collapse: bool):
    if not os.path.exists(grade_file):
        print_err(f"Grade file {grade_file} not found, exiting")
        exit(1)

    if outfile is None:
        outfile = grade_file

    if any(v.sheet.grade_status() != config.GRADED for _, v in frame.data.items()):
        print_warn("Not all submissions are graded!")
        resp = input("Do you want to continue? [Y/n] ")
        if resp.lower() != "y":
            print("Exiting.")
            exit(0)

    print(bright(f"Exporting Moodle grades to {outfile}....."), end="")

    gf = pd.read_csv(grade_file)
    # check if the maximum points in the grade file correspond to the maximum points in the sheet
    for _, student in gf.iterrows():
        if student[MC.GROUP] in frame.data:
            _, max_pts = frame.data[student[MC.GROUP]].sheet.range_points()
            if max_pts != student[MC.MAX_GRADE]:
                print(red(f"\nmaximum points in exercise range ({max_pts}) do not correspond to max points in grade file ({student['Maximum Grade']}), exiting"))
                exit(1)

    search_column = MC.GROUP if MC.GROUP in gf.columns else MC.FULL_NAME 
    gf[MC.GRADE] = [get_grade(frame, d[search_column]) for _,d in gf.iterrows()]
    gf[MC.FEEDBACK_COMMENTS] = [get_feedback(frame, d[search_column], collapse) for _,d in gf.iterrows()]
    now = dt.datetime.now().strftime(MC.DATE_FORMAT)
    gf[MC.LAST_MODIFIED_GRADE] = [now if get_grade(frame, d[search_column]) is not None else MC.NOT_MODIFIED for _,d in gf.iterrows()]
    
    gf.to_csv(outfile, index=None)
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

    # check whether json file exists
    if not os.path.exists(args.config):
        print_err("No configuration file found at path \"{}\", exiting".format(args.config))
        exit(1)

    # parse json and update globals
    parse_config(args.config, args.suffix, config.DEFAULT_MASK)

    # Create Frame
    f = Frame(config.DEFAULT_MASK)

    f.autosave()
    
    write_grades(f, args.grading_worksheet, args.outfile, not args.no_collapse)


if __name__ == "__main__":
    main()
