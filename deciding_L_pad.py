from manim import *
from manim_slides import Slide

class DecidingLPad(Slide):
    def construct(self):

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        intro = Tex(
            r"We can design an NTM ",
            r"M' ",
            r"that decides $\mathscr{L}_{\text{pad}}$ in polynomial time", 
            tex_template=myTemplate,
            font_size=45,
        )
        intro[1].set_color(PINK)

        intro.to_edge(UP, buff=0.5)
        self.play(Write(intro))

        self.next_slide()

        # line 1

        line1 = Tex(r"1.\quad Check if $w = \langle x, 1^{2^{|x|^{c}}} \rangle$")
        line1.to_edge(DOWN, buff=0.5)

        # line 2
        line2 = Tex(r"2. \quad Run ",
                    r"M ",
                    r"on ",
                    r"x ",
                    r"and follow the output")
        line2[1].set_color(YELLOW)
        line2[3].set_color(GREEN)
        line2.to_edge(DOWN, buff=0.5)

        tex = Tex(
            r"$w = \langle x, 1^{2^{|x|^{c}}} \rangle$",
            tex_template=myTemplate,
            font_size=60,
            color=GREEN
        )

        large_rectangle = RoundedRectangle(
            width=8.0, 
            height=5.0, 
            corner_radius=0.2
        )

        top_left = large_rectangle.get_corner(UL)

        tex.next_to(top_left, direction=UP*0.6+RIGHT, buff=0.2)
        self.play(FadeOut(intro))
        self.play(Write(tex))

        machine_name = Tex(r"$M'$", tex_template=myTemplate, color=PINK)

        # 2. Move text to that corner with a small margin
        machine_name.next_to(top_left, direction=DOWN+RIGHT, buff=0.1)

        self.play(FadeIn(large_rectangle), Write(machine_name)) # Add the mobject to the scene

        x_rect = Rectangle(width=1, height=.5)
        x_rect.set_fill(GREEN, opacity=0.5)
        x_label = Text("x", font_size=25).move_to(x_rect)
        x_group = VGroup(x_rect, x_label)
        #x_group.to_edge(LEFT, buff=0.5)

        # === padding rectangle ===
        rect = Rectangle(width=4, height=.5)
        rect.set_fill(BLUE, opacity=0.5)
        rect.next_to(x_group, RIGHT, buff=0)

        rect_group = VGroup(x_group, rect).move_to(ORIGIN)

        ones = VGroup(*[Text("1", font_size=25) for _ in range(7)])
        ones.arrange(RIGHT, buff=0.35)
        # center the ones in the right rectangle
        ones.move_to(rect.get_center())

        pointer = Triangle().scale(0.18).set_fill(WHITE, opacity=1.0).set_stroke(WHITE)
        pointer.next_to(ones[0], DOWN, buff=0.15)

        # start with low opacity to show "unchecked" state
        for one in ones:
            one.set_opacity(0.25)

        self.play(FadeIn(rect_group), FadeIn(ones), FadeIn(pointer))

        self.play(Write(line1))

        for i, one in enumerate(ones, start=1):
            # move pointer above current '1'

            self.play(pointer.animate.next_to(one, DOWN, buff=0.15), run_time=0.06)

            # highlight the '1' by increasing opacity and slightly scaling up
            self.play(
                one.animate.set_opacity(1.0).scale(1.05),
            )

        question = Tex(r"Does the \# of 1's $= 2^{|x|^{c}}$? If not, reject.", font_size=30, tex_template=myTemplate)
        question.next_to(rect_group, DOWN, buff=0.6)
        self.play(Write(question))

        self.next_slide()

        self.play(FadeOut(rect), FadeOut(pointer), FadeOut(ones), FadeOut(line1), FadeOut(question))

        self.play(Write(line2))

          # --- Machine Box ---
        machine_box = RoundedRectangle(width=3.5, height=2, corner_radius=0.2)
        machine_label = Tex(r"NTM ", r"M", font_size=32)
        machine_label[1].set_color(YELLOW)
        machine_group = VGroup(machine_box, machine_label)
        machine_group.next_to(x_group, RIGHT, buff=0.4)

        self.play(FadeIn(machine_group))

        # --- Runtime ---
        runtime = Tex(r"$\text{Time}($",
                      r"$M$",
                      r"$) = 2^{|x|^c}$").scale(0.9)
        runtime[1].set_color(YELLOW)
        runtime.next_to(machine_group, DOWN, buff=0.5)

        self.play(machine_box.animate.set_fill(BLUE, opacity=0.2), run_time=0.4)

        self.play(Write(runtime))

        text = Text("REJECT/ACCEPT", font_size=15)

        text.to_edge(RIGHT)

        arrow = Arrow(
            start=machine_group.get_right(),
            end=text.get_left(),
            buff=0.2,
            stroke_width=3
        )

        self.play(FadeIn(arrow), FadeIn(text))

        self.next_slide()