# tutorial.spec
tmcbase = tutorial.tmc
genuibase = tutorial.genui

TGTDIR = /home/tutorial
IGNORE = "*.o" "*.exe" "*.stackdump" Makefile
DISTRIB = interact services
IDISTRIB = doit

tutorialcol :
tutorialdisp : tutorial.tbl
doit : tutorial.doit

%%
CXXFLAGS=-Wall -g
