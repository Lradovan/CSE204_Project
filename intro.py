from manim import *
from manim_slides import Slide

# Slide number 1
class Intro(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        title = Tex(
            r"Complexity Classes Overview",
            font_size=60,
            tex_template=myTemplate
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        classes = VGroup()

        p_class = Tex(r"$\mathbb{P}$: Problems solvable in polynomial time", font_size=40, tex_template=myTemplate)
        p_class.set_color(BLUE)
        p_class.next_to(title, DOWN, buff=0.3)
        classes.add(p_class)

        np_class = Tex(r"$\mathbb{NP}$: Problems verifiable in polynomial time", font_size=40, tex_template=myTemplate)
        np_class.set_color(ORANGE)
        np_class.next_to(p_class, DOWN, buff=0.5)
        classes.add(np_class)

        exp_class = Tex(r"$\mathbb{EXP}$: Problems solvable in deterministic TM in exponential time",
                        r"\\[6pt]",
                        r"or $\bigcup_{c \in \mathbb{N}} \mathrm{DTIME}(2^{n^c})$",
                        font_size=40, tex_template=myTemplate)
        exp_class.set_color(RED)
        exp_class.next_to(np_class, DOWN, buff=0.5)
        classes.add(exp_class)

        nexp_class = Tex(r"$\mathbb{NEXP}$: Problems solvable by a NTM in exponential time",
                         r"\\[6pt]",
                         r"or $\bigcup_{c \in \mathbb{N}} \mathrm{NTIME}(2^{n^c})$",
                         font_size=40, tex_template=myTemplate)
        nexp_class.set_color(PURPLE)
        nexp_class.next_to(exp_class, DOWN, buff=0.5)
        classes.add(nexp_class)

        self.play(LaggedStartMap(Write, classes, lag_ratio=0.5))

        self.next_slide()

        theorem = Tex(
            r"Theorem: If $\mathbb{EXP} \neq \mathbb{NEXP}$, then $\mathbb{P} \neq \mathbb{NP}$",
            font_size=40,
            tex_template=myTemplate
        )
        theorem.next_to(classes, DOWN, buff=1)

        self.play(Write(theorem))