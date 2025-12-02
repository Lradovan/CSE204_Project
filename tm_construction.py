from manim import *
from manim_slides import Slide

## Slide number 2
class TMConstruction(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        intro = Tex(
            r"Since we showed $\mathscr{L}_{\text{pad}} \in \mathcal{P}$, there must be a polytime TM ",
            r"N ",
            r"that decides $\mathscr{L}_{\text{pad}}$",
            font_size=38,
            tex_template=myTemplate
        )

        intro[1].set_color(LIGHT_BROWN)
        intro.to_edge(UP, buff=0.5)
        self.play(Write(intro, duration=1))

        self.next_slide()

        construction = Tex(
            r"Let us construct a TM ",
            r"N' ",
            r"that decides $\mathscr{L}$",
            font_size=45,
            tex_template=myTemplate
        )

        construction.next_to(intro, DOWN * .7, buff=1)
        construction[1].set_color(TEAL)

        self.play(Write(construction, duration=0.8))

        line1 = Tex(r"1.\quad Construct $\langle x, 1^{2^{|x|^{c}}} \rangle$")
        line1.to_edge(UP, buff=0.5)
        line1.align_to(intro, LEFT)

        line2 = Tex(r"2.\quad Run ",
                    r"N ",
                    r"on $\langle x, 1^{2^{|x|^{c}}} \rangle$ and follow the output")
        line2[1].set_color(LIGHT_BROWN)
        line2.next_to(line1, DOWN, buff=0.3)
        line2.align_to(line1, LEFT)

        machine_box = RoundedRectangle(
            width=10, 
            height=5.0, 
            corner_radius=0.2,
            color=TEAL
        )

        machine_box.next_to(construction, DOWN*2)
        machine_box.to_edge(LEFT, buff=0.5)
        top_left = machine_box.get_corner(UL)
        machine_name = Tex(r"$N'$", tex_template=myTemplate, color=TEAL)

        # 2. Move text to that corner with a small margin
        machine_name.next_to(top_left, direction=DOWN+RIGHT, buff=0.1)

        self.play(Write(machine_box), Write(machine_name)) # Add the mobject to the scene

        # ===  Padding stuff taken from padding.py ===

        target_width = 4

         # === Input box x ===
        x_rect = Rectangle(width=1, height=.5)
        x_rect.set_fill(GREEN, opacity=0.5)
        x_label = Text("x", font_size=20).move_to(x_rect)
        x_group = VGroup(x_rect, x_label)
        x_group.next_to(machine_box.get_left(), buff=.2)

        self.play(FadeIn(x_group))

        # === Base rectangle ===
        rect = Rectangle(width=.01, height=.5)
        rect.set_fill(BLUE, opacity=0.5)
        rect.next_to(x_group, RIGHT, buff=0)
        self.play(FadeIn(rect))

        self.next_slide()

        self.play(FadeOut(construction), FadeOut(intro))
        self.play(Write(line1))

        # === Arrow ===
        size_arrow = DoubleArrow(
            rect.get_left() + DOWN *.8,
            rect.get_right() + DOWN * .8,
            buff=0,
        )

        self.play(GrowArrow(size_arrow))

        size_label = MathTex("2^{|x|^c}", font_size=40)
        size_label.next_to(size_arrow, DOWN * .8)

        # === Dynamic "1"s container ===
        ones_group = VGroup()
        self.add(ones_group)

        def update_ones(group):
            group.submobjects = []
            left = rect.get_left()
            right = rect.get_right()
            available_width = right[0] - left[0]
            spacing = 0.35
            count = max(1, int(available_width / spacing))

            for i in range(count):
                one = Text("1", font_size=20)
                x_pos = left[0] + 0.2 + i * spacing
                one.move_to([x_pos, rect.get_center()[1], 0])
                group.add(one)

        ones_group.add_updater(update_ones)

        # === Updaters for arrow & label ===
        def update_arrow(arrow):
            arrow.become(
                DoubleArrow(
                    rect.get_left() + DOWN*.8,
                    rect.get_right() + DOWN*.8,
                    buff=0,
                )
            )

        def update_label(label):
            label.next_to(size_arrow, DOWN)

        size_arrow.add_updater(update_arrow)
        size_label.add_updater(update_label)

        self.next_slide()

        # === Animate padding expansion ===
        self.play(
            rect.animate.stretch_to_fit_width(target_width, about_point=rect.get_left()),
            run_time=2.0,
            rate_func=smooth
        )

        self.play(Write(size_label))

        # Stop updating after animation ends
        size_arrow.remove_updater(update_arrow)
        size_label.remove_updater(update_label)
        ones_group.remove_updater(update_ones)

        self.next_slide()

        self.play(Write(line2))

        self.next_slide()

        self.play(FadeOut(size_arrow), FadeOut(size_label))

        # fade in the TM N

        machine_box = RoundedRectangle(width=3.5, height=2, corner_radius=0.2, color=LIGHT_BROWN)
        machine_label = Tex(r"TM ", r"N", font_size=32)
        machine_label[1].set_color(LIGHT_BROWN)
        machine_group = VGroup(machine_box, machine_label)
        machine_group.next_to(rect, RIGHT, buff=0.4)

        self.play(Write(machine_group))

        # --- Runtime ---
        runtime = Tex(r"$\text{Time}($",
                      r"$N$",
                      r"$) = poly(2^{|x|^c})$").scale(0.9)
        runtime[1].set_color(LIGHT_BROWN)
        runtime.next_to(machine_group, DOWN, buff=0.5)

        self.play(machine_box.animate.set_fill(LIGHT_BROWN, opacity=0.1), run_time=0.4)

        self.play(Write(runtime))

        text = Text("REJECT/ACCEPT", font_size=15)

        text.next_to(machine_box.get_right())
        text.to_edge(RIGHT)

        arrow = Arrow(
            start=machine_group.get_right(),
            end=text.get_left(),
            buff=0.1,
            stroke_width=3
        )

        self.play(Write(arrow), Write(text))