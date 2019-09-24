

UI := ui_word.py ui_vowels.py ui_usage.py ui_expression.py \
	ui_encounter.py ui_media.py ui_mediaedit.py

ifneq ($(NUM),)
NOPT := --number $(NUM)
endif

all: test 

ui: $(UI)

ui_%.py : %.ui
	pyuic5 -i 0 $< > $@

database:
	./parse.py $(AUDIO) $(subst words/,,$(wildcard words/*))

test: $(UI)
	python3 app_media.py
	#python3 app_encounter.py
	#python3 app_word.py
	#python3 app_expression.py
	#python3 app_usage.py
	#python3 app_vowels.py

