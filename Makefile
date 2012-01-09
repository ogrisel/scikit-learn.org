SKLEARN_REPO_ALIAS ?= origin
SKLEARN_REPO_URL ?= "https://github.com/scikit-learn/scikit-learn.git"
SKLEARN_FOLDER ?= scikit-learn

WEB_REPO_ALIAS ?= origin  # alias of the remote repo where to upload the doc to
WEB_FOLDER ?= webroot

SOURCE_BRANCH ?= master
TARGET_FOLDER ?= dev

default: clone fetch build html github

clone:
	@echo "Cloning the scikit-learn repo if missing"
	if [ ! -d ${SKLEARN_FOLDER} ]; then git clone ${SKLEARN_REPO_URL} ${SKLEARN_FOLDER}; fi

fetch:
	@echo "Updating the source from remote repo"
	(cd ${SKLEARN_FOLDER} && git fetch ${SKLEARN_REPO_ALIAS})

build:
	@echo "Building the right branch of scikit-learn"
	(cd ${SKLEARN_FOLDER} && git checkout ${SOURCE_BRANCH})
	(cd ${SKLEARN_FOLDER} && make inplace)

html:
	@echo "Building the HTML doc with sphinx"
	(cd ${SKLEARN_FOLDER}/doc && make html)
	mkdir -p ${WEB_FOLDER}/${TARGET_FOLDER}
	cp -r ${SKLEARN_FOLDER}/doc/_build/html/* ${WEB_FOLDER}/${TARGET_FOLDER}/

github:
	@echo "Send to github"
	ghp-import -p ${WEB_FOLDER} -r ${WEB_REPO_ALIAS}
