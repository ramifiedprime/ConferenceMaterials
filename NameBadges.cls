\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{NameBadges}[A document class for making name badges at large scale, essentially a hook between the ticket and conferencebooklet classes]
\LoadClass[a4paper,10pt]{letter}


\RequirePackage{amsthm}
\RequirePackage{amsmath}
\RequirePackage{makecell}
\RequirePackage{longtable}
\RequirePackage{graphicx}
\RequirePackage[]{hyperref}
\RequirePackage{environ}
\RequirePackage{ifthen}
\RequirePackage{etoolbox}
\RequirePackage[freepin,crossmark]{ticket}
\RequirePackage{graphicx}
\RequirePackage{ConferenceBooklet}

\renewcommand{\ticketdefault}{%
    \put(5, 13){\line(1,0){70}}
    \put(5, 10){\scriptsize \@conferencename}
    \put(5, 7){\scriptsize \@institution}
    \put(5, 4){\scriptsize \@conferencedates}
    \put(70, 3){\@hostlogo}
    \put(30, 12){\makebox(20,10){\parbox{60mm}{\centering\@funderlogos}}}
}

% now what do you like to put in your ticket
\newcommand{\nametag}[1]{\ticket{%
    \put(30, 30){\makebox(22,10){\parbox{60mm}{\centering\bfseries\Large
    \csname @participant_#1\endcsname{name}}}}
    \put(30, 22){\makebox(20,10){\parbox{60mm}{\centering
    \csname @participant_#1\endcsname{institution}}}}
}}%

\ticketSize{80}{40}
% ---------------------------------------------------------------------------
% \DeclareOption{OPTION}{
% things to do if OPTION is passed
% }
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{amsart}}
\ProcessOptions\relax
\endinput