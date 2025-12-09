"""
Authors: Ethan Makishima and Lucas Radovan
Date: December 2025
Description: Third slide, visually describes the padding language
"""

from manim import *
from manim_slides import Slide
from helpers import create_padding_animation

# Slide number 3
class Padding(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        # == Intro: describe the padded language before the main animation ==
        title = Text("Padded language", font_size=48)
        title.to_edge(UP)

        intro_tex = Tex(
            r"$\mathscr{L}_{\text{pad}} = \left\{ \langle x, 1^{2^{|x|^{c}}} \rangle \mid x \in \mathscr{L} \right\}$",
            tex_template=myTemplate,
            font_size=36,
        )
        intro_tex.next_to(title, DOWN, buff=0.4)

        note = Tex(
            r"Take $x \in \mathscr{L}$ and append $1^{2^{|x|^{c}}}$ to get an element of $\mathscr{L}_{\text{pad}}$.",
            tex_template=myTemplate,
            font_size=30,
        )
        note.next_to(intro_tex, DOWN, buff=0.3)

        self.play(FadeIn(title))
        self.play(Write(intro_tex))
        self.play(Write(note))
        self.next_slide()

        # fade intro out before continuing to the main construction
        self.play(FadeOut(title), FadeOut(intro_tex), FadeOut(note))

        # == definition of L_pad text to be shown during the animation ===

        l_pad_def = Tex(
            r"$\mathscr{L}_{\text{pad}} = \left\{ \langle x, 1^{2^{|x|^{c}}} \rangle \mid x \in \mathscr{L} \right\}$",
            tex_template=myTemplate,
            font_size=60,
        )
        l_pad_def.to_edge(UP, buff=0.5)

         # load the padding animation pieces
        parts = create_padding_animation(
            scene=self,
            x_height=1,
            x_width=2,
            x_font_size=32,
            one_font_size=28,
            size_arrow_mult=1.2,
        )

        # position entire composite object
        parts["group"].to_edge(LEFT, buff=0.5)

        # add label for x
        x_in_L = Tex(r"$x \in \mathscr{L}$", tex_template=myTemplate, font_size=45)
        x_in_L.next_to(parts['x_group'], DOWN, buff=0.2)

        self.play(Write(l_pad_def))
        self.play(FadeIn(parts["x_group"]))
        self.play(Write(x_in_L))
        self.play(FadeIn(parts["padding_rect"]))
        self.play(GrowArrow(parts["size_arrow"]))

        self.next_slide()

        # animate the padding expansion
        self.play(
            parts["padding_rect"].animate.stretch_to_fit_width(10, about_point=parts["padding_rect"].get_left()),
            run_time=2.0
        )
    
        self.play(Write(parts["size_label"]))

        # cleanup the padding animation
        parts["cleanup"]()

        # === Brace spanning from left of x_rect to right of padding rect ===
        brace = BraceBetweenPoints(
            parts['x_group'].get_left(),
            parts['padding_rect'].get_right(),
            direction=DOWN,
        ).shift(DOWN * 2)

        brace_label = Tex(
            r"$\langle x, 1^{2^{|x|^{c}}} \rangle \in\ \mathscr{L}_{\text{pad}}$",
            font_size=40,
            tex_template=myTemplate
        )
        brace_label.next_to(brace, DOWN)

        self.next_slide()
        self.play(GrowFromCenter(brace))
        self.play(Write(brace_label))