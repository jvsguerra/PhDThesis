BUILD=./scripts/build.sh
CLEANUP=./scripts/cleanup.sh
TEXFILE=phdquali.tex
MAKEINDEX=no

.PHONY: build cleanup

build:
	bash ${BUILD} ${TEXFILE} ${MAKEINDEX}

cleanup:
	@echo "Finding extra files..."
	@$(CLEANUP)
