.PHONY: Diplomacy.log

FILES :=                              \
    Diplomacy.html                      \
    Diplomacy.log                       \
    Diplomacy.py                        \
    RunDiplomacy.in                     \
    RunDiplomacy.out                    \
    RunDiplomacy.py                     \
    TestDiplomacy.out                   \
    TestDiplomacy.py					  \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy1.in   \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy1.out  \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy2.in   \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy2.out  \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy3.in   \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy3.out  \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy4.in   \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy4.out  \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy5.in   \
	cs330e-diplomacy-tests/andrewksmith12-RunDiplomacy5.out  \
    cs330e-diplomacy-tests/andrewksmith12-TestDiplomacy.out  \
    cs330e-diplomacy-tests/andrewksmith12-TestDiplomacy.py   \

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Windows
    PYTHON   := python                 # on my machine it's python
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := python -m pydoc        # on my machine it's pydoc
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
endif


diplomacy-tests:
	git clone https://gitlab.com/fareszf/cs330e-diplomacy-tests.git

Diplomacy.html: Diplomacy.py
	$(PYDOC) -w Diplomacy

Diplomacy.log:
	git log > Diplomacy.log

RunDiplomacy.tmp: RunDiplomacy.in RunDiplomacy.out RunDiplomacy.py
	$(PYTHON) RunDiplomacy.py < RunDiplomacy1.in > RunDiplomacy1.tmp
	$(PYTHON) RunDiplomacy.py < RunDiplomacy2.in > RunDiplomacy2.tmp
	$(PYTHON) RunDiplomacy.py < RunDiplomacy3.in > RunDiplomacy3.tmp
	$(PYTHON) RunDiplomacy.py < RunDiplomacy4.in > RunDiplomacy4.tmp
	$(PYTHON) RunDiplomacy.py < RunDiplomacy5.in > RunDiplomacy5.tmp
	diff --strip-trailing-cr RunDiplomacy1.tmp RunDiplomacy1.out
	diff --strip-trailing-cr RunDiplomacy2.tmp RunDiplomacy2.out
	diff --strip-trailing-cr RunDiplomacy3.tmp RunDiplomacy3.out
	diff --strip-trailing-cr RunDiplomacy4.tmp RunDiplomacy4.out
	diff --strip-trailing-cr RunDiplomacy5.tmp RunDiplomacy5.out

TestDiplomacy.tmp: TestDiplomacy.py
	$(COVERAGE) run    --branch TestDiplomacy.py >  TestDiplomacy.tmp 2>&1
	$(COVERAGE) report -m                      >> TestDiplomacy.tmp
	cat TestDiplomacy.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  *.tmp
	rm -f  RunDiplomacy.tmp
	rm -f  TestDiplomacy.tmp
	rm -rf __pycache__
	rm -rf cs330e-diplomacy-tests

config:
	git config -l

format:
	$(AUTOPEP8) -i Diplomacy.py
	$(AUTOPEP8) -i RunDiplomacy.py
	$(AUTOPEP8) -i TestDiplomacy.py

scrub:
	make clean
	rm -f  Diplomacy.html
	rm -f  Diplomacy.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

versions:
	which       $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	which       $(COVERAGE)
	$(COVERAGE) --version
	@echo
	which       git
	git         --version
	@echo
	which       make
	make        --version
	@echo
	which       $(PIP)
	$(PIP)      --version
	@echo
	which       $(PYLINT)
	$(PYLINT)   --version
	@echo
	which        $(PYTHON)
	$(PYTHON)    --version

test: Diplomacy.html Diplomacy.log RunDiplomacy.tmp TestDiplomacy.tmp diplomacy-tests check
