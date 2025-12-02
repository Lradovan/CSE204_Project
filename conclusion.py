from manim import *
from manim_slides import Slide

# Slide number 1
class Conclusion(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        tm_explanation = Tex(
            r"TM M decides language $\mathscr{L}$, so M is deterministic",
            r"\\[6pt]",
            r"and runs in polynomial time on input of length $2^{|n|^{c}}$",
            font_size=40,
            tex_template=myTemplate
        )

        tm_explanation.to_edge(UP, buff=1)

        self.play(Write(tm_explanation))
        self.next_slide()

        tm_time = Tex(
            r"Therefore, M runs in exponential time, which shows that $\mathscr{L} \in \mathcal{EXP}$",
            font_size=40,
            tex_template=myTemplate
        )
        tm_time.next_to(tm_explanation, DOWN, buff=1)
        
        self.play(Write(tm_time))
        self.next_slide()

        conclusion = Tex(
            r"Thus, we have shown that if $\mathcal{P} = \mathcal{NP}$, then $\mathcal{EXP} = \mathcal{NEXP}$.",
            font_size=45,
            tex_template=myTemplate
        )
        conclusion.next_to(tm_time, DOWN, buff=1)

        self.play(Write(conclusion))