from manim import *
from manim_slides import Slide

# Slide number 4
class DecidingL(Slide):
    def construct(self):

         # == text ===
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        tex = Tex(
        r"There is an NTM ",
        r"$M$",
        r" deciding $\mathscr{L}$ that runs in $2^{|x|^c}$ time",
        tex_template=myTemplate,
        font_size=45,
        )

        tex[1].set_color(YELLOW)   # only the middle piece

        tex.to_edge(UP, buff=0.5)
        self.play(Write(tex))

        # --- Machine Box ---
        machine_box = RoundedRectangle(width=3.5, height=2, corner_radius=0.2)
        machine_label = Tex(r"NTM ", r"$M$", font_size=32)

        machine_label[1].set_color(YELLOW)
        machine_group = VGroup(machine_box, machine_label)
        machine_group.move_to(ORIGIN)

        # --- Input x ---
        x_rect = Rectangle(width=1, height=.5)
        x_rect.set_fill(GREEN, opacity=0.5)
        x_label = Text("x", font_size=25).move_to(x_rect)
        x_group = VGroup(x_rect, x_label)
        x_group.to_edge(LEFT)

        # --- Output placeholders (dim at first) ---
        yes_text = Tex(r"$x \in \mathscr{L}$", font_size=45, tex_template = myTemplate, color=GREEN).set_opacity(0.3)
        no_text = Tex(r"$x \notin \mathscr{L}$", font_size=45, tex_template = myTemplate, color=RED).set_opacity(0.3)

        yes_text.to_edge(RIGHT).shift(UP * 0.5)
        no_text.to_edge(RIGHT).shift(DOWN * 0.5)

        # --- Nondeterministic arrows *pointing outwards* ---
        arrow_yes = Arrow(
            start=machine_group.get_right() + UP*0.2,
            end=yes_text.get_left(),
            buff=0.2,
            stroke_width=3
        ).set_opacity(0.4)

        arrow_no = Arrow(
            start=machine_group.get_right() + DOWN*0.2,
            end=no_text.get_left(),
            buff=0.2,
            stroke_width=3
        ).set_opacity(0.4)

        # --- Runtime ---
        runtime = Tex(r"$\text{Time}($",
                    r"$M$",
                    r"$) = 2^{|x|^c}$").scale(0.9)
        runtime[1].set_color(YELLOW)
        runtime.next_to(machine_group, DOWN, buff=0.5)

        # ---- Animations ----
        self.play(FadeIn(machine_group))
        self.play(FadeIn(x_group))

        # Move x into machine
        self.play(x_group.animate.next_to(machine_group, LEFT, buff=0.4))

        # Small pulse to indicate "processing"
        self.play(machine_box.animate.set_fill(YELLOW, opacity=0.1), run_time=0.4)
        # self.play(machine_box.animate.set_fill(opacity=0), run_time=0.4)

        # Show runtime
        self.play(Write(runtime))

        # Appear arrows + dim YES/NO outputs
        self.play(
            FadeIn(arrow_yes),
            FadeIn(arrow_no),
            FadeIn(yes_text),
            FadeIn(no_text),
        )

        # ---- Final nondeterministic choice (YES lights up) ----
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

        tex = Tex(
            r"This is \underline{polynomial} in $|\langle x, 1^{2^{|x|^{c}}} \rangle|$",
            tex_template=myTemplate,
            font_size=45,
        )
        tex.to_edge(DOWN, buff=0.5)
        self.play(Write(tex))