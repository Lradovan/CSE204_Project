# Installing Manim:

We use version **0.19.0** of Manim Community. Follow these steps to install Manim: https://docs.manim.community/en/stable/installation.html 

(Note: There are two different versions of Manin. The link above will explain how to download the community version of Manim, which is the version you need to view the slides.)

To install Manim v0.19.0 via pip, you can do: `pip install manim==0.19.0`

# Viewing Slides:

1. `pip install manim-slides`
2. `manim-slides render presentation.py`
3. `manim-slides convert Presentation slides.html --open`

(Note: Rendering slides might freeze and stop loading. If this happens, press CTRL + C and try running the command again.)


# Proof Outline:

1. Intro - EXP != NEXP -> P != NP 
2. Assumption that P = NP and Definition of L 
3. Definition of L_pad 
4. Decidability of L using M 
5. Decidability of L_pad using M' 
6. L_pad is in NP. So L_pad is in P. 
7. Final construction of TM N that uses M' 
8. Conclusion 
