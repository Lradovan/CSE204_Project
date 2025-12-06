from manim import *
from manim_slides import Slide

# Slide number 0
class Title(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        title1 = Tex(
            r"Proving If $\mathbb{P} \neq \mathbb{NP}$, then "
            r"$\mathbb{EXP} \neq \mathbb{NEXP}$",
            font_size=65,
            tex_template=myTemplate
        )
        title1.to_edge(UP, buff=0.5)
        self.play(Write(title1))

        title2 = Tex(
            r"Using the Padding Argument",
            font_size=65,
            tex_template=myTemplate
        )
        title2.next_to(title1, DOWN, buff=0.5)
        self.play(Write(title2))

        self.next_slide()

        authors = Tex(
            r"By Lucas Radovan and Ethan Makishima",
            font_size=40,
            tex_template=myTemplate
        )
        authors.next_to(title2, DOWN, buff=4)
        self.play(Write(authors))
