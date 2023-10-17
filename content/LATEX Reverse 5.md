```LATEX
\documentclass{article}

\usepackage{caption}

  

\title{Exercise on Tables in LaTeX}

\author{}

\date{}

  

\begin{document}

\maketitle

  

\noindent Simple table:

\begin{center}

\begin{tabular}{|r|cccc|r|}

\hline

Team & P & W & D & L & Points \\

\hline

Sometown United & 12 & 2 & 3 & 7 & 9 \\

Sometown City & 10 & 10 & 0 & 0 & 30 \\

\hline

\end{tabular}

\end{center}

  

\noindent Menu:

\begin{center}

\begin{tabular}{|l|r|}

\hline

Breakfast type & Price in pounds \\

\hline

Bacon and Eggs & 3.50 \\

Continental & 3.00 \\

Cereal and milk & 2.30 \\

\hline

\end{tabular}

\end{center}

  

\noindent Table with number and caption:

\begin{center}

\begin{tabular}{|l|l|}

\hline

Name of farm & Animals \\

\hline

Happy Farm & 623 cows \\

Farm 2 & 12 piglets \\

\hline

\end{tabular}

\captionof{table}{Animal farms}

\label{tab:animal_farms}

\end{center}

  

\noindent Table \ref{tab:animal_farms} contains some info.

  

\end{document}
```

![[my5fifth.pdf]]