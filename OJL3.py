import os
import subprocess

OJL3_DIR = os.path.dirname(os.path.abspath(__file__))
SANDBOX_PATH = os.path.join(OJL3_DIR, "OJ_sandbox")
SAFEEXEC_PATH = os.path.join(OJL3_DIR, "safeexec")
INPR_PATH = os.path.join(OJL3_DIR, "inprs")

SAFEEXEC_ARGS = ["--gid", "10000", "--nproc", "30"]

def run_script(inpr_path, source_path, in_path=None, inpr_options=None, report_path=None, time_lim_s=10, mem_lim_k=50000):
	if not inpr_options:
		inpr_options = []
	cmdline = [inpr_path] + inpr_options + [source_path]

	if report_path:
		report_args = ["--report_file", os.path.abspath(report_path)]
	else:
		report_args = []

	run_path = [SAFEEXEC_PATH] + SAFEEXEC_ARGS + ["--clock", str(time_lim_s), "--mem", str(mem_lim_k)] + report_args + ["--exec"] + cmdline

	if in_path: file_obj = open(in_path)
	else: file_obj = None

	sp = subprocess.Popen(run_path, stdin=file_obj, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	(out,err) = sp.communicate()
	return (sp.returncode, out, err)
