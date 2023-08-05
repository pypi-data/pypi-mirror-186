#!python

"""
Creates summary page from RapidPE/RIFT results
"""

__author__ = "Vinaya Valsan"

import os
import sys
import ast

import subprocess as sp
import numpy as np

from tabulate import tabulate
from glob import glob
from argparse import ArgumentParser
from urllib.parse import urlparse
from rapidpe_rift_pipe.config import Config
from rapidpe_rift_pipe.profiling import write_css_file
from rapidpe_rift_pipe.utils import print_output


optp = ArgumentParser()
optp.add_argument("input_dir", help="path to event run dir")
optp.add_argument( "--web-dir", default=None, help="path to web dir")
optp.add_argument( "--output-dir", default=None, help="directory to save plots")
opts = optp.parse_args()
print("-----------Creating summary page--------------")
input_dir = opts.input_dir

if opts.web_dir:
    output_dir = opts.web_dir
else:
    output_dir = os.path.join(os.getenv("HOME"),f'public_html/RapidPE/{input_dir[input_dir.rfind("output/") + 7 :]}')
os.makedirs(output_dir, exist_ok=True)
write_css_file(output_dir,'stylesheet.css')

if opts.output_dir:
    run_dir = opts.output_dir
else:
    run_dir = input_dir
summary_plot_dir = run_dir + "/summary_plots/"

os.system(f"cp {summary_plot_dir}* {output_dir}/")
print(f"Summary page will be saved in {output_dir}")
index_html_file = output_dir + "/summarypage.html"

html_file = open(index_html_file, "w")


print_output(
    html_file,
    """
<html>
<head>
<link rel="stylesheet" href="stylesheet.css">
<script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>
</head>
""",
)

print_output(html_file, "<body>")
print_output(html_file, f"<h2>rundir = {run_dir}</h2>")
event_info_file = input_dir + "/event_info_dict.txt"
with open(event_info_file) as f:
    contents = f.read()
    dictionary = ast.literal_eval(contents)

print_output(html_file, "<h1> Event Info  </h1>")
print_output(
    html_file,
    f"""
snr = {dictionary["snr"]} <br>
approximant = {dictionary["approximant"]} <br>
intrinsic_param = {dictionary["intrinsic_param"]} <br>
event_time = {dictionary["event_time"]} <br>
""",
)

config = Config.load(input_dir + "/Config.ini")
is_event = config.event.mode in {"sid", "gid"}
if is_event:
    gracedb_url = urlparse(config.gracedb_url)
    if config.event.mode == "sid":
        event_id = config.event.superevent_id
        event_path = f"/superevents/{event_id}/view/"
    else:
        event_id = config.event.gracedb_id
        event_path = f"/events/{event_id}/view/"
    event_url = gracedb_url._replace(path=event_path).geturl()
    print_output(
        html_file, f'GraceDB url : <a href="{event_url}">{event_id}</a> <br>'
    )

filelist = glob(output_dir + "/grid*png")
print_output(html_file, "<h1> Grid Plots </h1>")
for fname_full in sorted(filelist):
    fname_split = fname_full.split("/")
    fname = fname_split[-1]
    print_output(html_file, f'<img src="{fname}">')

print_output(html_file, "<h1> Posterior Plots </h1>")
unique_sigma_strs = [f[f.find('sigma1'):-4] for f in glob(output_dir + "/posterior_mchirp*png")]
for sigma_str in unique_sigma_strs:
    split_str = sigma_str.replace('p','.').replace('_',' = ').split('-')
    print_output(html_file, f"<h2> standard deviation: {split_str[0]}*grid_size, {split_str[1]}*grid_size</h2>")
    filelist = glob(output_dir + f"/posterior*{sigma_str}.png")
    for fname_full in sorted(filelist):
        fname_split = fname_full.split("/")
        fname = fname_split[-1]
        print_output(html_file, f'<img src="{fname}">')

print_output(html_file, "<h1> Skymaps </h1>")
filelist = glob(output_dir + "/skymap*png")
for fname_full in sorted(filelist):
    fname_split = fname_full.split("/")
    fname = fname_split[-1]
    print_output(html_file, f"<br>{fname}")
    print_output(html_file, f'<img src="{fname}">')


print_output(html_file,"""<h1> Timing </h1> """)

if os.path.exists(f'{summary_plot_dir}/cprofile.html')==True:
    filelist = np.sort(glob(output_dir + "/cprofile*hist*png"))
    for fname_full in sorted(filelist):
        fname_split = fname_full.split("/")
        fname = fname_split[-1]
        print_output(html_file, f'<img src="{fname}">')


# Total job time:
condor_submit_time = int(dictionary["condor_submit_time"])
job_timing_file = input_dir + "/job_timing.txt"
iteration_completion_time = []
with open(job_timing_file) as f:
    lines = f.readlines()
    for line_id,line in enumerate(lines):
        line_split = line.split(" ")
        level_complete_time = float(line_split[1])
        iteration_completion_time.append(level_complete_time)
        if line_id==0:
            print_output(
                html_file,
                f'<br> <font size="+2"> iteration level {line_split[0]} took '
                f"{level_complete_time-condor_submit_time} s </font>",
            )
        else:
            print_output(
                html_file,
                f'<br> <font size="+2"> iteration level {line_split[0]} took '
                f"{level_complete_time-iteration_completion_time[line_id-1]} s </font>",
            )


print_output(html_file,"<br><a href='cprofile.html'>Detailed cProfile info for a single ILE job</a>")
print_output(html_file, "<h1> Config.ini </h1>")

with open(input_dir + "/Config.ini") as config_f:
    for line in config_f:
        if line[0] != "#" and len(line.strip()) > 0:
            if line[0] == "[":
                print_output(html_file, f"<br> <b> {line} </b>")
            else:
                print_output(html_file, f"<br> {line}")

print_output(html_file, "<h1> Convergence </h1>")
header = [
    "filename",
    " iteration",
    " Neff ",
    " sqrt(2*lnLmax)",
    " sqrt(2*lnLmarg)",
    " ln(Z/Lmax)",
    "int_var",
]
log_file_list = np.sort(glob(input_dir + "/logs/integrate*out"))
convergence_data = np.ones(len(log_file_list)).tolist()
for i, log_file in enumerate(log_file_list):
    with open(log_file, "r") as f:
        lines = f.readlines()
        last_line = lines[-1]
        if "Weight" in last_line:
            last_line = lines[-3]
        elif "neff" in last_line:
            last_line = lines[-3]
        log_filename = log_file.split("/")[-1]
        data_list = last_line.split(" ")[1:]
        data_list[0] = log_filename
        convergence_data[i] = data_list
print_output(
    html_file, tabulate(convergence_data, headers=header, tablefmt="html")
)

grep_out = sp.getoutput("ls *")
rescue_dags = glob(run_dir + "*rescue*")
failed_job_ids = []
if len(rescue_dags) != 0:
    print_output(html_file, "<h1> Failed Jobs</h1>")
    for i, dag in enumerate(rescue_dags):
        with open(dag, "r") as f:
            lines = f.readlines()
            number_of_nodes_failed = int(
                lines[7][len("# Nodes that failed: ") :]
            )
            list_of_nodes_failed = lines[8][len("#   ") :].split(",")[:-1]
        print_output(
            html_file,
            f"{len(list_of_nodes_failed)} jobs" f" failed in level {i} <br>",
        )
        failed_job_ids.extend(list_of_nodes_failed)
    print_output(html_file, "<h2> list of failed jobs </h2>")

    for j, dag_job in enumerate(failed_job_ids):
        cmd = f'grep "DAG Node: {dag_job}" {run_dir}logs/*log'
        grep_out = sp.getoutput(cmd)
        outfile_path = grep_out[: grep_out.find(".log")] + ".out"
        print_output(html_file, "<details>")
        print_output(
            html_file, f"<summary> {j+1}) Job ID: {dag_job} </summary>"
        )
        print_output(html_file, f"path: {outfile_path} <br>")
        print_output(html_file, "<pre>")
        with open(outfile_path, "r") as f:
            print_output(html_file, f.read())
        print_output(html_file, "</pre>")
        print_output(html_file, "</details>")
    print_output(html_file, "</details>")


# print_output(html_file,"""<table class="sortable">
#  <caption>
#    Students currently enrolled in WAI-ARIA 101
#    <span class="sr-only">, column headers with buttons are sortable.</span>
#  </caption>
#  <thead>
#    <tr>
#      <th>
#        <button>
#          First Name
#          <span aria-hidden="true"></span>
#        </button>
#      </th>
#      <th aria-sort="ascending">
#        <button>
#          Last Name
#          <span aria-hidden="true"></span>
#        </button>
#      </th>
#      <th>
#        <button>
#          Company
#          <span aria-hidden="true"></span>
#        </button>
#      </th>
#      <th class="no-sort">Address</th>
#      <th class="num">
#        <button>
#          Favorite Number
#          <span aria-hidden="true"></span>
#        </button>
#      </th>
#    </tr>
#  </thead>
#  <tbody>
#    <tr>
#      <td>Fred</td>
#      <td>Jackson</td>
#      <td>Canary, Inc.</td>
#      <td>123 Broad St.</td>
#      <td class="num">56</td>
#    </tr>
#    <tr>
#      <td>Sara</td>
#      <td>James</td>
#      <td>Cardinal, Inc.</td>
#      <td>457 First St.</td>
#      <td class="num">7</td>
#    </tr>
#    <tr>
#      <td>Ralph</td>
#      <td>Jefferson</td>
#      <td>Robin, Inc.</td>
#      <td>456 Main St.</td>
#      <td class="num">513</td>
#    </tr>
#    <tr>
#      <td>Nancy</td>
#      <td>Jensen</td>
#      <td>Eagle, Inc.</td>
#      <td>2203 Logan Dr.</td>
#      <td class="num">3.5</td>
#    </tr>
#  </tbody>
# </table>""")

print_output(html_file, "</body></html>")

html_file.close()
