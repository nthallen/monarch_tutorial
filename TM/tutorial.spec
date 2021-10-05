# tutorial.spec
tmcbase = tutorial.tmc
tmcbase = uDACS.tmc
tmcbase = uDACS_A.tmc
colbase = uDACS_col.tmc
colbase = uDACS_A_col.tmc
genuibase = tutorial.genui

TGTDIR = /home/tutorial
IGNORE = "*.o" "*.exe" "*.stackdump" Makefile
DISTRIB = interact services
IDISTRIB = doit

tutorialcol : -lsubbuspp
tutorialdisp : tutorial.tbl
doit : tutorial.doit

%%
CXXFLAGS=-Wall -g
