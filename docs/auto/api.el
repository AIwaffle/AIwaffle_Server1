(TeX-add-style-hook
 "api"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "inputenc"
    "fontenc"
    "graphicx"
    "grffile"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "amssymb"
    "capt-of"
    "hyperref")
   (LaTeX-add-labels
    "sec:org7e75f92"
    "sec:org212e285"
    "sec:org08d5444"
    "sec:orge56f84a"
    "sec:org9eda3b0"
    "sec:org8e0696c"
    "sec:org253f954"
    "sec:org50b6cc9"
    "sec:org79041a1"
    "sec:org806c4db"
    "sec:org49c27e7"
    "sec:org5265526"
    "sec:orgc14215a"
    "sec:orgc377ffd"
    "sec:org4ca6f7d"
    "sec:orgcf08aeb"
    "sec:orgc49db25"
    "sec:orga87a324"
    "sec:org37d6cdd"
    "sec:orgb191206"
    "sec:orgcd52544"
    "sec:org509b09b"
    "sec:org4572f28"
    "sec:org27d0729"
    "sec:org5e5420a"))
 :latex)

