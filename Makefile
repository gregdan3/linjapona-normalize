.PHONY: init run

init:
	pdm install

run:
	pdm run python ./normalize_images.py

linjapona_128x128.zip:
	zip -r './linjapona_128x128.zip' ./out/*
