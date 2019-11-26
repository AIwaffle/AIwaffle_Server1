(TeX-add-style-hook
 "api"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
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
    "sec:orgf1d93eb"
    "sec:org3a1d720"
    "sec:orgbf32299"
    "sec:org8852a24"
    "sec:org123a97a"
    "sec:org477a42b"
    "sec:org62ed299"
    "sec:org5c2d377"
    "sec:org1e08338"
    "sec:org08a734b"
    "sec:org207bd47"
    "sec:orgbcf20a3"
    "sec:org39cd272"
    "sec:org763c23c"
    "sec:org682b186"
    "sec:org979a01e"
    "sec:orgfb92061"
    "sec:org7249e48"
    "sec:org7650fcb"
    "sec:orga3d67dc"
    "sec:orgf4739aa"
    "sec:orgcb51652"
    "sec:orgdb45025"
    "sec:org66ca10e"
    "sec:org959579a"))
 :latex)

