\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ConferenceBooklet}[A conference materials superclass.]
\LoadClass[]{amsart}
\RequirePackage[table]{xcolor}
\RequirePackage{array}
\usepackage{geometry}
\geometry{
    a4paper,
    left=20mm,
    right=10mm,
    top=20mm,
}

\RequirePackage{amsthm}
\RequirePackage{amsmath}
% \RequirePackage{makecell}
\RequirePackage{longtable}
\RequirePackage{graphicx}
\RequirePackage[]{hyperref}
\RequirePackage{environ}
\RequirePackage{ifthen}
\RequirePackage{etoolbox}
\RequirePackage{ConferenceBooklet}
\RequirePackage{multirow}

% ---------------------------------------------------------------------------
% \DeclareOption{OPTION}{
% things to do if OPTION is passed
% }
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{amsart}}
\ProcessOptions\relax
\endinput