grep -Ei "hindi|label" ../../Hindi-Texfiles/vocabulary.tex | sed "s/\\\begin{hindi}//g"  | sed "s/\\\end{hindi}//g" | sed "s/\\\\//g" | tac
