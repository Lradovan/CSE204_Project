from manim import *
from manim_slides import Slide

# Slide number 6
class LPadInP(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        in_np = Tex(
            r"Since the running time of ",
            r"$M'$ ", 
            r"is polynomial, and it contains a non-deterministic simulation of running ",
            r"$M$ ",
            r"on $x$, \underline{$\mathscr{L}_{\text{pad}} \in \mathcal{NP}$}.",
            font_size=40,
            tex_template=myTemplate
        )
        in_np[1].set_color(PINK)
        in_np[3].set_color(YELLOW)
        in_np.to_edge(UP, buff=1)

        self.play(Write(in_np))

        assumption = Tex(
            r"We assume $\mathcal{P} = \mathcal{NP}$",
            font_size=40,
            tex_template=myTemplate
        )
        assumption.next_to(in_np, DOWN*4)

        self.next_slide()

        self.play(Write(assumption))

        in_p = Tex(
            r"Therefore, \underline{$\mathscr{L}_{\text{pad}} \in \mathcal{P}$",
            font_size=40,
            tex_template=myTemplate
        )

        in_p.next_to(assumption, DOWN*4)

        self.next_slide()

        self.play(Write(in_p))

        l_in_exp = Tex(
            r"We can use this to show that $\mathscr{L} \in \mathcal{EXP}$",
            font_size=40,
            tex_template=myTemplate
        )

        l_in_exp.next_to(in_p, DOWN*4)

        self.next_slide()

        self.play(Write(l_in_exp))