#!/usr/bin/python3

"""This module defines functions which take in the source code path, destination directory and language name, compile the code into a program in the destination directory and returns the command line to run the program"""
import subprocess
import shutil
import os

GCC_PATH = "/usr/bin/gcc"
GPP_PATH = "/usr/bin/g++"
JAVAC_PATH = "/usr/bin/javac"
JAVA_PATH = "/usr/bin/java"

OJL3_DIR = os.path.dirname(os.path.abspath(__file__))
INPRS_PATH = os.path.join(OJL3_DIR, "inprs")

"""
Functions of the form compiler_<language>:

They take 2 parameters:
source_path - path to source code
dest_dir_path - path to directory where compiled program will be stored
The compiled program might have any name.
If the program is not meant to be compiled, it is simply copied to dest_dir_path

These functions return a tuple (success, out, prog_path, prog_type)
success is True if compilation was successful, otherwise false
out contains output of the compiler (both stdout and stderr). It usually consists of error messages or warnings.
prog_path is the path to the resulting compiled program
"""

def compile_c_or_cpp(source_path, dest_dir_path, compiler_path, compiler_options=None):
	if not compiler_options:
		compiler_options = []
	file_name_wo_ext = os.path.splitext(os.path.basename(source_path))[0]
	dest_path = os.path.join(dest_dir_path, file_name_wo_ext)
	sp = subprocess.Popen([compiler_path, source_path] + compiler_options + ["-o", dest_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
	(out, err) = sp.communicate()
	return (sp.returncode==0, out, dest_path)

def compile_c(source_path, dest_dir_path):
	return compile_c_or_cpp(source_path, dest_dir_path, GCC_PATH)
def compile_cpp(source_path, dest_dir_path):
	return compile_c_or_cpp(source_path, dest_dir_path, GPP_PATH)

def compile_java(source_path, dest_dir_path):
	dest_fname = "Main.class"
	dest_path = os.path.join(dest_dir_path, dest_fname)
	sp = subprocess.Popen([JAVAC_PATH, source_path, "-d", dest_dir_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
	(out, err) = sp.communicate()
	dest_file_exists = os.path.isfile(dest_path)
	success = sp.returncode==0 and dest_file_exists
	if sp.returncode==0 and not dest_file_exists and not out:
		out = "Could not find "+dest_fname
	return (success, out, dest_path)

no_compiler_langs = {"python2", "python3", "bash", "java_bytecode"}
# set of languages which are not compiled

def compile_none(source_path, dest_dir_path):
	# Don't compile, just copy
	source_name = os.path.basename(source_path)
	dest_path = os.path.join(dest_dir_path, source_name)
	shutil.copyfile(source_path, dest_path)
	return (True, None, dest_path)

compiler_dict = {
	"c": (compile_c, "native"),
	"cpp": (compile_cpp, "native"),
	"java": (compile_java, "java_bytecode"),
}

def get_compiled_lang(lang):
	if lang in compiler_dict:
		return compiler_dict[lang][1]
	elif lang in no_compiler_langs:
		return lang
	else:
		return None

class InvalidLangError(Exception):
	def __init__(self, lang):
		self.lang = lang
		self.message = lang + " is not a supported language"
		self.args = (lang,)
	def __str__(self):
		return self.message
	def __repr__(self):
		return "InvalidLangError("+self.lang+")"

def compile_source(lang, source_path, dest_dir_path):
	if lang in compiler_dict:
		return compiler_dict[lang][0](source_path, dest_dir_path)
	elif lang in no_compiler_langs:
		return compile_none(source_path, dest_dir_path)
	else:
		raise InvalidLangError(lang)

"""
Functions of the form run_<language>:
These functions return the command line which will run these programs
"""

simple_inpr_langs = ["python2", "python3", "bash"]

def run_native(prog_path, cmd_options=None):
	prog_name = os.path.basename(prog_path)
	if cmd_options==None: cmd_options = []
	return [os.path.join(".", prog_name)] + cmd_options

def run_inpr(prog_path, inpr_path, inpr_options=None, cmd_options=None):
	prog_name = os.path.basename(prog_path)
	if inpr_options==None: inpr_options=[]
	if cmd_options==None: cmd_options = []
	return [inpr_path] + inpr_options + [prog_name] + cmd_options

def run_java_bytecode(prog_path, cmd_options=None):
	class_name = os.path.splitext(os.path.basename(prog_path))[0]
	if cmd_options==None: cmd_options = []
	return [JAVA_PATH, class_name] + cmd_options

def get_prog_exec_args(lang, prog_path, cmd_options=None):
	if lang=="native":
		return run_native(prog_path, cmd_options)
	elif lang=="java_bytecode":
		return run_java_bytecode(prog_path, cmd_options)
	elif lang in simple_inpr_langs:
		inpr_path = os.path.join(INPRS_PATH, lang)
		return run_inpr(prog_path=prog_path, inpr_path=inpr_path, inpr_options=None, cmd_options=cmd_options)
	else:
		raise InvalidLangError(lang)
