# The purpose of this program is to produce the necessary
# lists for name badges or participant lists in the class provided
# from files in which the data is stored
# python3

import argparse
import re


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compute files in relation to conference materials preparation")
    parser.add_argument("inputfiles", metavar="f", nargs="+",
                        type= str,help="files containing only newspeaker or newparticipant commands")
    parser.add_argument('--titleabstract', dest='do_titleabs', action='store_const',
                        const=True, default=False,
                        help='make a list of titles and abstracts from the data in the files')
    parser.add_argument('--badges', dest='do_badges', action='store_const',
                        const=True, default=False,
                        help='compile name badges')
    parser.add_argument('--partlist', dest='do_participantlist', action='store_const',
                        const=True, default=False,
                        help='make a participant list from the data in the files')
    args = parser.parse_args()


    all_people = []
    pattern = re.compile(r'\\newspeaker{.*?}{.*?}{.*?}|\\newparticipant{.*?}{.*?}{.*?}')
    splitting_pattern = re.compile(r'\\|{')
    for file in args.inputfiles:
        with open (file, "r") as f:
            found_items = pattern.findall(f.read())
            all_people += [[y.strip("}") for y in splitting_pattern.split(x)[1:]] for x in found_items]

    participantlist = sorted(all_people, key=lambda x: x[3]+x[2])

    if args.do_titleabs:
        speakerlist = sorted([x for x in all_people if x[0]=="newspeaker"], key=lambda x: x[3]+x[2])
        with open("titleabstract.tex", "w") as f:
            for person in speakerlist:
                f.write("\\titleabstract{" + person[1] + "}\n")

    if args.do_participantlist:
        with open("participantlist.tex", "w") as f:
            for person in participantlist:
                f.write("\\participant{" + person[1] + "}\n")

    if args.do_badges:
        with open("namebadges.tex", "w") as f:
            f.write("\\documentclass{ConferenceMaterials}\n")
            for filename in args.inputfiles:
                usefulname = "".join(filename.split(".")[:-1])
                f.write("\\input{" + usefulname + "}\n")
            f.write("\\begin{document}\n")
            for person in participantlist:
                f.write("    \\badge{" + person[1] + "}\n")
            f.write("\\end{document}")

    