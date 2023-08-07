#!/usr/bin/env python3

# stdlib imports
import argparse
import os
import sys
import json
from typing import Dict

# external imports
import pandas as pd

# local imports
from worksheet_grading.config import JSON_EXERCISES, JSON_GROUPSIZE, JSON_SHEETNAME, CSV_BASENAME, STUDENT_FORMAT, NA, REMARKS_FILE
from worksheet_grading.util import bright, version_string, print_err
from worksheet_grading.moodle_util import MoodleCSV as MC

def parse_groups(df: pd.DataFrame):
    groups : Dict[str, list] = {}
    max_len = 0
    if MC.GROUP in df.columns:
        for i, r in df.iterrows(): 
            if r[MC.GROUP] != MC.NO_GROUP and r[MC.LAST_MODIFIED_SUB] != MC.NOT_MODIFIED:
                if r[MC.GROUP] not in groups: 
                    groups[r[MC.GROUP]] = [r[MC.FULL_NAME]]
                    max_len = max(max_len, 1)
                else:
                    groups[r[MC.GROUP]].append(r[MC.FULL_NAME])
                    groups[r[MC.GROUP]].sort()
                    max_len = max(max_len, len(groups[r[MC.GROUP]]))
    elif MC.FULL_NAME in df.columns:
        # make id number the group name
        for i, r in df.iterrows():
            if r[MC.LAST_MODIFIED_SUB] != MC.NOT_MODIFIED:
                groups[r[MC.FULL_NAME]] = [r[MC.FULL_NAME]]
        max_len = 1
    else:
        print_err("No group column in CSV files, exiting")
        exit(1)

    return groups, max_len        


def generate_config(config_path, group_size, exc_range, sheetname, max_points):
    print("Generating JSON config file:\n")
    num_ex = len(exc_range)
    cnf = {}
    cnf[JSON_EXERCISES] = {}
    pts_per_ex = int(max_points//num_ex)
    for e in exc_range:
        cnf[JSON_EXERCISES][str(e)] = [pts_per_ex]
    cnf[JSON_EXERCISES][str(num_ex)] = [int(pts_per_ex+(max_points-pts_per_ex*num_ex))]
    cnf[JSON_GROUPSIZE] = group_size
    if sheetname is not None:
        cnf[JSON_SHEETNAME] = sheetname
    else:
        cnf[JSON_SHEETNAME] = "sheet"
    cnf_content = json.dumps(cnf, indent=True)
    print(cnf_content)
    with open(config_path, "w") as f:
        f.write(cnf_content)
    print(f"\nSaved config to '{config_path}'.")


def check_config(config_path):
    if os.path.exists(config_path):
        resp = input(f"'{config_path}' already exists.\nDo you want to overwrite it? [Y/n] ")
        return resp.lower() == "y"
    return True


def check_files(csv_files):
    existing = []
    for f in csv_files:
        if os.path.exists(f):
            existing.append(f) 
    
    if existing:
        resp = input(f"Files {', '.join(existing)} exist.\nDo you want to overwrite them? [Y/n] ")
        return resp.lower() == "y"
    return True


def generate_csv(csv_file, index, groups, group_size):
    df_base = {"exercise": [index] * len(groups)}
    df = pd.DataFrame(df_base)
    df["group"] = sorted(groups.keys())
    for i in range(group_size):
        df[STUDENT_FORMAT.format(i+1)] = [groups[gr][i] if i < len(groups[gr]) else NA for gr in df["group"]]
    df["points"] = NA
    df["feedback"] = ""
    print(f"Generating {csv_file}... ", end="")
    df.to_csv(csv_file, index=False)
    print(f"Done"); 


def main():
    __program__ = "Worksheet Grading Importer"
    parser = argparse.ArgumentParser(__program__, description="Import student and group information from Moodle CSV. Creates a CSV file for each exercise and a configuration JSON file.", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("grading_worksheet", help="Path to the Moodle grading worksheet", type=str)
    parser.add_argument("-e", "--num-exercises", help="Number of exercises in the worksheet", type=int, required=True)
    parser.add_argument("-r", "--remarks", help="Whether to generate general remarks file", action="store_true")
    parser.add_argument('-s', '--sheet-name', help="Sheet name for generated files", required=True)
    parser.add_argument('-c', '--config', default="config.json", help="Destination path of config file for sheet data")
    parser.add_argument('-o', '--outdir', help="Output directory for generated files (default: current dir)")
    parser.add_argument('--start-exercise', help="Starting exercise (exercise range is [start_exercise; start_exercise+num_exercises-1])", default=1, type=int)
    parser.add_argument('--version', action="version", help="Display version and license information", version=version_string(__program__))
    args = parser.parse_args()
    
    if not os.path.exists(args.grading_worksheet):
        print(f"{args.grading_worksheet} is not a valid path", file=sys.stderr)
    
    df = pd.read_csv(args.grading_worksheet)	
    print(f"Successfully read grades file '{args.grading_worksheet}'.")

    groups, group_size = parse_groups(df)

    print(f"Found {len(df)} students and {len(groups)} groups of max size {group_size}\n")

    exc_range = range(args.start_exercise, args.start_exercise+args.num_exercises)
    csv_files = [args.sheet_name + CSV_BASENAME.format(i) for i in exc_range]
    if args.outdir is not None:
        csv_files = [os.path.join(args.outdir, c) for c in csv_files]

    if check_files(csv_files):
        for c,i in zip(csv_files, exc_range):
            generate_csv(c,i, groups, group_size)
        print()
    else:
        print("Skipping exercise csv generation\n")
        
    if args.remarks and check_files([args.sheet_name + CSV_BASENAME.format(0)]):
        print("Generating remarks file")
        generate_csv(REMARKS_FILE.format(args.sheet_name), 0, groups, group_size)
        print()
    
    if check_config(args.config):
        max_points = df[MC.MAX_GRADE][0]
        generate_config(args.config, group_size, exc_range, args.sheet_name, max_points)
        print(bright(f"You can now adapt the config file ('{args.config}') according to the worksheet layout and add handins."))
        print(f"Make sure that the points in the \"exercises\" section of the config file sum up to the maximum grade ({max_points})")
    else:
        print("Skipping config generation")




if __name__ == "__main__":
	main()