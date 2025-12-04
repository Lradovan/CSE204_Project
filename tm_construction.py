from manim import *
from manim_slides import Slide
from helpers import create_padding_animation

## Slide number 7
class TMConstruction(Slide):
    def construct(self):

        # tex template
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        # slide intro text
        intro = Tex(
            r"{\raggedright "
            r"Since we showed $\mathscr{L}_{\text{pad}} \in \mathbb{P}$, "
            r"there must be a polytime TM $N$ "
            r"that decides $\mathscr{L}_{\text{pad}}$."
            r"\par}",
            font_size=38,
            tex_template=myTemplate,
            substrings_to_isolate=["$N$"]
        )
        intro.set_color_by_tex("$N$", LIGHT_BROWN)
        intro.to_edge(UP, buff=0.5)
        self.play(Write(intro, duration=1))

        self.next_slide()

        # text to introduce the TM construction
        construction = Tex(
            r"{\raggedright "
            r"Let us construct a TM ",
            r"$N'$ ",
            r"that decides $\mathscr{L}$, using ",
            r"$N$",
            r"."
            r"\par}",
            tex_template=myTemplate,
            font_size=38,
        )
        construction.next_to(intro, DOWN * .7, buff=1)
        construction.align_to(intro, LEFT)
        construction[1].set_color(TEAL)
        construction[3].set_color(LIGHT_BROWN)
        self.play(Write(construction, duration=0.8))

        # text for step 1 of the TM construction
        step_1 = Tex(r"1.\quad Construct $\langle x, 1^{2^{|x|^{c}}} \rangle$.")
        step_1.to_edge(UP, buff=0.5)
        step_1.align_to(intro, LEFT)

        # text for step 2 of the TM construction
        step_2 = Tex(r"2.\quad Run ",
                    r"N ",
                    r"on $\langle x, 1^{2^{|x|^{c}}} \rangle$ and follow the output.")
        step_2[1].set_color(LIGHT_BROWN)
        step_2.next_to(step_1, DOWN, buff=0.3)
        step_2.align_to(step_1, LEFT)

        # box for the TM N'
        tm_N_prime_box = RoundedRectangle(
            width=10, 
            height=5.0, 
            corner_radius=0.2,
            color=TEAL
        )
        tm_N_prime_box.next_to(construction, DOWN*2)
        tm_N_prime_box.to_edge(LEFT, buff=0.5)

        # add a machine label to the top left of the box
        top_left = tm_N_prime_box.get_corner(UL)
        machine_name = Tex(r"$N'$", tex_template=myTemplate, color=TEAL)
        machine_name.next_to(top_left, direction=DOWN+RIGHT, buff=0.1)

        # write in the TM box and label
        self.play(Write(tm_N_prime_box), Write(machine_name))

        # run the padding animation
        parts = create_padding_animation(
            scene=self,
            x_height=.5,
            x_width=1,
            x_font_size=20,
            one_font_size=20,
            size_arrow_mult=0.8,
        )

        # Position entire composite object
        parts["group"].next_to(tm_N_prime_box.get_left(), buff=0.2, aligned_edge=LEFT)

        # now animate
        self.play(FadeIn(parts["x_group"]))
        self.play(FadeIn(parts["padding_rect"]))
        self.play(GrowArrow(parts["size_arrow"]))

        self.next_slide()

        self.play(FadeOut(construction), FadeOut(intro))
        self.play(Write(step_1))

        self.next_slide()

        # animate the padding expansion
        self.play(
            parts["padding_rect"].animate.stretch_to_fit_width(4, about_point=parts["padding_rect"].get_left()),
            run_time=2.0
        )
    
        self.play(Write(parts["size_label"]))

        # cleanup the padding animation
        parts["cleanup"]()

        self.next_slide()

        # write out the second step
        self.play(Write(step_2))

        self.next_slide()

        self.play(FadeOut(parts['size_arrow']), FadeOut(parts['size_label']))

        # fade in the TM N
        machine_box = RoundedRectangle(width=3.5, height=2, corner_radius=0.2, color=LIGHT_BROWN)
        machine_label = Tex(r"TM ", r"N", font_size=32)
        machine_label[1].set_color(LIGHT_BROWN)
        machine_group = VGroup(machine_box, machine_label)
        machine_group.next_to(parts['padding_rect'], RIGHT, buff=0.4)
        self.play(Write(machine_group))

        # --- runtime text for TM N---
        runtime = Tex(r"$\text{Time}($",
                      r"$N$",
                      r"$) = poly(2^{|x|^c})$").scale(0.9)
        runtime[1].set_color(LIGHT_BROWN)
        runtime.next_to(machine_group, DOWN, buff=0.5)

        # input arrow between w and TM N
        input_arrow = Arrow(
            start=parts['padding_rect'].get_right(),
            end=machine_label.get_left(),
            buff=0.2,
            stroke_width=3
        )
        self.play(Write(input_arrow))

        # small pulse to indicate "processing"
        self.play(machine_box.animate.set_fill(LIGHT_BROWN, opacity=0.1), run_time=0.4)

        # write in the runtime
        self.play(Write(runtime))

        decision = Text("REJECT/ACCEPT", font_size=15)
        decision.next_to(machine_box.get_right())
        decision.to_edge(RIGHT)

        output_arrow = Arrow(
            start=machine_label.get_right(),
            end=decision.get_left(),
            buff=0.1,
            stroke_width=3
        )

        # show the output arrow and reject/accept text
        self.play(Write(output_arrow), Write(decision))