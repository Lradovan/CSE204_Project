from manim import *
from manim_slides import Slide

# Slide number 5
class DecidingLPad(Slide):
    def construct(self):

        # tex template
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        # intro text
        intro = Tex(
            r"We can design an NTM ",
            r"$M'$ ",
            r"that decides $\mathscr{L}_{\text{pad}}$ in polynomial time.", 
            tex_template=myTemplate,
            font_size=45,
        )
        intro[1].set_color(PINK)
        intro.to_edge(UP, buff=0.5)
        self.play(Write(intro))

        self.next_slide()

        # text for step 1 of the construction
        step_1 = Tex(r"1.\quad Check if $w = \langle x, 1^{2^{|x|^{c}}} \rangle$.")
        step_1.to_edge(DOWN, buff=0.5)

        # text for step 2 of the construction
        step_2 = Tex(r"2. \quad Run ",
                    r"$M$ ",
                    r"on ",
                    r"$x$ ",
                    r"and follow the output.")
        step_2[1].set_color(YELLOW)
        step_2.to_edge(DOWN, buff=0.5)

        # runtime explanation for part 1
        step_1_rt_explanation = Tex(r"1. \quad On a single-tape TM, this procedure takes $O(|w|^2)$.", font_size = 35)
        step_1_rt_explanation.to_edge(DOWN, buff=0.5)

        # runtime explanation for part 2
        step_2_rt_explanation = Tex(r"2. \quad Since the running time of ",
                                   r"$M$ ",
                                   r"on $x$",
                                   r", $2^{|x|^{c}}$, is included in the input $w$, the running time of ",
                                   r"$M$ ",
                                   r"in terms of $w$ is $\underline{O(|w|)}$.", font_size = 35)
        step_2_rt_explanation[1].set_color(YELLOW)
        step_2_rt_explanation[4].set_color(YELLOW)
        step_2_rt_explanation.to_edge(DOWN, buff=0.5)

        # text for the input string w
        input_w = Tex(
            r"$w = \langle x, 1^{2^{|x|^{c}}} \rangle$",
            tex_template=myTemplate,
            font_size=60,
            color=GREEN
        )

        # rectangle for TM M'
        tm_M_prime_box = RoundedRectangle(
            width=8.0, 
            height=5.0, 
            corner_radius=0.2,
            color=PINK
        )

        # move the input w to above top left of machine box 
        top_left = tm_M_prime_box.get_corner(UL)
        input_w.next_to(top_left, direction=UP*0.6+RIGHT, buff=0.2)

        # fade out the intro and replace it with the input w
        self.play(FadeOut(intro))
        self.play(Write(input_w))

        # text for machine name M' - moved to the top left inner corner of the machine box
        machine_name = Tex(r"$M'$", tex_template=myTemplate, color=PINK)
        machine_name.next_to(top_left, direction=DOWN+RIGHT, buff=0.1)

        # load in the TM M'
        self.play(Write(tm_M_prime_box), Write(machine_name)) 

        # rectangle for the x input
        x_rect = Rectangle(width=1, height=.5)
        x_rect.set_fill(GREEN, opacity=0.5)
        x_label = Text("x", font_size=25).move_to(x_rect)
        x_group = VGroup(x_rect, x_label)

        # === padding rectangle ===
        padding_rect = Rectangle(width=4, height=.5)
        padding_rect.set_fill(BLUE, opacity=0.5)
        padding_rect.next_to(x_group, RIGHT, buff=0)

        # === count rectangle for input verification animation === 
        count_rect = Rectangle(width=1, height=0.5)
        count_rect.set_fill(TEAL, opacity=0.5)
        count_rect.next_to(padding_rect, RIGHT, buff=0)

        # group containing the three TM tape rectangles
        rect_group = VGroup(x_group, padding_rect, count_rect).move_to(ORIGIN)

        ones = VGroup(*[Text("1", font_size=25) for _ in range(7)])
        ones.arrange(RIGHT, buff=0.35)
        ones.move_to(padding_rect.get_center())

        pointer = Triangle().scale(0.18).set_fill(WHITE, opacity=1.0).set_stroke(WHITE)
        pointer.next_to(ones[0], DOWN, buff=0.15)

        # start with low opacity to show "unchecked" state
        for one in ones:
            one.set_opacity(0.25)

        # fade in everything but the counter
        self.play(FadeIn(x_group), FadeIn(padding_rect), FadeIn(ones), FadeIn(pointer))

        # write out the first step of the TM
        self.play(Write(step_1))

        self.next_slide()

        # fade in the counter
        counter = Integer(0).move_to(count_rect.get_center())
        self.play(FadeIn(count_rect), FadeIn(counter))

        # loop over the 1s, incrementing the counter for each
        for i, one in enumerate(ones, start=1):

            # Fast hop to the next '1'
            self.play(
                pointer.animate.next_to(one, DOWN),
                run_time=0.15,
                rate_func=linear
            )

            # Fast drop into c_rect
            self.play(
                pointer.animate.next_to(count_rect, DOWN, buff=0.15),
                run_time=0.08,
                rate_func=linear
            )

            # highlight
            self.play(
                one.animate.set_opacity(1.0).scale(1.05),
                run_time=0.12
            )

            # increment counter (smooth)
            self.play(
                counter.animate.set_value(counter.get_value() + 1),
                run_time=0.25,
                rate_func=smooth
            )

        # verification question regarding the # of 1's
        question = Tex(r"Does the \# of 1's $= 2^{|x|^{c}}$? If not, reject.", font_size=30, tex_template=myTemplate)
        question.next_to(rect_group, DOWN, buff=0.6)
        self.play(Write(question))

        self.next_slide()

        # fade out step 1 and bring in the runtime explanation
        self.play(FadeOut(step_1))
        self.play(Write(step_1_rt_explanation))

        self.next_slide()

        # fade out inside of M' except for the input rect x
        # fade in the second step of the TM
        self.play(FadeOut(padding_rect), FadeOut(count_rect), FadeOut(counter), FadeOut(pointer), FadeOut(ones), FadeOut(step_1_rt_explanation), FadeOut(question))
        self.play(Write(step_2))

        # --- Machine Box for the NTM M ---
        machine_box = RoundedRectangle(width=3.5, height=2, corner_radius=0.2)
        machine_label = Tex(r"NTM ", r"$M$", font_size=32)
        machine_label[1].set_color(YELLOW)
        machine_group = VGroup(machine_box, machine_label)
        machine_group.next_to(x_group, RIGHT, buff=0.4)
        self.play(FadeIn(machine_group))

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

        # --- text for runtime for NTM M---
        runtime = Tex(r"$\text{Time}($",
                      r"$M$",
                      r"$) = 2^{|x|^c}$").scale(0.9)
        runtime[1].set_color(YELLOW)
        runtime.next_to(machine_group, DOWN, buff=0.5)

        # show the runtime
        self.play(Write(runtime))

        decision = Text("REJECT/ACCEPT", font_size=15)
        decision.to_edge(RIGHT)

        output_arrow = Arrow(
            start=machine_label.get_right(),
            end=decision.get_left(),
            buff=0.2,
            stroke_width=3
        )

        # show the output arrow and reject/accept text
        self.play(Write(output_arrow), Write(decision))

        self.next_slide()

        # fade out step 2 and show the runtime explanation text
        self.play(FadeOut(step_2))
        self.play(Write(step_2_rt_explanation))