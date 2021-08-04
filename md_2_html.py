from markdown import markdown
from domonic import render, html, head, body, style, script, link, article, main
# import tufte

with open('README.md', 'rb') as f:
    txtfile = f.read().decode()
    content = markdown(txtfile, 
                       extensions=['toc',
                                   'footnotes',
                                    'def_list',
                                    # tufte.TufteNoteExtension(),
                                    # tufte.ParagraphToDivExtension()
                                   ]
                      )

html_content = html(
    head(
        link(_rel="stylesheet",
             _href="tufte.css"
            ),
        # link(_rel="stylesheet",
        #      _href="tweaks.css"
        #     ),
        script("""
            MathJax = {
                tex: {
                    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]
                }
            };"""
        ),
        script(
            _id="MathJax-script",
            _async=True,
            _src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
            _type="text/javascript"
        )
    ),
    body(article(main(content)))
)

with open('dev_index.html', 'wb') as f:
    f.write(render(html_content).encode())
