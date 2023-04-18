BUILD=./scripts/build.sh
CLEANUP=./scripts/cleanup.sh
# TEXFILE=phdquali.tex
TEXFILE=ic-tese-v3.tex
MAKEINDEX=no

.PHONY: build cleanup

build:
	bash ${BUILD} ${TEXFILE} ${MAKEINDEX}

cleanup:
	@echo "Finding extra files..."
	@$(CLEANUP)
