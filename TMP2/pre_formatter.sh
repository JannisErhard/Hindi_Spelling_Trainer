grep -Ei "hindi|label" ~/Hindi/Hindi_Tex_File/Hindi-Texfiles/vocabulary.tex | sed "s/\\\begin{hindi}//g"  | sed "s/\\\end{hindi}//g" | sed "s/\\\\//g" | tac
