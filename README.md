# Installing Manim:

Follow these steps to install Manim: https://docs.manim.community/en/stable/installation.html 

(Note: There are two different versions of Manin. The link above will explain how to download the community version of Manim, which is the version you need to view the slides.)

# To View the Slides:
 
1. `pip install -r requirements.txt`
2. `manim-slides render presentation.py`
3. `manim-slides convert Presentation slides.html --open`

(Note: Rendering slides might freeze and stop loading. If this happens, press CTRL + C and try running the command again.)


# Parts of the Proof

1. Intro - EXP != NEXP -> P != NP (mostly done)
2. Assumption that P = NP and Definition of L (mostly done)
3. Definition of L_pad (mostly done)
4. Decidability of L using M (mostly done)
5. Decidability of L_pad using M' (mostly done)
6. L_pad is in NP. So L_pad is in P. (mostly done)
7. Final construction of TM N that uses M' (mostly done)
8. Conclusion (mostly done)