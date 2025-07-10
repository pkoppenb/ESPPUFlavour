SUBDIRS = $(sort $(dir $(wildcard */Makefile)))

all : subs

subs :
	@for dir in $(SUBDIRS); do \
		cd $$dir && $(MAKE) || exit; cd ..; \
	done;
