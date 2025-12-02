from manim import *
from manim_slides import Slide

# Slide number 3
class Padding(Slide):
    def construct(self):
        target_width = 10

        # == text ===
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        tex = Tex(
            r"$\mathscr{L}_{\text{pad}} = \left\{ \langle x, 1^{2^{|x|^{c}}} \rangle \mid x \in \mathscr{L} \right\}$",
            tex_template=myTemplate,
            font_size=60,
        )
        tex.to_edge(UP, buff=0.5)

        # === Input box x ===
        x_rect = Rectangle(width=2, height=1)
        x_rect.set_fill(GREEN, opacity=0.5)
        x_label = Text("x", font_size=32).move_to(x_rect)
        x_group = VGroup(x_rect, x_label)
        x_group.to_edge(LEFT, buff=0.5)

        # (1) ★ ADD "x ∈ L" label BELOW x_group
        x_in_L = Tex(r"$x \in \mathscr{L}$", tex_template=myTemplate, font_size=45)
        x_in_L.next_to(x_group, DOWN, buff=0.2)

        self.play(FadeIn(x_group))
        self.play(Write(x_in_L))
        self.play(Write(tex))

        # === Base rectangle ===
        rect = Rectangle(width=.01, height=1)
        rect.set_fill(BLUE, opacity=0.5)
        rect.next_to(x_group, RIGHT, buff=0)
        self.play(FadeIn(rect))

        # === Arrow ===
        size_arrow = DoubleArrow(
            rect.get_left() + DOWN*1.2,
            rect.get_right() + DOWN*1.2,
            buff=0,
        )
        self.play(GrowArrow(size_arrow))

        # === Label ===
        size_label = MathTex("2^{|x|^c}", font_size=40)
        size_label.next_to(size_arrow, DOWN)
        # self.play(Write(size_label))

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
                one = Text("1", font_size=28)
                x_pos = left[0] + 0.2 + i * spacing
                one.move_to([x_pos, rect.get_center()[1], 0])
                group.add(one)

        ones_group.add_updater(update_ones)

        # === Updaters for arrow & label ===
        def update_arrow(arrow):
            arrow.become(
                DoubleArrow(
                    rect.get_left() + DOWN*1.2,
                    rect.get_right() + DOWN*1.2,
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

        # (2) ★ ADD "∈ L_pad" to the right of the full padded rectangle
        # (2) ∈ L_pad
        # === Brace spanning from left of x_rect to right of rect ===
        brace = BraceBetweenPoints(
            x_rect.get_left(),
            rect.get_right(),
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
