from manim import *
from math import sqrt

class DrawTextBox(Scene):
    def construct(self):
        text = Text("Max Cut Problem", font_size=64, color=WHITE)
        
        box = SurroundingRectangle(
            text, 
            color=BLUE, 
            buff=0.4, 
            fill_opacity=0.2, 
            fill_color=BLUE_E
        )

        VGroup(box, text).move_to(ORIGIN)
        
        self.play(Create(box), Write(text), run_time=1.5, rate_func=linear)
        self.wait(2)
        self.play(Uncreate(box), Unwrite(text), run_time=1.0, rate_func=linear)
        
class DrawGraphScene(Scene):
    def construct(self):
        vertices = list(range(1, 11))
        edges = [
            (1, 2), (2, 3), (3, 4), (4, 5), (5, 1), 
            (6, 7), (7, 8), (8, 9), (9, 10), (10, 6), 
            (1, 6), (2, 7), (3, 8), (4, 9), (5, 10)   
        ]
        
        graph = Graph(
            vertices, 
            edges, 
            layout="circular",
            layout_scale=3,
            labels=True,
            vertex_config={"fill_color": BLUE, "radius": 0.3},
            edge_config={"stroke_color": WHITE, "stroke_width": 3}
        )
        
        graph.move_to(config.frame_width * 0.25 * RIGHT)
        self.play(Create(graph), run_time=5, rate_func=ease_in_out_quint)
        
        cut_def = Paragraph(
            "A Cut is a partition of a vertex set",
            "into a Subset S and a Subset T", 
            t2c={"Subset S": RED, "Subset T": GREEN},
            font_size=32, color=WHITE, alignment = "center")
        cut_def.move_to(config.frame_width * 0.25 * LEFT + config.frame_height * 0.15 * UP)
        self.play(Write(cut_def), run_time=1, rate_func=linear)
        
        for i in range(1, 6):
            self.play(graph.vertices[2 * i - 1].animate.set_fill(RED, family=False), graph.vertices[2 * i].animate.set_fill(GREEN, family=False), run_time=0.2, rate_func=linear)
        
        for i in range(len(edges)):
            if (edges[i][0] % 2 != edges[i][1] % 2):
                self.play(graph.edges[edges[i]].animate.set_color(GOLD), run_time=0.2)
                
        cutset_def = Paragraph(
            "The cut-set here is the",
            "set of gold edges", 
            t2c={"gold": GOLD},
            font_size=32, color=WHITE, alignment="center")
        cutset_def.move_to(config.frame_width * 0.25 * LEFT)
        self.play(Write(cutset_def), run_time=1, rate_func=linear)
        
        self.wait(3)
        
        cutset_size = Paragraph(
            "The cardinality of the cut-set is",
            "the size of the cut", 
            t2c={"cut-set": GOLD},
            font_size=32, color=WHITE, alignment="center")
        cutset_size.move_to(config.frame_width * 0.25 * LEFT + config.frame_height * 0.15 * DOWN)
        self.play(Write(cutset_size), run_time=1, rate_func=linear)
        self.wait(2)
        
        maxcut = Paragraph(
            "We would like to find",
            "the BIGGEST cut!",
            font_size=32, color=WHITE, alignment="center")
        maxcut.move_to(config.frame_width * 0.25 * LEFT + config.frame_height * 0.30 * DOWN)
        self.play(Write(maxcut), run_time=1, rate_func=linear)
        
        self.wait(5)
        self.play(
            Uncreate(graph),
            Unwrite(cut_def),
            Unwrite(cutset_def),
            Unwrite(cutset_size),
            Unwrite(maxcut),
            run_time = 2.0
        )
        
class DrawNPHardScene(Scene):
    def construct(self):
        hard = Text("NP-Hard!", font_size = 128, color=WHITE)
        hard.move_to((config.frame_height / 2 + 2) * UP)
        self.add(hard)
        
        self.play(
            hard.animate.move_to((config.frame_height / 4)  * UP),
            run_time=2.0,
            rate_func=exponential_decay
        )
        
        stat1 = Text(
            "No known algorithm that solves it \"quickly\" (in polynomial time).",
            font_size=32, color=WHITE)
        stat2 = Text(
            "There are relatively large statistical approxiamtions to the max cut.",
            font_size=32, color=WHITE)
        stat3 = Paragraph(
            "The Goemans-Williamson algorithm guarantees a cut",
            "whose size is at least 87.8% of the max cut size!",
            font_size=32, color=WHITE, alignment="center")
        
        stat1.move_to((config.frame_width / 2 + stat1.width) * LEFT)
        self.add(stat1)
        self.play(
            stat1.animate.move_to(ORIGIN),
            run_time=2.0,
            rate_func=exponential_decay
        )
        
        self.wait(7)
        
        stat2.move_to((config.frame_width / 2 + stat1.width) * RIGHT + (config.frame_height / 8) * DOWN)
        self.add(stat2)
        self.play(
            stat2.animate.move_to((config.frame_height / 8) * DOWN),
            run_time=2.0,
            rate_func=exponential_decay
        )
        
        stat3.move_to((config.frame_height / 2 + stat3.height) * DOWN)
        self.add(stat3)
        self.play(
            stat3.animate.move_to((config.frame_height / 4) * DOWN),
            run_time=2.0,
            rate_func=exponential_decay
        )
        
        self.wait(3)
        self.play(Unwrite(hard), Unwrite(stat1), Unwrite(stat2), Unwrite(stat3), run_time=1)
        
class DrawCutRep(Scene):
    def construct(self):
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{xcolor}")
        rep = MathTex(r"\forall \{uv\} \in E_G [\delta = (x_u - x_v)^2]")
        rep_val = MathTex(r"\forall i [x_i \in \{1, -1\}]")
        s_half = MathTex(r"x_i = 1 \Rightarrow i \in \textcolor[HTML]{FC6255} S", tex_template=my_template)
        t_half = MathTex(r"x_i = -1 \Rightarrow i \in \textcolor[HTML]{83C167} T", tex_template=my_template)
        sum1 = MathTex(r"|C|=\frac{1}{4}\sum\limits_{(i,j) \in E_G} (x_i - x_j)^2")
        rep.move_to(config.frame_width / 4 * LEFT + config.frame_height / 3 * UP)
        rep_val.next_to(rep, DOWN, buff=0.5)
        s_half.next_to(rep_val, DOWN, buff=0.5)
        t_half.next_to(s_half, DOWN, buff=0.5)
        sum1.move_to(config.frame_height / 3 * DOWN)
        
        vertices = list([1, 'u', 'v', 4, 5])
        edges = [
            (1, 'u'), (1, 5), ('u', 'v'), ('v', 4), (4, 5), (5, 'u')
        ]
        
        graph = Graph(
            vertices, 
            edges, 
            layout="planar",
            layout_scale=3,
            labels=True,
            vertex_config={"fill_color": BLUE, "radius": 0.3},
            edge_config={"stroke_color": WHITE, "stroke_width": 3}
        )
        
        for i in range(5):
            if (i % 2 == 0):
                graph.vertices[vertices[i]].set_fill(RED, family=False)
            else:
                graph.vertices[vertices[i]].set_fill(GREEN, family=False)
    
        graph.move_to(config.frame_width / 5 * RIGHT + config.frame_height / 6 * UP)
        self.play(Create(graph), run_time=2) 
        self.play(Write(rep), run_time=1)
        self.play(Write(rep_val), run_time=1)
        self.wait(6)
        self.play(Write(s_half), run_time=1)
        self.wait(3)
        self.play(Write(t_half), run_time=1)
        self.wait(3)
        self.play(Write(sum1), run_time=1)
        self.wait(4)
        self.play(Uncreate(graph), Unwrite(rep), Unwrite(rep_val), Unwrite(s_half), Unwrite(t_half), run_time=1)
        self.play(sum1.animate.move_to(config.frame_width / 4 * LEFT + config.frame_height / 3 * UP), run_time=1)
        
class DrawExpansion(ThreeDScene):
    def construct(self):
        sum1 = MathTex(r"|C|=\frac{1}{4}\sum\limits_{(i,j) \in E_G} (x_i - x_j)^2")
        sum2 = MathTex(r"|C|=\frac{1}{4}\sum\limits_{(i,j) \in E_G} (x_i^2 + x_j^2 - 2x_ix_j)")
        sum3 = MathTex(r"|C|=\frac{1}{4}\sum\limits_{(i,j) \in E_G} (y_i \cdot y_i + y_j \cdot y_j -   2y_i \cdot y_j)")
        map = MathTex(r"F: \{-1, 1\} \to \mathbb{R}^1, \quad x_i \mapsto \mathbf{\hat{y}_i}")
        span = MathTex(r"span\{y_1, y_2, ..., y_n\} \subseteq \mathbb{R}^n")
        
        sum1.move_to(config.frame_width / 4 * LEFT + config.frame_height / 3 * UP)
        sum2.move_to(config.frame_width / 5 * LEFT + config.frame_height / 3 * UP)
        sum3.move_to(config.frame_width / 6 * LEFT + config.frame_height / 3 * UP)
        map.next_to(sum1, DOWN, buff=0.5)
        span.next_to(map, DOWN, buff=0.5)
        
        self.add(sum1)
        self.wait(12/30)
        self.play(ReplacementTransform(sum1, sum2), run_time=1)
        self.wait(1)
        self.play(Write(map), run_time=1)
        self.wait(13)
        self.play(ReplacementTransform(sum2, sum3), run_time=1)
        self.wait(3)
        self.play(Write(span), run_time=1)
        self.wait(4)
        self.wait(11)
        self.play(Unwrite(sum3), Unwrite(map), Unwrite(span), run_time=1)

class DrawCoord(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6
        )

        axes.add_coordinates()
        labels = axes.get_axis_labels(
            Tex("X").scale(0.75),
            Tex("Y").scale(0.75),
            Tex("Z").scale(0.75)
        )

        sphere = Sphere(
            center=axes.c2p(0, 0, 0),
            radius=1,
            fill_opacity=0.25,
            checkerboard_colors=[BLUE_D, BLUE_E],
            stroke_width=0.5,
            stroke_opacity=0.25
        )

        origin = axes.c2p(0, 0, 0)

        vector1 = Arrow3D(start=origin, end=axes.c2p(1/sqrt(3), 1/sqrt(3), 1/sqrt(3)), color=RED)
        vector2 = Arrow3D(start=origin, end=axes.c2p(-1/sqrt(3), 2/sqrt(3), 0), color=GREEN)
        vector3 = Arrow3D(start=origin, end=axes.c2p(0/sqrt(3.5), -1.5/sqrt(3.5), 2/sqrt(3.5)), color=YELLOW)
        vector4 = Arrow3D(start=origin, end=axes.c2p(1.5/sqrt(3), 0, -1.5/sqrt(3)), color=PURPLE)

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), Write(labels), run_time=1)
        self.wait(0.5)

        self.play(
            GrowFromCenter(sphere),
            GrowFromPoint(vector1, ORIGIN),
            GrowFromPoint(vector2, ORIGIN),
            GrowFromPoint(vector3, ORIGIN),
            GrowFromPoint(vector4, ORIGIN),
            run_time=1.5
        )
        self.wait(1)
        self.move_camera(theta=-45 * DEGREES + PI / 2, run_time=4)
        self.wait(3)

class DrawSphereNoPlane(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6
        )

        axes.add_coordinates()
        labels = axes.get_axis_labels(
            Tex("X").scale(0.75),
            Tex("Y").scale(0.75),
            Tex("Z").scale(0.75)
        )

        sphere = Sphere(
            center=axes.c2p(0, 0, 0),
            radius=1,
            fill_opacity=0.25,
            checkerboard_colors=[BLUE_D, BLUE_E],
            stroke_width=0.5,
            stroke_opacity=0.25
        )

        origin = axes.c2p(0, 0, 0)

        vector1 = Arrow3D(start=origin, end=axes.c2p(1/sqrt(3), 1/sqrt(3), 1/sqrt(3)), color=RED)
        vector2 = Arrow3D(start=origin, end=axes.c2p(-1/sqrt(3), 2/sqrt(3), 0), color=GREEN)
        vector3 = Arrow3D(start=origin, end=axes.c2p(0/sqrt(3.5), -1.5/sqrt(3.5), 2/sqrt(3.5)), color=YELLOW)
        vector4 = Arrow3D(start=origin, end=axes.c2p(1.5/sqrt(3), 0, -1.5/sqrt(3)), color=PURPLE)

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES + PI / 2)
        self.add(axes)
        self.add(labels)
        self.add(sphere)
        self.add(vector1)
        self.add(vector2)
        self.add(vector3)
        self.add(vector4)
        
class DrawSDP(Scene):
    def construct(self):
        sum3 = MathTex(r"|C|=\frac{1}{4}\sum\limits_{(i,j) \in E_G} (y_i \cdot y_i + y_j \cdot y_j - 2y_i \cdot y_j)", font_size=40)
        sum4 = MathTex(r"|C|=\frac{1}{4}\sum\limits_{(i,j) \in E_G} (2 - 2y_i \cdot y_j)", font_size=40)
        sum5 = MathTex(r"|C|=\frac{1}{2}\sum\limits_{(i,j) \in E_G} (1 - y_i \cdot y_j)", font_size=40)
        unit_eq1 = MathTex(r"\forall i [y_i \cdot y_i = 1]", font_size=40)
        unit_eq2 = MathTex(r"\forall i [y_i \cdot y_i = 1] \Rightarrow", font_size=40)
        sum3.move_to(config.frame_width / 5 * LEFT + config.frame_height / 3 * DOWN)
        sum4.move_to(config.frame_width / 5 * LEFT + config.frame_height / 3 * DOWN)
        sum5.move_to(config.frame_width / 5 * LEFT + config.frame_height / 3 * DOWN)
        unit_eq1.next_to(sum3, UP, buff=0.5)
        unit_eq2.next_to(sum3, UP, buff=0.5)
        
        self.play(Write(sum3), run_time=1)
        self.play(Write(unit_eq1), run_time=1)
        self.wait(2)
        self.play(ReplacementTransform(unit_eq1, unit_eq2), ReplacementTransform(sum3, sum4), run_time=1)
        self.wait(1)
        self.play(ReplacementTransform(sum4, sum5), run_time=1)
        self.wait(4)
        
        sdp = Paragraph("Semi-Definite", "Programming", alignment="center", font_size=48)
        sdp.move_to(config.frame_width / 5 * LEFT + config.frame_height / 3 * UP)
        self.play(Write(sdp), run_time=1)
        
        self.wait(9)
        
        away = Paragraph(
            "If u and v are adjacent, they should",
            "be looking AWAY from each other!",
            t2c={" u ": RED, " v ": GREEN},
            font_size=32, color=WHITE, alignment = "center")
        away.next_to(sdp, DOWN, buff=1)
        self.play(Write(away), run_time=1, rate_func=linear)
        
        self.wait(4)
        self.play(Unwrite(sum4), Unwrite(unit_eq2), Unwrite(sdp), Unwrite(away), run_time=1)
        
class DrawPlane(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6
        )

        axes.add_coordinates()
        labels = axes.get_axis_labels(
            Tex("X").scale(0.75),
            Tex("Y").scale(0.75),
            Tex("Z").scale(0.75)
        )

        sphere = Sphere(
            center=axes.c2p(0, 0, 0),
            radius=1,
            fill_opacity=0.25,
            checkerboard_colors=[BLUE_D, BLUE_E],
            stroke_width=0.5,
            stroke_opacity=0.25
        )

        origin = axes.c2p(0, 0, 0)

        vector1 = Arrow3D(start=origin, end=axes.c2p(1/sqrt(3), 1/sqrt(3), 1/sqrt(3)), color=RED)
        vector2 = Arrow3D(start=origin, end=axes.c2p(-1/sqrt(3), 2/sqrt(3), 0), color=GREEN)
        vector3 = Arrow3D(start=origin, end=axes.c2p(0/sqrt(3.5), -1.5/sqrt(3.5), 2/sqrt(3.5)), color=YELLOW)
        vector4 = Arrow3D(start=origin, end=axes.c2p(1.5/sqrt(3), 0, -1.5/sqrt(3)), color=PURPLE)

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES + PI / 2)
        self.add(axes)
        self.add(labels)
        self.add(sphere)
        self.add(vector1)
        self.add(vector2)
        self.add(vector3)
        self.add(vector4)
        
        normal_vector = np.array([-0.5, 1.0, 1.0])
        normal_vector = normal_vector / np.linalg.norm(normal_vector)
        z_axis = np.array([0, 0, 1])
        rot_axis = np.cross(z_axis, normal_vector)
        rot_axis = rot_axis / np.linalg.norm(rot_axis) # Normalize the axis of rotation
        rot_angle = np.arccos(np.dot(z_axis, normal_vector))

        plane = Surface(
            lambda u, v: axes.c2p(u, v, 0),
            u_range=[-3, 3],
            v_range=[-3, 3],
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.25,
            stroke_opacity=0.25
        )
        plane.rotate(rot_angle, axis=rot_axis, about_point=origin)

        half_space_red = Cube(side_length=6, fill_color=RED, fill_opacity=0.2, stroke_width=0)
        half_space_red.shift(OUT * 3) # Shift up so the bottom face touches the origin
        half_space_red.rotate(rot_angle, axis=rot_axis, about_point=origin)

        half_space_green = Cube(side_length=6, fill_color=GREEN, fill_opacity=0.2, stroke_width=0)
        half_space_green.shift(IN * 3) # Shift down so the top face touches the origin
        half_space_green.rotate(rot_angle, axis=rot_axis, about_point=origin)
        
        self.play(Create(plane), run_time=2)
        self.wait(1)
        self.play(FadeIn(half_space_red), run_time=1)
        self.wait(3)
        self.play(FadeIn(half_space_green), run_time=1)
        self.move_camera(theta=-45 * DEGREES, run_time=4)
        
#draw plane over 2 seconds 14:22 to 16:22
#wait 1 sec / 17:22
#color one half in red over 1 sec /18:22
#wait 3 sec / 21:22
#color other half in green over 1 sec /22:22

#starts at 2:28
class DrawFinal(ThreeDScene):
    def construct(self):
        self.wait(1)
        opp = Paragraph("Vectors looking opposite ways =",
                        "higher chance they end up on",
                        "different halves of the cut!", font_size=32, color=WHITE, alignment = "center")
        opp.move_to(config.frame_width / 4 * LEFT + config.frame_height / 3 * UP)
        self.play(Write(opp), run_time=1)
        prob1 = MathTex(r"\forall u, v \in V_g [Pr(u \in S \wedge v \in T]) = \frac{\theta_{uv}}{2\pi}", font_size=40)
        prob2 = MathTex(r"E(|C|) = \frac{1}{4}\sum\limits_{(i,j) \in E_G} \frac{\theta_{ij}}{2\pi}=", font_size=40)
        prob3 = MathTex(r"\frac{1}{4}\sum\limits_{(i,j) \in E_G} \frac{4}{\pi} \frac{\theta_{ij}}{(2sin(\frac{\theta_{ij}}{2}))^2} \frac{||u_i-u_j||^2}{4}")
        prob4 = MathTex(r"E(|C|) \geq \frac{\alpha}{4}\sum\limits_{(i,j) \in E_G} ||u_i-u_j||^2", font_size=40)
        prob5 = MathTex(r"E(|C|) \geq 0.878567 |Cut_{max}|", font_size=40)
        trans_group = VGroup(prob2, prob3)
        prob1.next_to(opp, DOWN, buff=0.5)
        prob2.next_to(opp, DOWN, buff=0.5)
        prob3.next_to(prob2, DOWN, buff=0.5)
        prob4.next_to(prob2, DOWN, buff=0.25)
        prob5.next_to(prob2, DOWN, buff=0.25)
        self.wait(12)
        self.play(Write(prob1), run_time=1)
        self.wait(7)
        self.play(ReplacementTransform(prob1, prob2), Write(prob3), run_time=1)
        self.wait(3)
        self.play(ReplacementTransform(trans_group, prob4), run_time=1)
        self.wait(3)
        self.play(ReplacementTransform(prob4, prob5), run_time=1)
        
        