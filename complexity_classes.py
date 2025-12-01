from manim import *
from manim_slides import Slide


class ComplexityClassesOverview(Slide):
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

        p_class = Tex(r"$\mathcal{P}$: Problems solvable in polynomial time", font_size=40, tex_template=myTemplate)
        p_class.set_color(BLUE)
        classes.add(p_class)

        np_class = Tex(r"$\mathcal{NP}$: Problems verifiable in polynomial time", font_size=40, tex_template=myTemplate)
        np_class.set_color(ORANGE)
        np_class.next_to(p_class, DOWN, buff=0.5)
        classes.add(np_class)

        exp_class = Tex(r"$\mathcal{EXP}$: Problems solvable in exponential time", font_size=40, tex_template=myTemplate)
        exp_class.set_color(RED)
        exp_class.next_to(np_class, DOWN, buff=0.5)
        classes.add(exp_class)

        self.play(LaggedStartMap(Write, classes, lag_ratio=0.5))

        self.next_slide()

        relationships = Tex(
            r"$\mathcal{P} \subseteq \mathcal{NP} \subseteq \mathcal{EXP}$",
            font_size=45,
            tex_template=myTemplate
        )
        relationships.next_to(classes, DOWN, buff=1)

        self.play(Write(relationships))