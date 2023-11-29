grep -Ei "hindi|label" raw | sed "s/\\\begin{hindi}//g"  | sed "s/\\\end{hindi}//g" | sed "s/\\\\//g" | tac
