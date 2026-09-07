PYTHON = python3
MAIN = pac-man
CONFIG = config.json
PDB = pdb

install:
	pip install -r requirements.txt
run:
	$(PYTHON) $(MAIN) (CONFIG)


debug:
	$(PYTHON) -m $(PDB) $(MAIN)

