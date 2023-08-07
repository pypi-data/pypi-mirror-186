# standard library imports
import csv
import re
import os
import json  # json config file parsing
from typing import Dict, List
import enum

# external imports
import pandas as pd # easier csv file modification 

# local library imports
from worksheet_grading.util import *
import worksheet_grading.config as config


# ========== DATA STRUCTURE ========== #

class GradeStatus(enum.Enum):
    GRADED = 0
    PARTIALLY_GRADED = 1
    UNGRADED = 2


class Exercise:
    def __init__(self, ex_num, num_answ, max_points, name=None):
        self.number : int = ex_num
        self.answers : List[Answer] = [Answer(i+1) for i in range(num_answ)]
        if name is not None:
            self.name = name
        self.max_points = max_points

    def deduct(self, answer_num, reason, points):
        if answer_num > len(self.answers) or answer_num < 1:
            print_err("Invalid Answer")
            return
        self.answers[answer_num - 1].deduct(reason, points)

    def _grade_status(self) -> GradeStatus:
        grade_status = [a.graded for a in self.answers]
        if not any(grade_status):
            return GradeStatus.UNGRADED
        else:
            if all(grade_status):
                return GradeStatus.GRADED
            else:
                return GradeStatus.PARTIALLY_GRADED

    def mark_correct(self, ans_num):
        self.answers[ans_num - 1].mark_correct()

    def _calc_points(self) -> float:
        p = self.max_points
        for a in self.answers:
            p += a.deductions.deducted_points()
        if p < 0:
            p = 0
        # don't format as float if not necessary
        if p == round(p):
            p = round(p)
        return p

    grade_status = property(_grade_status)
    act_points = property(_calc_points)

    def csv_feedback(self):
        if self.grade_status == GradeStatus.GRADED:
            fb_str = ""
            for ans in self.answers:
                fb_str += ans.csv_feedback_string()
            # remove last newline
            if fb_str != "":
                fb_str = fb_str[:-1]
            return fb_str
        else:
            return config.NA
     
    def csv_points(self):
        if self.grade_status == GradeStatus.GRADED:
            points = self.act_points
        else:
            points = config.NA
        return points

    def short_rep(self):
        if hasattr(self, "name"):
            return "{} {} [{}] ({})".format(config.EXERCISE_BASENAME, self.number, self.name, self._grade_string())
        else:
            return "{} {} ({})".format(config.EXERCISE_BASENAME, self.number, self._grade_string())

    def _grade_string(self):
        grade_string = "not graded"
        if self.grade_status == GradeStatus.GRADED:
            grade_string = "{}/{} Points".format(self.act_points, self.max_points)
        elif self.grade_status == GradeStatus.PARTIALLY_GRADED:
            grade_string = "partially graded"
        return grade_string

    def long_rep(self):
        if hasattr(self, "name"):
            rep = "{} {} [{}] ({})\n\n".format(config.EXERCISE_BASENAME, self.number, self.name, self._grade_string())
        else:
            rep = "{} {} ({})\n\n".format(config.EXERCISE_BASENAME, self.number, self._grade_string())
        for a in self.answers:
            rep += a.rep(self.number, key=True)
        return rep

    def html_string(self, collapse=True):
        collapse = collapse and len(self.answers) == 1
        if hasattr(self, "name"):
            s = "<p>\n<b>{} {}</b> <i>({})</i><b>: {}&#8239;/&#8239;{}&#8202;P</b>".format(config.EXERCISE_BASENAME, self.number, self.name, self.act_points, self.max_points)
        else:
            s = "<p>\n<b>{} {}: {}&#8239;/&#8239;{}&#8202;P</b>".format(config.EXERCISE_BASENAME, self.number, self.act_points, self.max_points)
        if not collapse:
            s += "<ul>"
        for answer in self.answers:
            s += answer.html_string(self.number, collapse) + "\n"
        if not collapse:
            s += "</ul>"
        s += "</p>"
        return s


class Answer:
    def __init__(self, ans_num):
        self.num : int = ans_num
        self.deductions : Deductions = Deductions(ans_num)
        self.graded : bool = False

    def deduct(self, reason, points):
        self.deductions.add(reason, points)
        self.graded = True

    def mark_correct(self):
        self.deductions.clear()
        self.graded = True

    def html_string(self, ex_num, collapse=False):
        if collapse:
            return self.deductions.html_string(collapse)
        else:
            return "<li>{}.{}: {}</li>".format(ex_num, self.num, self.deductions.html_string(collapse))

    def feedback_string(self):
        return self.deductions.feedback_string()

    def csv_feedback_string(self):
        return self.deductions.csv_feedback_string()

    def rep(self, ex_num, key=False):
        repstr = ""
        if key:
            repstr += "\t[{}] ".format(magenta(self.num))
        grade_string = "not graded"
        if self.graded:
            grade_string = self.deductions.rep()
        repstr += "{}.{}: {}\n".format(ex_num, self.num, grade_string)
        return repstr


class Sheet:
    def __init__(self):
        self.exercises : Dict[int, Exercise] = {}
        self.remarks = Deductions(0)

    def html_string(self, collapse=True):
        s = ""
        # Collect feedback for all exercises
        for k in sorted(self.exercises.keys()):
            e = self.exercises[k]
            if e.max_points > 0:
                s += e.html_string(collapse) + "\n"

        # Calculate points
        max_points = sum([e.max_points for e in self.exercises.values()])
        reached_points = sum([e.act_points for e in self.exercises.values()])

        # Handle general remarks
        if self.remarks.deds:
            ded_points = self.remarks.deducted_points()
            if ded_points != 0:
                s += "<p><b>General Remarks: {}&#8202;P</b>\n".format(ded_points)
            else:
                s += "<p><b>General Remarks:</b>\n"
            s += self.remarks.html_string(collapse=True)
            s += "</p>\n"
            reached_points += ded_points
        s += "<p><b>Total: {}&#8239;/&#8239;{}&#8202;P</b></p>\n".format(reached_points, max_points)
        return s

    def print_html(self):
        print(self.html_string())

    def deduct(self, ex_num, answer_num, grade_text, deduction):
        if ex_num != 0:
            self.exercises[ex_num].deduct(answer_num, grade_text, deduction)
        else:
            # remarks (exercise 0)
            self.remarks.add(grade_text, deduction)

    def mark_correct(self, ex_num, ans_num):
        # do not consider remarks (exercise 0)
        if ex_num != 0:
            self.exercises[ex_num].mark_correct(ans_num)

    def range_points(self, mask=None):
        # calculate points for exercises
        max_points = sum([e.max_points for e in self.exercises.values() if mask is None or e.number in mask])
        act_points = sum([e.act_points for e in self.exercises.values() if mask is None or e.number in mask])
        # add remark points
        act_points += self.remarks.deducted_points()
        return act_points, max_points

    def grade_status(self, mask=None) -> GradeStatus:
        if mask is not None:
            exs = filter(lambda e: e.number in mask, self.exercises.values())
        else:
            exs = self.exercises.values()

        ex_status = list(map(lambda e: e.grade_status, exs))

        if all(s == GradeStatus.UNGRADED for s in ex_status):
            return GradeStatus.UNGRADED
        else:
            if all(s == GradeStatus.GRADED for s in ex_status):
                return GradeStatus.GRADED
            else:
                return GradeStatus.PARTIALLY_GRADED


class Deductions:
    def __init__(self, ans_num):
        self.deds = []
        self.ans_num = ans_num

    def add(self, reason, points):
        self.deds.append((reason, points))

    def feedback_string(self):
        s = ""
        if len(self.deds) == 0:
            s += "-{}: correct\n".format(self.ans_num)
        else:
            for d in self.deds:
                if d[1] == 0:
                    s += "-{}: {}\n".format(self.ans_num, d[0])
                else:
                    s += "-{}: {} ({:.2f}P)\n".format(self.ans_num, d[0], d[1])
            s = s[:-1]
        return s

    def csv_feedback_string(self):
        s = ""
        if len(self.deds) == 0:
            s += "@{}@0@correct\n".format(self.ans_num)
        else:
            for d in self.deds:
                s += "@{}@{:.2f}@{}\n".format(self.ans_num, d[1], d[0])
        return s

    def html_string(self, collapse=False):
        if len(self.deds) == 0:
            if collapse:
                return ""
            else:
                return "correct"
        elif len(self.deds) == 1:
            s = ""
            if collapse:
                s += "<ul><li>" 
            if self.deds[0][1] == 0:
                s += self.deds[0][0]
            else:
                s += "{} [{:.2f}&#8202;P]".format(self.deds[0][0], self.deds[0][1])
            if collapse:
                s += "</li></ul>"
            return s
        else:
            s = "<ul>\n"
            for d in self.deds:
                if d[1] == 0:
                    s += "<li>{}</li>".format(d[0])
                else:
                    s += "<li>{} [{:.2f}&#8202;P]</li>\n".format(d[0], d[1])
            s += "</ul>"
            return s

    def rep(self, show_correct=True):
        if len(self.deds) == 0:
            if show_correct:
                return "correct"
            else:
                return ""
        elif len(self.deds) == 1:
            if self.deds[0][1] == 0:
                return self.deds[0][0]
            else:
                return "{} ({:.2f}P)".format(self.deds[0][0], self.deds[0][1])
        else:
            s = "\n"
            for d in self.deds:
                if d[1] == 0:
                    s += "\t\t- {}\n".format(d[0])
                else:
                    s += "\t\t- {} ({:.2f}P)\n".format(d[0], d[1])
            s = s[:-1]
            return s

    def deducted_points(self):
        p = 0
        for d in self.deds:
            p += float(d[1])
        return p

    def clear(self):
        self.deds.clear()


class FrameEntry:
    def __init__(self, group, students, exercises):
        self.group : str = group
        self.students : List[str] = students
        self.sheet : Sheet = init_sheet(exercises)

    def parse_feedback(self, deds, ex_num, points, feedback, restore=False):
        if points != config.NA:
            for fb in feedback.split("\n"):
                for m in re.finditer(config.FEEDBACK_PATTERN, fb):
                    ans_num = m[1]
                    deduction = m[2]
                    grade_text = m[4]
                    if float(deduction) == 0 and re.match(r"\s*correct\s*", grade_text):
                        self.sheet.mark_correct(int(ex_num), int(ans_num))
                    else:
                        self.sheet.deduct(int(ex_num), int(ans_num), grade_text, float(deduction))
                        deds.add_entry(int(ex_num), int(ans_num), grade_text, float(deduction), increment=restore)

    def name_len(self):
        # +2 for brackets
        if config.GROUP_SIZE > 1:
            return len(", ".join(self.students))+2
        else:
            return 0

    def group_len(self):
        return len(self.group)

    def group_string(self, exercises : List[int]):
        if config.GROUP_SIZE > 1:
            student_str = ", ".join(self.students)
            student_str = "(" + student_str + ")"
        else:
            student_str = ""
        grade_status = self.sheet.grade_status(mask=exercises)
        if grade_status == GradeStatus.GRADED:
            act_points, max_points = self.sheet.range_points(exercises)
            grade_str = light_green("{}/{} Points".format(act_points, max_points))
        elif grade_status == GradeStatus.PARTIALLY_GRADED:
            grade_str = light_yellow("partially graded")
        elif grade_status == GradeStatus.UNGRADED:
            grade_str = light_red("ungraded")
        else:
            raise RuntimeError("invalid grade status observed")
        return "{0:<{group_len}} {1:<{name_len}} | {2}".format(self.group, student_str, grade_str, group_len=config.MAX_GROUP_LEN,
                                                               name_len=config.MAX_NAMES_LEN)


class Frame:
    def __init__(self, mask):
        # get specified csv files
        masked_exc = list(set(mask) & set(config.DEFAULT_MASK))
        potential_files = [config.CSV_BASENAME.format(i) for i in masked_exc]
        dir_contents = os.listdir()
        files = list(set(potential_files) & set(dir_contents))

        # set exercises
        self.exercises = sorted([int(re.search(config.CSV_PATTERN, f).group(1)) for f in files])
        dir_file_nums = set(int(re.search(config.CSV_PATTERN, f).group(1)) for f in filter(lambda s: re.match(config.CSV_PATTERN, s), dir_contents))

        # do not show general remarks if not all exercises are present
        if dir_file_nums & set(self.exercises) != dir_file_nums and config.REMARKS_PRESENT:
            print_info("Not all exercises are present, hiding general remarks") 
            config.REMARKS_PRESENT = False

        # check if exercises in deductions match current exercises
        # restore deductions if this is not the case or no deduction file exists
        restore_deds = not os.path.isfile(config.DEDUCTION_FILE)
        if os.path.isfile(config.DEDUCTION_FILE):
            ded_csv = pd.read_csv(config.DEDUCTION_FILE)
            if set(ded_csv["ex_num"]) != set(self.exercises):
                restore_deds = True
                print_info("Deduction file does not match current exercises, restoring")
                os.remove(config.DEDUCTION_FILE)
        else:
            print_info("No deduction file found, creating new one")

        if restore_deds:
            with open(config.DEDUCTION_FILE, "w") as f:
                f.write(config.DEDUCTIONS_FIRSTLINE)

        # check if remarks file exists and add to files list if present
        if config.REMARKS_PRESENT:
            files.append(config.REMARKS_FILE)
        
        # set deds and data
        self.deds = DeductionCollection()
        self.data : Dict[str, FrameEntry] = {}

        if config.AUTOSAVE_FILE in os.listdir():
            print_info("Restoring from autosave, delete \"{}\" if you want to start from scratch".format(
                config.AUTOSAVE_FILE))
            as_df = pd.read_csv(config.AUTOSAVE_FILE)
            if set(self.exercises) & set(as_df["exercise"]) != set(self.exercises):
                print_err("Autosave file does not contain the currently selected exercises. "
                          "Please save your current changes for exercises {} and "
                          "delete \"{}\".".format(list(set(as_df["exercise"])), config.AUTOSAVE_FILE))
                exit(1)

            as_df.fillna(config.NA, inplace=True)
            config.detect_group_size(as_df)
            for i, r in as_df.iterrows():
                group_name = r["group"]
                students = []
                for i in range(1,config.GROUP_SIZE+1):
                    s = r[config.STUDENT_FORMAT.format(i)]
                    if s != config.NA:
                         students.append(s)
                if group_name not in self.data.keys():
                    self.data[group_name] = FrameEntry(group_name, students, self.exercises)
                if r["exercise"] in self.exercises or (r["exercise"] == 0 and config.REMARKS_PRESENT):
                    self.data[group_name].parse_feedback(self.deds, r["exercise"], r["points"], r["feedback"], restore=restore_deds)
            self.csv_df = as_df

        else:
            print_info("No autosave found, starting from scratch.\n")
            # create data structure from first file
            df = pd.read_csv(files[0])
            df.fillna(config.NA, inplace=True)
            config.detect_group_size(df)
            for i, r in df.iterrows():
                group_name = r["group"]
                students = []
                for i in range(1,config.GROUP_SIZE+1):
                    s = r[config.STUDENT_FORMAT.format(i)]
                    if s != config.NA:
                        students.append(s)
                self.data[group_name] = FrameEntry(group_name, students, self.exercises)
                if r["exercise"] in self.exercises or (r["exercise"] == 0 and config.REMARKS_PRESENT):
                    self.data[group_name].parse_feedback(self.deds, r["exercise"], r["points"], r["feedback"], restore=restore_deds)
            self.csv_df = df

            # read other files
            for f in files[1:]:
                df = pd.read_csv(f)
                df.fillna(config.NA, inplace=True)
                for i, r in df.iterrows():
                    group_name = r["group"]
                    students = []
                    self.data[group_name].parse_feedback(self.deds, r["exercise"], r["points"], r["feedback"])
                self.csv_df = pd.concat([self.csv_df, df]) 
            self.csv_df.sort_values(["exercise", "group"], inplace=True)
                

    def update_feedback(self):
        def csv_feedback(row):
            if row["exercise"] in self.exercises:
                return self.data[row["group"]].sheet.exercises[row["exercise"]].csv_feedback()
            elif row["exercise"] == 0:
                # remarks
                return self.data[row["group"]].sheet.remarks.csv_feedback_string()

        def csv_points(row):
            if row["exercise"] in self.exercises:
                return self.data[row["group"]].sheet.exercises[row["exercise"]].csv_points()
            elif row["exercise"] == 0:
                # remarks
                return self.data[row["group"]].sheet.remarks.deducted_points()

        self.csv_df["feedback"] = self.csv_df.apply(csv_feedback, axis=1)
        self.csv_df["points"] = self.csv_df.apply(csv_points, axis=1)


    def write_csv_files(self):
        self.update_feedback()
        basename = config.CSV_BASENAME

        for e in self.exercises:
            # rename old file
            os.rename(basename.format(e), basename.format(e) + ".old")

            # save exercise files
            cf = self.csv_df[self.csv_df["exercise"] == e]
            cf.to_csv(basename.format(e), index=None)
        
        # save remarks file
        if config.REMARKS_PRESENT:
            os.rename(config.REMARKS_FILE, config.REMARKS_FILE + ".old")
            self.csv_df[self.csv_df["exercise"] == 0].to_csv(config.REMARKS_FILE, index=None)


    def autosave(self):
        self.update_feedback()

        self.csv_df.to_csv(config.AUTOSAVE_FILE, index=None)
        self.deds.write_csv()

    def ungraded_groups(self):
        return list(filter(lambda e: e.sheet.grade_status(mask=self.exercises) == GradeStatus.UNGRADED,
                           self.data.values()))

    def partial_groups(self):
        return list(
            filter(lambda e: e.sheet.grade_status(mask=self.exercises) == GradeStatus.PARTIALLY_GRADED,
                   self.data.values()))

    def graded_groups(self):
        return list(filter(lambda e: e.sheet.grade_status(mask=self.exercises) == GradeStatus.GRADED,
                           self.data.values()))


class DeductionCollection:
    def __init__(self):
        self.entries : List[DeductionEntry] = []
        with open(config.DEDUCTION_FILE, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for (i, line) in enumerate(reader):
                if i != 0:
                    ex_num = line[0]
                    ans_num = line[1]
                    reason = line[2]
                    points = line[3]
                    count = line[4]
                    self.new_entry(ex_num, ans_num, reason, points, count)

    def add_entry(self, ex_num, ans_num, reason, points, increment=False):
        found = False
        for e in self.entries:
            if e.ex_num == ex_num and e.ans_num == ans_num and \
                    e.reason == reason and e.points == points:
                found = True
                if increment:
                    e.increment_count()
                break
        if not found:
            self.new_entry(ex_num, ans_num, reason, points, 1)

    def new_entry(self, ex_num, ans_num, reason, points, count):
        self.entries.append(DeductionEntry(ex_num, ans_num, reason, points, count))

    def write_csv(self):
        with open(config.DEDUCTION_FILE, "w") as f:
            f.write(config.DEDUCTIONS_FIRSTLINE)
            for d in self.entries:
                f.write(d.csv_string())

    def get(self, ex_num: int, ans_num: int):
        deds = list(filter(lambda e: e.ex_num == ex_num and e.ans_num == ans_num, self.entries))
        deds.sort(key=lambda e: e.count, reverse=True)
        return deds

    def __str__(self):
        s = ""
        for d in self.entries:
            s += str(d) + "\n"
        return s


class DeductionEntry:
    def __init__(self, ex_num, ans_num, reason, points, count):
        self.ex_num = int(ex_num)
        self.ans_num = int(ans_num)
        self.reason = reason
        self.points = float(points)
        self.count = int(count)

    def increment_count(self):
        self.count += 1

    def csv_string(self):
        return "{},{},\"{}\",{},{}\n".format(self.ex_num, self.ans_num, self.reason, self.points, self.count)

    def __str__(self):
        return "{}.{}: {} ({} Points)".format(self.ex_num, self.ans_num, self.reason, self.points)


# ========== UTITLITY FUNCTIONS ========== #

def init_sheet(exercises: List[int]):
    sh = Sheet()

    for e in exercises:
        # config.EXERCISES ... exercises in JSON
        exc = config.EXERCISES.get(str(e))
        if exc is not None:
            sh.exercises[e] = Exercise(e, len(exc), sum(exc), name=config.EXERCISE_NAMES.get(str(e)))
    
    return sh


def parse_config(config_path, suffix, mask):
    # check whether json file exists
    if not os.path.exists(config_path):
        print_err("No configuration file found at \"{}\", exiting".format(config_path))
        exit(1)

    # parse json
    sheet_config = json.loads(open(config_path).read())  # load json
    
    if config.JSON_EXERCISES not in sheet_config:
        print_err("No exercises specified in configuration file, exiting")
        exit(1)

    if config.JSON_GROUPSIZE not in sheet_config:
        print_err("No group size specified in configuration file, exiting")
        exit(1)

    if config.JSON_SHEETNAME not in sheet_config:
        print_err("No sheet name specified in configuration file, exiting")
        exit(1)

    config.SHEETNAME = sheet_config[config.JSON_SHEETNAME]  # update sheet name
    if config.JSON_PDF_PATH in sheet_config:
        config.PDF_PATH = sheet_config[config.JSON_PDF_PATH] 
    if config.JSON_GROUPSIZE in sheet_config:
        config.GROUP_SIZE = int(sheet_config[config.JSON_GROUPSIZE])
    if config.JSON_EXERCISE_NAMES in sheet_config:
        config.EXERCISE_NAMES = sheet_config[config.JSON_EXERCISE_NAMES]
    if config.JSON_EXERCISE_BASENAME in sheet_config:
        config.EXERCISE_BASENAME = str(sheet_config[config.JSON_EXERCISE_BASENAME])

    config.CSV_BASENAME = config.SHEETNAME + config.CSV_BASENAME
    config.CSV_PATTERN = config.SHEETNAME + config.CSV_PATTERN
    config.AUTOSAVE_FILE = config.AUTOSAVE_FILE.format(config.SHEETNAME)
    config.DEDUCTION_FILE = config.DEDUCTION_FILE.format(config.SHEETNAME)
    config.REMARKS_FILE = config.REMARKS_FILE.format(config.SHEETNAME)

    if os.path.isfile(config.REMARKS_FILE):
        config.REMARKS_PRESENT = True

    # get exercise numbers from json
    config.EXERCISES = sheet_config[config.JSON_EXERCISES]

    # adapt suffix
    if suffix is not None:
        config.AUTOSAVE_FILE = suffix_string(config.AUTOSAVE_FILE, suffix)
        config.CSV_BASENAME = suffix_string(config.CSV_BASENAME, suffix)
        config.CSV_PATTERN = suffix_string(config.CSV_PATTERN, suffix)
    