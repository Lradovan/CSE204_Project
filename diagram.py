from manim import *
from manim_slides import Slide

class ComplexityDiagram(Slide):
    def construct(self):

        # ----- Parameters -----
        y_baseline = -2.5  # where all ellipses will "touch"
        x_offsets = {
            "NEXP": 0.0,
            "EXP": 0.0,
            "NP": 0.0,
            "P": 0.0,
        }
        # You can adjust these x-offsets to cluster the ellipses tighter near the bottom.
        # Example: { "NEXP": -0.2, "EXP": 0, "NP": 0.15, "P": 0.3 }

        # ----- Ellipses -----
        nexp = Ellipse(width=5, height=6, color=BLUE).set_fill(BLUE, 0.05)
        exp  = Ellipse(width=4, height=5, color=GREEN).set_fill(GREEN, 0.05)
        np   = Ellipse(width=3, height=3.5, color=YELLOW).set_fill(YELLOW, 0.05)
        p    = Ellipse(width=2, height=2, color=RED).set_fill(RED, 0.05)

        # Fix baseline: bottom tips aligned
        for shape, name in [(nexp, "NEXP"), (exp, "EXP"), (np, "NP"), (p, "P")]:
            shape.move_to([x_offsets[name], y_baseline + shape.height/2, 0])

        # ----- Labels -----
        nexp_label = Text("NEXP", font_size=30).next_to(nexp, UP, buff=-0.5)
        exp_label  = Text("EXP", font_size=30).next_to(exp, UP, buff=-0.5)
        np_label   = Text("NP", font_size=30).next_to(np, UP, buff=-0.5)
        p_label    = Text("P", font_size=30).next_to(p, UP, buff=-0.5)

        # ----- Animation -----
        self.play(FadeIn(nexp), FadeIn(nexp_label))
        self.next_slide()

        self.play(FadeIn(exp), FadeIn(exp_label))
        self.next_slide()

        self.play(FadeIn(np), FadeIn(np_label))
        self.next_slide()

        self.play(FadeIn(p), FadeIn(p_label))
        self.next_slide()

        # ----- Indicate EXP != NEXP -----
        sep_line = DashedLine(
            exp.get_right(), nexp.get_right(), dash_length=0.12
        )
        sep_label = Text("≠", font_size=40).next_to(sep_line, RIGHT, buff=0.15)

        self.play(Create(sep_line), FadeIn(sep_label))
        self.next_slide()

        implication = Text("⇒  P ≠ NP", font_size=40).to_edge(DOWN)
        self.play(Write(implication))