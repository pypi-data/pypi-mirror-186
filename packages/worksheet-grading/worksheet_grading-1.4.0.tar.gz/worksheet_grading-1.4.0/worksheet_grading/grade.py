#!/usr/bin/env python

# stdlib imports
import argparse
import webbrowser
import subprocess
import statistics

# external imports
import readchar
import readline # overwrite input() for arrow key support

# local imports
from worksheet_grading.util import *
from worksheet_grading.gradelib import *
import worksheet_grading.config as config
from worksheet_grading.__init__ import __version__, __program__
from typing import Optional

# ========== COMMAND LINE LOGIC ========== #

class State:
    def __init__(self, frame: Frame):
        self.frame : Frame = frame
        self.sel_remarks : bool = False
        self.sel_method : Optional[function] = None
        self.page_groups : Optional[str] = None
        self.selection : Optional[int] = None
        self.page : Optional[int] = None
        self.ex_num : Optional[int] = None
        self.ans_num : Optional[int] = None
        self.ded_page : Optional[int] = None
        self.deds : Optional[List[DeductionEntry]] = None
        self.selected_group : Optional[FrameEntry] = None
        self.selected_exc : Optional[Exercise] = None
        self.cur_ded : Optional[DeductionEntry] = None
        self.last_rem_ded : Optional[List[DeductionEntry]] = None


def group_overview(frame: Frame):
    ungraded_groups = frame.ungraded_groups()
    graded_groups = frame.graded_groups()
    partial_groups = frame.partial_groups()

    strings = ["Graded:", "Partially Graded:", "Ungraded:"]
    max_len = max(map(len, strings))

    return "Found {0} groups: \n\t{1:<{max_len}} {2:>{max_len}}\n\t" \
           "{3:<{max_len}} {4:>{max_len}}\n\t{5:<{max_len}} {6:>{max_len}}\n" \
        .format(
            bright(len(frame.data.values())),
            strings[0],
            light_green(len(graded_groups)),
            strings[1],
            light_yellow(len(partial_groups)),
            strings[2],
            light_red(len(ungraded_groups)),
            max_len=max_len,
        )


def clear_terminal():
    print("\033c", end="")


def handle_action(state: State, actions, message, prompt_string=None):
    keys = []
    descriptions = []
    methods = []

    create_prompt_string = prompt_string is None

    # prepare lists and prompt
    action_format = "{} [{}]"
    if create_prompt_string:
        prompt_string = ""
    for a in actions:
        k, d, m = a
        keys.append(k)
        descriptions.append(d)
        methods.append(m)
        if create_prompt_string:
            prompt_string += action_format.format(d, magenta(k))
            prompt_string += "  "

    c = None
    while c is None:
        print(message, end="")

        print()
        print(prompt_string)
        c = readchar.readkey()

        # standard key bindings
        if c == readchar.key.CTRL_C:
            state.frame.autosave()
            exit(0)

        clear_terminal()

        matching = []
        for k in keys:
            if c in k:
                matching.append(k)
        if len(matching) > 0:
            methods[keys.index(matching[0])](state)
        else:
            ch = c if c.isalnum() else c.encode()
            print("\nUnknown option: \"{}\"\n".format(ch))
            c = None

    return c


def menu(frame: Frame):
    while True:
        message = "\n" + bright(light_blue("{} V{}".format(__program__, __version__))) + "\n\n"
        message += group_overview(frame)
        actions = [
            ("g", "Quick Grade", act_quick_grade),
            ("s", "Search a group", act_search_group),
            ("a", "Show all groups", act_all_groups),
            ("w", "Write to CSV files", act_write_output),
            ("c", "Check deductions", act_sanity_check),
            ("t", "Statistics", act_statistics),
            ("x", "Exit", act_exit),
        ]
        state = State(frame)
        handle_action(state, actions, message)


def select_group(state: State, groups):
    if len(groups) == 0:
        print(red("No matching group found\n"))
    elif len(groups) == 1:
        state.page_groups = groups
        state.selection = 0
        act_group_view(state)
        state.selection = None
        state.page_groups = None
    else:
        group_selection_view(state, groups)


def group_selection_view(state: State, groups):
    if not hasattr(state, "page") or state.page is None:
        state.page = 0

    actions = [
        ("1", "Select Group 1", act_sel_1),
        ("2", "Select Group 2", act_sel_2),
        ("3", "Select Group 3", act_sel_3),
        ("4", "Select Group 4", act_sel_4),
        ("5", "Select Group 5", act_sel_5),
        ("n" + readchar.key.RIGHT, "Next Page", act_next_page),
        ("p" + readchar.key.LEFT, "Previous Page", act_previous_page),
        ("b", "Back", act_back)
    ]
    while True:
        state.sel_method = act_group_view

        first_index = state.page * 5 % len(groups)
        state.page_groups = []
        message = bright("Select a group:\n\n")

        # compute max lens
        reset_max_lens()
        for i in range(5):
            index = (first_index + i) % len(groups)
            state.page_groups.append(groups[index])
            update_max_lens(groups[index].group_len(), groups[index].name_len())

        for i in range(5):
            new_group_str = "\t[{}] {}\n".format(magenta(i + 1), state.page_groups[i].group_string(state.frame.exercises))
            message += new_group_str

        message += dim("\n\tShowing entries {}-{} of {}\n".format(first_index + 1,
                                                                  (((first_index + 4) % len(groups)) + 1), len(groups)))

        prompt_string = "Select Group [{}]  Next page [{}]  Previous page [{}]  Back [{}]" \
            .format(
                magenta("1") + "-" + magenta("5"),
                magenta("n") + ", " + magenta(config.RIGHT_ARROW),
                magenta("p") + ", " + magenta(config.LEFT_ARROW),
                magenta("b")
            )
        act = handle_action(state, actions, message, prompt_string=prompt_string)
        if act == "b":
            break

    state.page = None
    state.page_groups = None
    state.sel_method = None


# ========== ACTIONS ========== #

def act_exit(state: State):
    state.frame.autosave()
    exit(0)


def act_quick_grade(state: State):
    groups = state.frame.partial_groups()
    groups.extend(state.frame.ungraded_groups())
    if len(groups) == 0:
        print("All groups are graded\n")
    else:
        select_group(state, groups[0:1])


def act_write_output(state: State):
    print("Writing data to csv files and renaming existing csv files to FILENAME.old")
    state.frame.write_csv_files()
    print("Successfully wrote data to csv files")


def act_sel_1(state: State):
    state.selection = 0
    state.sel_method(state)
    state.selection = None


def act_sel_2(state: State):
    state.selection = 1
    state.sel_method(state)
    state.selection = None


def act_sel_3(state: State):
    state.selection = 2
    state.sel_method(state)
    state.selection = None


def act_sel_4(state: State):
    state.selection = 3
    state.sel_method(state)
    state.selection = None


def act_sel_5(state: State):
    state.selection = 4
    state.sel_method(state)
    state.selection = None


def act_sel_6(state: State):
    state.selection = 5
    state.sel_method(state)
    state.selection = None


def act_sel_7(state: State):
    state.selection = 6
    state.sel_method(state)
    state.selection = None


def act_sel_8(state: State):
    state.selection = 7
    state.sel_method(state)
    state.selection = None


def act_sel_9(state: State):
    state.selection = 8
    state.sel_method(state)
    state.selection = None


def act_sel_10(state: State):
    state.selection = 9
    state.sel_method(state)
    state.selection = None


def act_sel_11(state: State):
    state.selection = 10
    state.sel_method(state)
    state.selection = None


def act_sel_12(state: State):
    state.selection = 11
    state.sel_method(state)
    state.selection = None


def act_sel_13(state: State):
    state.selection = 12
    state.sel_method(state)
    state.selection = None


def act_sel_14(state: State):
    state.selection = 13
    state.sel_method(state)
    state.selection = None


def act_sel_15(state: State):
    state.selection = 14
    state.sel_method(state)
    state.selection = None


def act_back(_):
    # NO OPERATION
    return


def act_next_page(state: State):
    if state.page is None:
        state.page = 1
    else:
        state.page += 1


def act_previous_page(state: State):
    if state.page is None:
        state.page = 0
    else:
        state.page -= 1


def act_next_exc(state: State):
    if state.ex_num is None:
        state.ex_num = min(state.frame.exercises)
    else:
        state.ex_num = get_next(state.ex_num, state.frame.exercises)
        if state.ex_num is None:
            state.ex_num = max(state.frame.exercises)+1


def act_previous_exc(state: State):
    if state.ex_num is None:
        state.ex_num = 0
    else:
        state.ex_num = get_prev(state.ex_num, state.frame.exercises)
        if state.ex_num is None:
            state.ex_num = 0


def act_next_ans(state: State):
    if state.ans_num is None:
        state.ans_num = 1
    else:
        state.ans_num += 1
    state.ded_page = 0


def act_previous_ans(state: State):
    if not hasattr(state, "ans_num") or state.ans_num is None:
        state.ans_num = 0
    else:
        state.ans_num -= 1
    state.ded_page = 0


def act_all_groups(state: State):
    groups = list(state.frame.data.values())
    select_group(state, groups)


def act_search_group(state: State):
    name = input("Enter search string: ").lower()
    clear_terminal()
    matching_groups = list(
        filter(lambda e: name in e.group.lower() or any(name in s.lower() for s in e.students),
               state.frame.data.values()))
    select_group(state, matching_groups)


def act_previous_deds(state: State):
    if state.ded_page is None:
        state.ded_page = 0
    else:
        if state.ded_page > 0:
            state.ded_page -= 1


def act_next_deds(state: State):
    if state.ded_page is None:
        state.ded_page = 1
    else:
        if (state.ded_page + 1) * 5 < len(state.deds):
            state.ded_page += 1


def act_open_pdf(state: State):
    pdf = config.PDF_PATH + state.selected_group.group.replace("/", "") + ".pdf"
    if not os.path.isfile(pdf):
        print("No such file: " + pdf + "\n")
    else:
        webbrowser.open_new("file://" + os.getcwd() + "/" + pdf)


def act_open_pdf_viewer(state: State):
    pdf = config.PDF_PATH + state.selected_group.group.replace("/", "") + ".pdf"
    if not os.path.isfile(pdf):
        print("No such file: " + pdf + "\n")
    else:
        for viewer in config.PDF_VIEWERS:
            cmd = "which " + viewer + " | grep -o " + viewer + " > /dev/null && echo '0' || echo '1'"
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p.wait()
            if output == b'0\n':
                subprocess.Popen([viewer, pdf], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return

        print("Either no supported pdf viewer or 'which' not installed, list of supported pdf viewers:")
        print(*config.PDF_VIEWERS, sep=", ")
        print("\n")


def act_mark_correct(state: State):
    state.selected_exc.answers[state.ans_num].mark_correct()
    act_next_ans(state)


def act_new_ded(state: State):
    print(bright("Add new deduction (cancel with EOF)"), end="\n\n")
    try:
        reason = input("Enter reason for deduction: ").replace("\"", "'")
        while True:
            points = input("Enter points that should be deducted: ")
            try:
                parsed_points = float(points)
                if parsed_points > 0:
                    parsed_points = -parsed_points
                break
            except ValueError:
                print("Invalid floating point number {}".format(points))
        state.frame.deds.add_entry(state.ex_num, state.ans_num + 1, reason, parsed_points)
        if not state.sel_remarks:
            state.selected_exc.deduct(state.ans_num + 1, reason, parsed_points)
        else:
            state.selected_group.sheet.remarks.add(reason, parsed_points)
        clear_terminal()
    except EOFError:
        clear_terminal()


def act_ded_scroll_up(state: State):
    state.cur_ded = max(0, state.cur_ded-1)


def act_ded_scroll_down(state: State):
    if state.sel_remarks:
        state.cur_ded = min(state.cur_ded+1, len(state.selected_group.sheet.remarks.deds)-1)
    else:
        state.cur_ded = min(state.cur_ded+1, len(state.selected_exc.answers[state.ans_num].deductions.deds)-1)


def act_del_ded(state: State):
    if not state.sel_remarks:
        state.last_rem_ded.append((state.selected_exc.answers[state.ans_num].deductions.deds[state.cur_ded], state.cur_ded))
        state.selected_exc.answers[state.ans_num].deductions.deds.pop(state.cur_ded)
    else:
        state.last_rem_ded.append((state.selected_group.sheet.remarks.deds[state.cur_ded], state.cur_ded))
        state.selected_group.sheet.remarks.deds.pop(state.cur_ded)


def act_undo_last_ded_rem(state: State):
    if len(state.last_rem_ded) == 0:
        print(red("Nothing to undo\n"))
        return
    dc, di = state.last_rem_ded[-1]
    if not state.sel_remarks:
        state.selected_exc.answers[state.ans_num].deductions.deds.insert(di, dc)
    else:
        state.selected_group.sheet.remarks.deds.insert(di, dc)
    state.last_rem_ded.pop()


def act_rem_ded(state: State):
    deds = state.selected_exc.answers[state.ans_num].deductions.deds if not state.sel_remarks else \
        state.selected_group.sheet.remarks.deds
    if len(deds) == 0:
        print(bright(red("No deductions found to remove")), end="\n\n")
        return
    state.cur_ded = 0
    state.last_rem_ded = []
    actions = [
        (readchar.key.UP, "Scroll up", act_ded_scroll_up),
        (readchar.key.DOWN, "Scroll down", act_ded_scroll_down),
        ("r"+readchar.key.ENTER, "Remove", act_del_ded),
        ("u", "Undo", act_undo_last_ded_rem),
        ("b", "Back", act_back),
    ]
    prompt_string = "Scroll [{},{}]  Remove selected [{}]  Undo last removal [{}]  Back [{}]" \
        .format(
            magenta(config.UP_ARROW),
            magenta(config.DOWN_ARROW),
            magenta("r") + ", " + magenta(config.ENTER_ARROW),
            magenta("u"),
            magenta("b"),
        )


    while True:
        message = bright("Remove deductions") + "\n\n"
        for i, (ds, dp) in enumerate(deds):
            ded_str = f"\t- {ds} ({dp} P)\n"
            if i == state.cur_ded:
                message += highlight(ded_str)
            else:
                message += ded_str
        act = handle_action(state, actions, message, prompt_string)
        if act == "b":
            break
    
    state.frame.autosave()


def act_deduct_selected(state: State):
    if state.ded_page * 5 + state.selection < len(state.deds):
        ded = state.deds[state.ded_page * 5 + state.selection]
        if state.sel_remarks:
            state.selected_group.sheet.remarks.add(ded.reason, ded.points)
        else:
            state.selected_exc.deduct(state.ans_num + 1, ded.reason, ded.points)
        ded.increment_count()


def act_remarks(state: State):
    state.sel_remarks = True
    state.ex_num = min(state.frame.exercises)
    state.selection = -1
    act_ans_view(state)
    state.frame.autosave()
    state.selection = None
    state.ex_num = None
    state.sel_remarks = False


def act_ans_view(state: State):
    if not state.sel_remarks and state.selection >= len(state.selected_exc.answers):
        print("invalid answer selection ({})\n".format(state.selection + 1))
        return

    state.ded_page = 0

    actions = [
        ("1", "Select Deduction 1", act_sel_1),
        ("2", "Select Deduction 2", act_sel_2),
        ("3", "Select Deduction 3", act_sel_3),
        ("4", "Select Deduction 4", act_sel_4),
        ("5", "Select Deduction 5", act_sel_5),
        (readchar.key.UP, "Previous deds", act_previous_deds),
        (readchar.key.DOWN, "Next deds", act_next_deds),
        ("d", "Add new deduction", act_new_ded),
        ("r", "Remove deduction", act_rem_ded),
        ("b", "Back", act_back)
    ]
    prompt_string = "Choose Deduction [{}]  Add new deduction [{}]  Scroll Common Deductions [{}]" \
        .format(
            magenta("1") + "-" + magenta("5"),
            magenta("d"),
            magenta(config.UP_ARROW) + ", " + magenta(config.DOWN_ARROW),
        )
    if not state.sel_remarks:
        prompt_string = "Mark as correct [{}]  ".format(magenta("c")) + prompt_string
        prompt_string += "\nNext Subexercise [{}]  Previous Subexercise [{}]".format(
            magenta("n") + ", " + magenta(config.RIGHT_ARROW),
            magenta("p") + ", " + magenta(config.LEFT_ARROW)
        )
        actions.extend([
            ("c", "Mark as correct", act_mark_correct),
            ("n" + readchar.key.RIGHT, "Next", act_next_ans),
            ("p" + readchar.key.LEFT, "Previous", act_previous_ans)
        ])
    prompt_string += "  Remove Deduction [{}]  Back [{}]".format(
            magenta("r"),
            magenta("b")
    )

    state.ans_num = state.selection
    state.deds = state.frame.deds.get(state.ex_num, state.ans_num + 1)
    while True:
        if not state.sel_remarks:
            # selected exercise

            # switching logic
            if state.ans_num + 1 > len(state.selected_exc.answers):
                if state.ex_num == max(state.frame.exercises):
                    return
                else:
                    state.ans_num = 0
                    state.ex_num = get_next(state.ex_num, state.frame.exercises)
                    state.selected_exc = state.selected_group.sheet.exercises[state.ex_num]
                    state.frame.autosave()
            if state.ans_num < 0:
                if state.ex_num == min(state.frame.exercises):
                    return
                else:
                    state.ex_num = get_prev(state.ex_num, state.frame.exercises)
                    state.ans_num = len(state.selected_group.sheet.exercises[state.ex_num].answers) - 1
                    state.selected_exc = state.selected_group.sheet.exercises[state.ex_num]
                    state.frame.autosave()

            state.deds = state.frame.deds.get(state.ex_num, state.ans_num + 1)
            answer = state.selected_exc.answers[state.ans_num]

            message = state.selected_group.group_string(state.frame.exercises) + "\n" + bright(state.selected_exc.short_rep()) + "\n\n"
            message += "Subexercise " + answer.rep(state.ex_num)
        else:
            # general remarks selected
            remarks = state.selected_group.sheet.remarks
            feedback = remarks.rep(show_correct=False)
            message = state.selected_group.group_string(state.frame.exercises) + "\n\n" + "General Remarks: " + ("None" if len(feedback) == 0 else feedback) + "\n"

        state.sel_method = act_deduct_selected

        if len(state.deds) == 0:
            message += "\nNo deductions found\n"
        else:
            message += "\nCommon Deductions:\n"
            first_ded = state.ded_page * 5
            last_ded = min((state.ded_page + 1) * 5, len(state.deds))
            j = 1
            for i in range(first_ded, last_ded):
                message += "\t[{}] {} ({:.2f}P)\n".format(magenta(j), state.deds[i].reason, state.deds[i].points)
                j += 1

        act = handle_action(state, actions, message, prompt_string=prompt_string)
        if act == "b":
            break

    state.ded_page = None
    state.deds = None
    state.ans_num = None


def act_exercise_view(state: State):
    if state.selection not in range(len(state.frame.exercises)):
        print_err("invalid exercise selection ({})\n".format(state.selection+1))
        return

    actions = [
        ("1", "Select Subexercise 1", act_sel_1),
        ("2", "Select Subexercise 2", act_sel_2),
        ("3", "Select Subexercise 3", act_sel_3),
        ("4", "Select Subexercise 4", act_sel_4),
        ("5", "Select Subexercise 5", act_sel_5),
        ("6", "Select Subexercise 6", act_sel_6),
        ("7", "Select Subexercise 7", act_sel_7),
        ("8", "Select Subexercise 8", act_sel_8),
        ("9", "Select Subexercise 9", act_sel_9),
        ("n" + readchar.key.RIGHT, "Next", act_next_exc),
        ("p" + readchar.key.LEFT, "Previous", act_previous_exc),
        ("b", "Back", act_back)
    ]
    prompt_string = "Select Subexercise [{}]  Next [{}]  Previous [{}]  Back [{}]" \
        .format(
            magenta("1") + "-" + magenta("9"),
            magenta("n") + ", " + magenta(config.RIGHT_ARROW),
            magenta("p") + ", " + magenta(config.LEFT_ARROW),
            magenta("b")
        )

    exercises = state.selected_group.sheet.exercises

    state.ex_num = state.frame.exercises[state.selection] 
    while True:
        # if state.ex_num + 1 > state.frame.last_ex or state.ex_num + 1 < state.frame.first_ex:
        #     return

        # check if we are at the end of valid exercises
        if max(state.frame.exercises) < state.ex_num or min(state.frame.exercises) > state.ex_num:
            return

        exc = exercises[state.ex_num]
        message = state.selected_group.group_string(state.frame.exercises) + "\n\n"
        message += exc.long_rep()
        state.selected_exc = exc

        state.sel_method = act_ans_view
        act = handle_action(state, actions, message, prompt_string=prompt_string)
        if act == "b":
            state.frame.autosave()
            break


def act_group_view(state: State):
    selected_group : FrameEntry = state.page_groups[state.selection % len(state.page_groups)]
    reset_max_lens()
    update_max_lens(selected_group.group_len(), selected_group.name_len())
    sheet = selected_group.sheet

    state.selected_group = selected_group

    actions = [
        ("1", "Select Exercise 1", act_sel_1),
        ("2", "Select Exercise 2", act_sel_2),
        ("3", "Select Exercise 3", act_sel_3),
        ("4", "Select Exercise 4", act_sel_4),
        ("5", "Select Exercise 5", act_sel_5),
        ("6", "Select Exercise 6", act_sel_6),
        ("7", "Select Exercise 7", act_sel_7),
        ("8", "Select Exercise 8", act_sel_8),
        ("9", "Select Exercise 9", act_sel_9),
        ("A", "Select Exercise 10", act_sel_10),
        ("B", "Select Exercise 11", act_sel_11),
        ("C", "Select Exercise 12", act_sel_12),
        ("D", "Select Exercise 13", act_sel_13),
        ("E", "Select Exercise 14", act_sel_14),
        ("F", "Select Exercise 15", act_sel_15),
        ("g", "General Remarks", act_remarks),
        ("o", "Open PDF (Browser)", act_open_pdf),
        ("v", "Open PDF Viewer", act_open_pdf_viewer),
        ("b", "Back", act_back),
    ]
    prompt_string = "Select Exercise [" + magenta("1") + "-" + magenta("9") + ", " + magenta("A") + "-" + \
        magenta("F") + "]"
    if config.REMARKS_PRESENT:
        actions.append(("g", "General Remarks", act_ans_view))
        prompt_string += "  General Remarks [" + magenta("g") + "]"
    prompt_string += "  Open PDF (Browser) [" + magenta("o") + "]  Open PDF Viewer [" + \
        magenta("v") + "]  Back [" + magenta("b") + "]"

    while True:
        message = selected_group.group_string(state.frame.exercises) + "\n\n"
        i = 1
        for e in state.frame.exercises:
            message += "\t[{}] {}\n".format(magenta(hex(i)[2:].upper()), sheet.exercises[e].short_rep())
            i += 1
        if config.REMARKS_PRESENT:
            message += "\n\t[{}] {}\n".format(magenta("g"), f"General remarks ({'None' if not sheet.remarks.deds else str(sheet.remarks.deducted_points())+' Points'})")
        state.sel_method = act_exercise_view
        act = handle_action(state, actions, message, prompt_string=prompt_string)
        if act == "b":
            state.frame.autosave()
            break

    state.sel_method = None
    state.selected_group = None


def act_sanity_check(state: State):
    points = sc_points()
    sane = True
    for e in state.frame.data.values():
        for ex in e.sheet.exercises.values():
            for a in ex.answers:
                if a.deductions.deducted_points() < -1 * points[ex.number][a.num - 1]:
                    print(red("Invalid deduction found for group \"{}\" exercise {}.{}").format(e.group,
                                                                                                ex.number, a.num))
                    sane = False

    if not sane:
        print()
        print(red("Invalid deductions found, see above output"))
    else:
        print(green("No invalid deductions found"))
    

def act_statistics(state: State):
    stat_frame = state.frame.csv_df
    groups = state.frame.data.keys()
    stat_pts = []
    for g in groups:
        if state.frame.data[g].sheet.grade_status() == config.GRADED:
            stat_pts.append(stat_frame[stat_frame.group == g]["points"].sum())

    try:
        mean = statistics.mean(stat_pts)
        stdev = statistics.stdev(stat_pts)
        median = statistics.median(stat_pts)
        print(bright("Statistics of graded exercises:"))
        print(f"    Mean: \t{mean:.2f}".expandtabs(16))
        print(f"    Stdev: \t{stdev:.2f}".expandtabs(16))
        print(f"    Median: \t{median:.2f}".expandtabs(16))
        print(f"    Min: \t{min(stat_pts)}".expandtabs(16))
        print(f"    Max: \t{max(stat_pts)}".expandtabs(16))
    except statistics.StatisticsError:
        print(red("Failed to retrieve statistics (possibly too few data points)"))


# ========== UTILITY ========== #

def update_max_lens(group_len, name_len):
    config.MAX_GROUP_LEN = max(config.MAX_GROUP_LEN, group_len)
    config.MAX_NAMES_LEN = max(config.MAX_NAMES_LEN, name_len)


def reset_max_lens():
    config.MAX_GROUP_LEN = 0
    config.MAX_NAMES_LEN = 0


# Points for sanity check
def sc_points():
    points = []
    for i in config.DEFAULT_MASK:
        exc = config.EXERCISES.get(str(i))
        if exc is not None:
            points.append(exc)
    return points

# ========== MAIN ========== #

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(__program__, description="Interactive exercise grading tool", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-e', '--exercises', default="{}-{}".format(config.DEFAULT_FIRSTEX, config.DEFAULT_LASTEX),
                        help="Exercises that should be considered, must either be a range (e.g., 1-5), comma-separated list (1,4,6) or single exercise (e.g., 3)")
    parser.add_argument('-s', '--suffix', help="File suffix for considered csv files", type=str)
    parser.add_argument('-c', '--config', default="config.json", help="Config file for the sheet data", type=str)
    parser.add_argument('--no-color', action="store_false", help="Turn off colored terminal output")
    parser.add_argument('--version', action="version", help="Display version and license information", version=version_string(__program__))
    args = parser.parse_args()

    # set color mode according to argument
    set_color(args.no_color)

    try:
        mask = list(parse_int_list(args.exercises))
    except ValueError:
        print_err("Invalid exercise range \"{}\"".format(args.exercises))
        exit(1)

    if min(mask) < 1 or max(mask) > 15:
        print_err("Exercises must be between 1 and 15, exiting")
        exit(1)

    # check whether json file exists
    if not os.path.exists(args.config):
        print_err("No configuration file found at path \"{}\", exiting".format(args.config))
        exit(1)

    # parse json and update globals
    parse_config(args.config, args.suffix, mask)

    # Create Frame
    f = Frame(mask)

    f.autosave()

    # Start main menu
    menu(f)


if __name__ == "__main__":
    main()
