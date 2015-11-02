import os
import subprocess

OJL3_DIR = os.path.dirname(os.path.abspath(__file__))
SANDBOX_PATH = os.path.join(OJL3_DIR, "OJ_sandbox")
SAFEEXEC_PATH = os.path.join(OJL3_DIR, "safeexec")
INPR_PATH = os.path.join(OJL3_DIR, "inprs")

SAFEEXEC_ARGS = ["--gid", "10000", "--nproc", "5"]

def run_prog(inpr_path, source_path, in_path=None, cmd_options=None, exec_path=None, report_path=None, time_lim_s=10, mem_lim_k=80000):
	# if inpr_path is None, source_path will be treated as an executable
	if not cmd_options:
		cmd_options = []
	if inpr_path:
		cmdline = [inpr_path] + cmd_options + [source_path]
	else:
		cmdline = [source_path] + cmd_options

	if report_path:
		report_args = ["--report_file", os.path.abspath(report_path)]
	else:
		report_args = []

	run_path = [SAFEEXEC_PATH] + SAFEEXEC_ARGS + ["--clock", str(time_lim_s), "--mem", str(mem_lim_k)] + report_args + ["--exec"] + cmdline

	if in_path: file_obj = open(in_path)
	else: file_obj = None

	sp = subprocess.Popen(run_path, stdin=file_obj, cwd=exec_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	(out,err) = sp.communicate()
	verdict, time_s, mem_k = parse_report(open(report_path).read())
	return (verdict, out, err, time_s, mem_k)

def parse_report(report_text):
	report_lines = report_text.strip().split('\n')
	if report_lines[0] == "OK":
		verdict = "OK"
	elif report_lines[0] == "Time Limit Exceeded":
		verdict = "TLE"
	elif report_lines[0].startswith("Command exited with non-zero status"):
		verdict = "NZEC"
	elif report_lines[0].startswith("Command terminated by signal"):
		verdict = report_lines[0].rsplit(maxsplit=1)[1][:-1]
	else:
		raise Exception("Unknown verdict "+report_lines[0])
	mem_k = int(report_lines[2].split()[2])
	time_s = float(report_lines[3].split()[2])
	return (verdict, time_s, mem_k)
