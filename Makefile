

UI := ui_word.py ui_vowels.py ui_usage.py ui_expression.py

ifneq ($(NUM),)
NOPT := --number $(NUM)
endif

all: test 

ui: $(UI)

ui_%.py : %.ui
	pyuic5 -i 0 $< > $@

test: $(UI)
	python3 app_expression.py
	#python3 app_usage.py
	#python3 app_vowels.py
	#python3 app_word.py

