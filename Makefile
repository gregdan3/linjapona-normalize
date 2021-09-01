.PHONY: init run

init:
	pdm install

run:
	pdm run python ./normalize_images.py
