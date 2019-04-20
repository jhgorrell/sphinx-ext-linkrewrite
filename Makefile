#
# sphinx-ext-linkrewrite/Makefile ---
#

ifeq (${SEL_DIR},)
  $(error source ./setup.env)
endif

SHELL:=bash
.SUFFIXES:

_default: _test

#####

sys_python3_exe=$(shell PATH=/usr/local/bin:/usr/bin:${PATH} type -p python3)
pip3_cmd:=${SEL_VE_DIR}/bin/python3 -m pip

_ve_build:
	${sys_python3_exe} -m venv "${SEL_VE_DIR}"
#
	${pip3_cmd} install --upgrade pip
	${pip3_cmd} install --upgrade autopep8 isort sphinx
#
	${pip3_cmd} install -e .

_ve_rm:
	-rm -rf "${SEL_VE_DIR}"

_ve_rebuild: _ve_rm _ve_build

${SEL_VE_DIR}:
	make _ve_rebuild

#####

autopep8_files=$(shell find sphinx_ext_linkrewrite setup.py -name \*.py | sort)

_isort:
	isort \
	  --multi-line 3 \
	  --trailing-comma \
	  --line-width 1 \
	  ${autopep8_files}

_autopep8:
	autopep8 -a -i \
	  --max-line-length 120 \
	  ${autopep8_files}

_pylint:
	pylint --py3k ${autopep8_files}

_precommit:
	make _ve_rebuild
	make _isort _autopep8
	make _test

#####

_docs_all:
	cd ./docs && make ${@}

_clean:
	-rm -rf ./docs/build

#####

# test the pushed version
_test_github_install:
	pip3 uninstall sphinx_ext_linkrewrite
	pip3 install git+https://github.com/jhgorrell/sphinx-ext-linkrewrite.git#egg=sphinx_ext_linkrewrite

_test+=${SEL_VE_DIR}
_test+=_docs_all

_test: ${_test}
