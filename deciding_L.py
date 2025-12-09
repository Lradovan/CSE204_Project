"""
Authors: Ethan Makishima and Lucas Radovan
Date: December 2025
Description: Fourth slide - explanation for the decidability of L
"""

from manim import *
from manim_slides import Slide

# Slide number 4
class DecidingL(Slide):
    def construct(self):

        # tex template
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        # slide intro text
        intro = Tex(
            r"{\raggedright "
            r"Since $\mathscr{L}$ is in $\mathbb{NEXP}$, there exists a NTM ",
            r"$M$ ",
            r"deciding $\mathscr{L}$ that runs in $2^{|x|^c}$ time."
            r"\par}",
            tex_template=myTemplate,
            font_size=35,
        )

        intro.align_to(LEFT)  
        intro[1].set_color(YELLOW)   
        intro.to_edge(UP, buff=0.5)

        # load in the intro
        self.play(Write(intro))

        self.next_slide()

        # === machine box for NTM M ===
        machine_box = RoundedRectangle(width=3.5, height=2, corner_radius=0.2)
        machine_label = Tex(r"NTM ", r"$M$", font_size=32)
        machine_label[1].set_color(YELLOW)
        machine_group = VGroup(machine_box, machine_label)
        machine_group.move_to(ORIGIN)

        # === input x ===
        x_rect = Rectangle(width=1, height=.5)
        x_rect.set_fill(GREEN, opacity=0.5)
        x_label = Text("x", font_size=25).move_to(x_rect)
        x_group = VGroup(x_rect, x_label)
        x_group.to_edge(LEFT)

        # === output placeholders (dim at first) ===
        yes_text = Tex(r"$x \in \mathscr{L}$", font_size=45, tex_template = myTemplate, color=GREEN).set_opacity(0.3)
        no_text = Tex(r"$x \notin \mathscr{L}$", font_size=45, tex_template = myTemplate, color=RED).set_opacity(0.3)

        yes_text.to_edge(RIGHT).shift(UP * 0.5)
        no_text.to_edge(RIGHT).shift(DOWN * 0.5)

        # arrows from the NTM to yes/no
        arrow_yes = Arrow(
            start=machine_label.get_right() + UP*0.2,
            end=yes_text.get_left(),
            buff=0.2,
            stroke_width=3
        ).set_opacity(0.4)

        arrow_no = Arrow(
            start=machine_label.get_right() + DOWN*0.2,
            end=no_text.get_left(),
            buff=0.2,
            stroke_width=3
        ).set_opacity(0.4)
        
        # load in the input and NTM
        self.play(FadeIn(machine_group))
        self.play(FadeIn(x_group))

        # move x next to machine
        self.play(x_group.animate.next_to(machine_group, LEFT, buff=0.4))

        # draw and arrow from the input into the machine
        input_arrow = Arrow(
            start=x_rect.get_right(),
            end=machine_label.get_left(),
            buff=0.2,
            stroke_width=3
        )
        self.play(Write(input_arrow))

        # small pulse to indicate "processing"
        self.play(machine_box.animate.set_fill(YELLOW, opacity=0.1), run_time=0.4)

        # runtime of the NTM
        runtime = Tex(r"$\text{Time}($",
                    r"$M$",
                    r"$) = 2^{|x|^c}$").scale(0.9)
        runtime[1].set_color(YELLOW)
        runtime.next_to(machine_group, DOWN, buff=0.5)

        # show NTM runtime
        self.play(Write(runtime))

        # appear arrows + dim YES/NO outputs
        self.play(
            Write(arrow_yes),
            Write(arrow_no),
            Write(yes_text),
            Write(no_text),
        )

        # light up YES and NO arrows 
        self.wait(0.5)
        self.play(
            yes_text.animate.set_opacity(1),
            arrow_yes.animate.set_opacity(1),
            run_time=0.7
        )
        self.play(
            yes_text.animate.set_opacity(0.3),
            arrow_yes.animate.set_opacity(.3),
            run_time=0.7
        )
        self.play(
            no_text.animate.set_opacity(1),
            arrow_no.animate.set_opacity(1),
            run_time=0.7
        )
        self.play(
            no_text.animate.set_opacity(0.3),
            arrow_no.animate.set_opacity(0.3),
            run_time=0.7
        )

        self.next_slide()

        runtime_claim = Tex(
            r"This is \underline{polynomial} in $|\langle x, 1^{2^{|x|^{c}}} \rangle|.$",
            tex_template=myTemplate,
            font_size=45,
        )
        runtime_claim.to_edge(DOWN, buff=0.5)
        self.play(Write(runtime_claim))