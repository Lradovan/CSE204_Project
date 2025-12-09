"""
Authors: Ethan Makishima and Lucas Radovan
Date: December 2025
Description: Second slide - assumption that P = NP and definiton of L
"""

from manim import *
from manim_slides import Slide

## Slide number 2
class Assumption(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        title = Tex(
            r"Proof of Theorem",
            font_size=60,
            tex_template=myTemplate
        )

        title.to_edge(UP, buff=0.5)
        self.play(Write(title, duration=1))

        assumption = Tex(
            r"Assume $\mathbb{P} = \mathbb{NP}$.",
            font_size=45,
            tex_template=myTemplate
        )
        assumption.next_to(title, DOWN, buff=1)

        self.play(Write(assumption, duration=0.8))

        definition = Tex(
            r"Let $\mathscr{L}$ be a language in $\mathbb{NEXP}$.",
            font_size=45,
            tex_template=myTemplate
        )
        definition.next_to(assumption, DOWN, buff=1)

        self.next_slide()
        self.play(Write(definition, duration=1))
        ## Explain end goal of proof

        goal = Tex(
            r"We will show that $\mathscr{L}$ is also in $\mathbb{EXP}$.",
            font_size=45,
            tex_template=myTemplate
        )
        goal.next_to(definition, DOWN, buff=1)

        self.next_slide()
        self.play(Write(goal, duration=1))
        

