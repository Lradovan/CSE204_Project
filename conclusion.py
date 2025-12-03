from manim import *
from manim_slides import Slide

# Slide number 8
class Conclusion(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        tm_explanation = Tex(
            r"TM ",
            r"$N'$ ",
            r"decides language $\mathscr{L}$ ",
            r"and runs in poly($2^{|x|^{c}}$) time.",
            font_size=40,
            tex_template=myTemplate
        )
        tm_explanation[1].set_color(TEAL)

        tm_explanation.to_edge(UP, buff=1)

        self.play(Write(tm_explanation))
        self.next_slide()

        tm_time = Tex(
            r"Therefore, ",
            r"$N'$ ", 
            r"runs in exponential time, which shows that $\mathscr{L} \in \mathcal{EXP}$",
            font_size=40,
            tex_template=myTemplate
        )
        tm_time[1].set_color(TEAL)
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
        self.next_slide()

        conclusion_end = Tex(
            r"Which proves: if $\mathcal{EXP} \neq \mathcal{NEXP}$, then $\mathcal{P} \neq \mathcal{NP}$",
            font_size=45,
            tex_template=myTemplate
        )

        conclusion_end.next_to(conclusion, DOWN, buff=1)

        self.play(Write(conclusion_end))

        self.next_slide()

        qed_box = Square(side_length=0.35, stroke_width=3)
        qed_fill = Square(side_length=0.35, fill_opacity=0, stroke_width=0)

        qed_box.to_corner(DOWN+RIGHT)
        qed_fill.move_to(qed_box)

        # Show outline
        self.play(Create(qed_box))

        # Fill it in
        self.play(qed_fill.animate.set_fill(color=WHITE, opacity=1), run_time=0.6)

        