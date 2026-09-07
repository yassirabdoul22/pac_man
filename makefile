PYTHON = python3
MAIN = pac-man
CONFIG = config.json
PDB = pdb
MAP = maps/easy/map.txt
install:
	pip install -r requirements.txt
run:
	$(PYTHON) $(MAIN) (CONFIG)


debug:
	$(PYTHON) -m $(PDB) $(MAIN) $(MAP)

