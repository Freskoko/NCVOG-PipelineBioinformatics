# How to run:

Change the name of NCVOG_NUMBER in step1.py to change which NCVOG is looked up

# Tree comparisons:

The three trees show some similarty.
Most notably, NCVOG0035 and NCVOG0038 are very similar.
These two trees show much the same story, with only slight variations in length between the different species.

Tree for NCVOG0001 is much less complex, and shows a different story.
Still, there is overlap between the three trees. Specifically Emiliania huxleyi virus 86, stays as a link between the two. 

# Informatics issues:

Getting the virual enviroment to work was a hassle. Using
"sudo chmod -R 777 /home/henrik" many times worked. It recursively make each file and folder everywhere, available to everyone. 

I kept getting the issue that some .algn files contained repeating information. The plottree
command did not tolerate this, so i made "remove_dup.py" to fix this issue. 

