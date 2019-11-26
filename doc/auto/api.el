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
    "sec:orgaa3e908"
    "sec:org6b7eb8c"
    "sec:org649a170"
    "sec:org0bfd702"
    "sec:org9f2bd78"
    "sec:org38b7ee0"
    "sec:org3445e95"
    "sec:org4251e91"
    "sec:org92f6d09"
    "sec:orgda8113a"
    "sec:orgb9ff69c"
    "sec:orgeb7ee58"
    "sec:org423af3d"
    "sec:org18b287f"
    "sec:org2081c90"
    "sec:orgab97dea"
    "sec:orgfec1eb9"
    "sec:org2118e74"
    "sec:orga08bd35"
    "sec:orgdaca863"
    "sec:org5ba6b08"
    "sec:org0380756"
    "sec:org1103382"))
 :latex)

