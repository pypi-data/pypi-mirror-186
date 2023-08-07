#!/usr/bin/env python3

import argparse
import csv

from worksheet_grading.util import version_string

def suffixed_filename(csvname, suffix):
    cleaned_csv_name = csvname.replace(".csv", "")
    return cleaned_csv_name + suffix + ".csv"

def transform_row(row):
    r = []
    for _r in row:
        if "@" in _r or " " in _r or _r.isspace() or _r == "":
            r.append("\""+_r+"\"")
        else:
            r.append(_r)
    return ",".join(r)

def split_csv(csvname, suffixes):
    lines = [[] for s in suffixes]

    # read source file
    with open(csvname, "r") as source:
        reader = csv.reader(source, delimiter=",", quotechar="\"")
        for (i, row) in enumerate(reader):
            l = transform_row(row)
            if i == 0:
                for s in range(len(suffixes)):
                    lines[s].append(l)
            else:
                lines[(i-1)%len(suffixes)].append(l)
    
    # write to files
    for (i, s) in enumerate(suffixes):
        with open(suffixed_filename(csvname, s), "w") as f:
            for l in lines[i]:
                f.write(l + "\n") 

def merge_csv(target, source_suffixes):
    lines = [[] for s in source_suffixes]
    # read csv files
    for (i, s) in enumerate(source_suffixes):
        with open(suffixed_filename(target, s), "r") as source:
            reader = csv.reader(source, delimiter=",", quotechar="\"")
            for (j, row) in enumerate(reader):
                l = transform_row(row)
                lines[i].append(l)

    # check that first line is equal
    firstline = lines[0][0]
    for i in range(len(source_suffixes)):
        if firstline != lines[i][0]:
            print("First lines of supplied files are not equal, exiting.")
            exit(1)

    # merge csv files
    with open(target, "w") as f:
        maxlen = max([len(s) for s in lines])
        f.write(firstline+"\n")
        for j in range(1, maxlen):
            for i in range(len(source_suffixes)):
                if j < len(lines[i]):
                    f.write(lines[i][j]+"\n")     

def main():
    __program__ = "Worksheet Grading CSV Splitter"
    parser = argparse.ArgumentParser(__program__, description="Split up csv files or merge previously split up files", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("csvname", help="the csv file that should be split up / target for the merge")
    parser.add_argument("suffixes", nargs="+", help="the file suffixes that the csv should be split up to / merged to csv file")
    parser.add_argument("--merge", help="whether to run the script in MERGE mode (i.e. reverse the split)", action="store_true")
    parser.add_argument("--version", help="display version and license information", action="version", version=version_string(__program__))

    args = parser.parse_args()

    if args.merge:
        merge_csv(args.csvname, args.suffixes)
    else:
        split_csv(args.csvname, args.suffixes)

if __name__ == "__main__":
    main()
