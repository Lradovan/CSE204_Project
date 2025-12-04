from manim import *

def create_padding_animation(scene, x_height, x_width, x_font_size, one_font_size, size_arrow_mult):
    """
    Create the padding-expansion animation objects and updaters.

    Parameters
    ----------
    scene : the scene into which the objects will be created. 
    x_height : height of the input rectangle representing the string x.
    x_width : width of the input rectangle representing x.
    x_font_size : font size for the label "x" inside the input rectangle.
    one_font_size : font size for the dynamically-appearing "1"s that fill the padding region.
    size_arrow_mult : vertical offset multiplier for the size arrow and label.

    Returns
    -------
    dict
        A dictionary containing all important created objects and a cleanup()
        function to remove all updaters when the animation is finished.
    """

    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

    # === Input box ===
    x_rect = Rectangle(width=x_width, height=x_height).set_fill(GREEN, opacity=0.5)
    x_label = Text("x", font_size=x_font_size).move_to(x_rect)
    x_group = VGroup(x_rect, x_label).to_edge(LEFT, buff=0.5)

    # === Padding rectangle ===
    padding_rect = Rectangle(width=0.01, height=x_height).set_fill(BLUE, opacity=0.5)
    padding_rect.next_to(x_group, RIGHT, buff=0)

    # === Arrow ===
    size_arrow = DoubleArrow(
        padding_rect.get_left() + DOWN*size_arrow_mult,
        padding_rect.get_right() + DOWN*size_arrow_mult,
        buff=0,
    )

    # === Size label ===
    size_label = MathTex("2^{|x|^c}", font_size=40)
    size_label.next_to(size_arrow, DOWN)

    # === Dynamic ones ===
    ones_group = VGroup()
    scene.add(ones_group)

    def update_ones(group):
        group.submobjects = []
        left = padding_rect.get_left()
        right = padding_rect.get_right()
        width = right[0] - left[0]
        spacing = 0.35
        count = max(0, int(width / spacing))

        for i in range(count):
            one = Text("1", font_size=one_font_size)
            one.move_to([left[0] + 0.2 + i * spacing, padding_rect.get_center()[1], 0])
            group.add(one)

    ones_group.add_updater(update_ones)

    # Arrow + label updater
    def update_arrow(arrow):
        arrow.become(DoubleArrow(
            padding_rect.get_left() + DOWN*size_arrow_mult,
            padding_rect.get_right() + DOWN*size_arrow_mult,
            buff=0,
        ))

    def update_label(label):
        label.next_to(size_arrow, DOWN)

    size_arrow.add_updater(update_arrow)
    size_label.add_updater(update_label)

    master_group = VGroup(
        x_group,
        padding_rect,
        size_arrow,
        size_label,
        ones_group
    )

    return {
        "group": master_group,
        "x_group": x_group,
        "padding_rect": padding_rect,
        "size_arrow": size_arrow,
        "size_label": size_label,
        "ones_group": ones_group,
        "cleanup": lambda: (
            size_arrow.remove_updater(update_arrow),
            size_label.remove_updater(update_label),
            ones_group.remove_updater(update_ones)
        ),
    }