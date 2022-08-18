# The purpose of this program is to produce the necessary
# lists for name badges or participant lists in the class provided
# from files in which the data is stored
# python3

import sys
import re


if __name__ == '__main__':
    all_people = []
    pattern = re.compile(r'\\newspeaker{.*?}{.*?}{.*?}|\\newparticipant{.*?}{.*?}{.*?}')
    splitting_pattern = re.compile(r'\\|{')
    for file in sys.argv[1:]:
        with open (file, "r") as f:
            # print()
            found_items = pattern.findall(f.read())
            all_people += [[y.strip("}") for y in splitting_pattern.split(x)[1:]] for x in found_items]

    participantlist = sorted(all_people, key=lambda x: x[3]+x[2])
    speakerlist = sorted([x for x in all_people if x[0]=="newspeaker"], key=lambda x: x[3]+x[2])
    
    with open("participantlist.tex", "w") as f:
        for person in participantlist:
            f.write("\\participant{" + person[1] + "}\n")

    with open("titleabstract.tex", "w") as f:
        for person in speakerlist:
            f.write("\\titleabstract{" + person[1] + "}\n")
