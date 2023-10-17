```LATEX
\documentclass{article}

\usepackage{amsmath}

\usepackage{amsthm}

\usepackage{graphicx}

  

\title{How I spent last summer}

  

\author{William Fayers\\

School of Mathematics and Physics,\\

University of Lincoln}

\date{October 17, 2023}

  

\newtheorem{theorem}{Theorem}

\newtheorem{lemma}{Lemma}

  

\begin{document}

\maketitle

  

\begin{abstract}

In this article, I shall discuss how I spent last summer.

\end{abstract}

  

\section*{Introduction}

Preparation is described in Section 1, beginning in Section 2, and summer proper in Section 3. Section 4 contains a photo showing a capybara that I saw when I visited the capybara cafe in Tokyo.

  

\textit{Note: Everything written about in this document is entirely fictional and not intentionally based on any true events.}

  

\section{Preparation}

Prepare for summer:

\begin{enumerate}

\item Get fit

\begin{enumerate}

\item Jogging

\item Press-ups

\item Learn to swim

\end{enumerate}

\item Buy summer clothes

\item Buy tickets

\end{enumerate}

  

\section{May}

Apart from recreational activities, in May I also did some maths, as described in Subsection 2.3.

  

\subsection{May weather}

It was raining \textit{a lot}. This phenomenon is explained in \cite[Section 4]{weather}.

  

\subsection{Reading books}

Because of what is described in Subsection 2.1, we stayed indoors and read the book \cite{book}.

  

\subsection{Maths}

I was also revising some maths for A-level exams, like the following.

\begin{theorem}

The solutions of a quadratic equation \( ax^2 + bx + c = 0 \) are given by the formulae

$$

x_{1}=\frac{-b+\sqrt{b^{2}-4ac}}{2a} \quad \text{and} \quad x_{2}=\frac{-b-\sqrt{b^{2}-4ac}}{2a}.

$$

\end{theorem}

  

\begin{lemma}

A finite sum \( \sum_{i=0}^{k} r^i a_0 \) of a geometric progression with ratio \( r \neq 1 \) is equal to

$$

a_0\left(\frac{1-r^{k+1}}{1-r}\right).

$$

\end{lemma}

  

\begin{proof}

We have

$$

(1-r)(1+r+r^2+\cdots+r^k)=1-r^{k+1},

$$

which is verified by expanding brackets:

\begin{align*}

&(1+r+r^2+\cdots+r^k)-r(1+r+r^2+\cdots+r^k)\\

&\quad=1+r+r^2+\cdots+r^k-r-r^2-\cdots-r^k-r^{k+1}=1-r^{k+1}.

\end{align*}

Dividing both sides of formula (3) by \( r-1 \) and multiplying by \( a_0 \) we have

$$

a_0+r a_0+r^2 a_0+r^3 a_0+\cdots+r^k a_0=a_0\left(\frac{1-r^{k+1}}{1-r}\right).

$$

\end{proof}

  

\begin{theorem}

The infinite sum \( \sum_{i=0}^{\infty} r^i a_0 \) of a geometric progression with ratio \( r \) satisfying \( 0<r<1 \) is equal to \( \frac{a_0}{1-r} \).

\end{theorem}

  

\begin{proof}

The sum \( \sum_{i=0}^{\infty} r^i a_0 \) is equal to the limit of the partial sums \( \sum_{i=0}^{k} r^i a_0 \) as \( k \) tends to \( \infty \). By Lemma 1,

$$

\sum_{i=0}^{k} r^i a_0=a_0\left(\frac{1-r^{k+1}}{1-r}\right).

$$

When \( 0<r<1 \), the term \( r^{k+1} \) tends to 0 as \( k \) tends to \( \infty \). Hence the result.

\end{proof}

  

\section{Summer proper}

After exams, we watched football matches on TV. At the moment the table in group E looks as in Table 1.

  

\begin{table}[h]

\centering

\caption{Euro 2016. Group E}\label{tab:groupE}

\begin{tabular}{|c|l||c|c|c|c|c|c||c|}

\hline

Pos & Team & Pld & W & D & L & GD & Pts & Qualification \\

\hline\hline

1 & Italy & 3 & 2 & 0 & 1 & +2 & 6 & Qualified \\

\hline

2 & Belgium & 3 & 2 & 0 & 1 & +2 & 6 & Qualified \\

\hline

3 & Republic of Ireland & 3 & 1 & 1 & 1 & 0 & 4 & Round of 16 \\

\hline

4 & Sweden & 3 & 0 & 1 & 2 & -2 & 1 & \\

\hline

\end{tabular}

\end{table}

  

\section{Photo}

Figure 1 shows the capybara cafe from Tokyo

\begin{figure}[h]

\includegraphics[width=\textwidth]{CapybaraCafe}

\caption{Capybara Cafe}\label{fig:capybara}

\end{figure}

  

\begin{thebibliography}{9}

\bibitem{weather}

A. Nother, Recent advances in weather prediction, \textit{J. Adv. Weather} \textbf{76}, no. 3 (2013), 23-45.

\bibitem{book}

S. Someone, \textit{A great book}, Lincoln, 2014.

\bibitem{image}

C. Capybara, Cafe Capybara introduction page, \textit{Cafe Capybara}, 2023.

\end{thebibliography}

  

  

\end{document}
```

![[latex-assignment.pdf]]