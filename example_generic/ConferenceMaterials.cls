\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ConferenceMaterials}[A conference materials superclass.]
\LoadClass[]{amsart}
\RequirePackage[table]{xcolor}
\RequirePackage{array}
\usepackage{geometry}
\geometry{
    a4paper,
    total={170mm,257mm},
    left=20mm,
    top=20mm,
}

\RequirePackage[freepin, crossmark]{ticket}
\RequirePackage{amsthm}
\RequirePackage{amsmath}
\RequirePackage{makecell}
\RequirePackage{longtable}
\RequirePackage{graphicx}
\RequirePackage[]{hyperref}
\RequirePackage{environ}
\RequirePackage{ifthen}
\RequirePackage{ConferenceMaterials}


% ---------------------------------------------------------------------------
% \DeclareOption{OPTION}{
% things to do if OPTION is passed
% }
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{amsart}}
\ProcessOptions\relax
\endinput