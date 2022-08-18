# Basic Functionality

## List Production

Running the file makelists.py with arguments which are names of files containing your speakers and nonspeakers will generate an alphabetical (by surname) list for the participant list in the file "participantlist.tex".

## Datafiles
The main thing is to use the newspeaker and newparticipant commands in a separate file as data.  The python makelists.py file can use this, as can a name badges file, as can a conference booklet.  This means that the data is in one place and there are no inconsistencies between materials.