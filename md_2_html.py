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
        style("""
   main {
      display: flex;
      width:90%;
    }

    .main-content {
      flex: 5
    }

    .sidenav {
      flex: 1;
      height: 100%;
      background-color: #fffff8;
      padding: 1%;
    }

    .sidenav a {
      font-size: .8em;
    }

    .sidenav a:hover {
      color: hsl(0, 30%, 65%);
    }
    @media screen and (max-height: 450px) {
      .sidenav {
        padding-top: 15px;
      }"""
        ),
        link(_rel="stylesheet",
             _href="tufte.css"
            ),
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
    body(
        article(
            main(
                content
            )
        )
    )
)

with open('dev_index.html', 'wb') as f:
    f.write(render(html_content).encode())
