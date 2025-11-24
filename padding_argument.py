from manim import *

class Padding(Scene):
    def construct(self):
        target_width = 10

        # === Base rectangle ===
        rect = Rectangle(width=2, height=1)
        rect.set_fill(BLUE, opacity=0.5)
        rect.to_edge(LEFT, buff=0)
        rect.shift(RIGHT * 1)
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
        self.play(Write(size_label))

        # === Dynamic "1"s container ===
        ones_group = VGroup()
        self.add(ones_group)

        # === Updater: fill rectangle with 1s ===
        def update_ones(group):
            group.submobjects = []  # <-- CLEAR PROPERLY

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
            arrow.put_start_and_end_on(
                rect.get_left() + DOWN*1.2,
                rect.get_right() + DOWN*1.2,
            )

        def update_label(label):
            label.next_to(size_arrow, DOWN)

        size_arrow.add_updater(update_arrow)
        size_label.add_updater(update_label)

        # === Animate padding expansion ===
        self.play(
            rect.animate.stretch_to_fit_width(target_width).shift(RIGHT * 4),
            run_time=2.0,
            rate_func=smooth
        )

        # Stop updating after animation ends
        size_arrow.remove_updater(update_arrow)
        size_label.remove_updater(update_label)
        ones_group.remove_updater(update_ones)

        self.wait(1)
