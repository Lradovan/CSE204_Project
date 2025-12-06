from manim import *
from manim_slides import Slide

# import all of the invididual slides
from title import Title
from intro import Intro
from assumption import Assumption
from padding import Padding
from deciding_L import DecidingL
from deciding_L_pad import DecidingLPad
from L_pad_in_P import LPadInP
from tm_construction import TMConstruction
from conclusion import Conclusion

class Presentation(Slide):
    def construct(self):

        # (0) title
        Title.construct(self)
        self.next_slide()
        self.clear()

        # (1) intro
        Intro.construct(self)
        self.next_slide() 
        self.clear()

        # (2) assumption
        Assumption.construct(self)
        self.next_slide() 
        self.clear()

        # (3) definition of L_pad
        Padding.construct(self)
        self.next_slide()
        self.clear()

        # (4) Decidability of L
        DecidingL.construct(self)
        self.next_slide()
        self.clear()

        # (5) Decidability of L_pad
        DecidingLPad.construct(self)
        self.next_slide()
        self.clear()

        # (6) L_pad is in P
        LPadInP.construct(self)
        self.next_slide()
        self.clear()

        # (7) TM Construction
        TMConstruction.construct(self)
        self.next_slide()
        self.clear()

        # (8) Conclusion
        Conclusion.construct(self)
        self.next_slide()
        self.clear()