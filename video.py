from extension import *
import cv2

BACKGROUD_COLOR = '#0f1517'
ACCENT_COLOR = '#96d0e5'
SECONDARY_COLOR = '#e5ab96'
TERTIARY_COLOR = '#ffffff'


class Thumbnail(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.divisors = DivisorsIlustration(ACCENT_COLOR, 0.5, 0.9)
        self.divisors.generate_lines(5)
        self.divisors.lines.become(self.divisors.to_multiplication_table())

        self.multiplication_table = MultiplicationTable(ACCENT_COLOR, 0.5, 0.9)
        self.multiplication_table.generate_lines(5)
        self.multiplication_table.lines.set_opacity(.4)

        self.multiplication_table.lines.scale(3)
        self.divisors.lines.scale(3)
        
        self.multiplication_table.lines.move_to(ORIGIN)
        self.divisors.lines.next_to(self.multiplication_table.lines, ORIGIN, aligned_edge=LEFT + UP)
        
        for i, line in enumerate(self.divisors.lines.submobjects):
            for j, number in enumerate(line.submobjects):
                value = (i + 1) * (j + 1)
                if is_prime(value):
                    number.set_color(SECONDARY_COLOR)
        for i, line in enumerate(self.multiplication_table.lines.submobjects):
            for j, number in enumerate(line.submobjects):
                value = (i + 1) * (j + 1)
                if is_prime(value):
                    number.set_color(SECONDARY_COLOR)
        self.add(self.divisors.lines)
        self.add(self.multiplication_table.lines)


class Introduction(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.divisors = DivisorsIlustration(ACCENT_COLOR, 0.5, 4/5)
        self.divisors.generate_lines(15)
        self.divisors.lines.move_to(ORIGIN)
        self.play(ShowCreation(self.divisors.lines), run_time=4)

        self.wait(3)

        self.play(Transform(self.divisors.lines,
                  self.divisors.to_multiplication_table()), run_time=3)

        self.wait(2)

        self.multiplication_table = MultiplicationTable(ACCENT_COLOR, 0.5, 4/5)
        self.multiplication_table.generate_lines(15)
        self.multiplication_table.lines.move_to(ORIGIN)
        self.multiplication_table.lines.set_opacity(.4)

        self.play(FadeIn(self.multiplication_table.lines))

        self.wait(2)

        self.play(FadeOut(self.multiplication_table.lines), run_time=2)

        self.wait()

        self.play(Transform(self.divisors.lines,
                  self.divisors.from_multiplication_table()), run_time=2)

        self.wait()


class EvenSequence(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.divisors = DivisorsIlustration(ACCENT_COLOR, 0.5, 4/5)

        self.divisors.generate_lines(15)
        self.divisors.lines.move_to(ORIGIN)

        self.add(self.divisors.lines)

        self.wait()

        self.play(*self.divisors.highlight_line(2))

        self.wait(2)

        self.position_arrow = CustomArrow(
            DOWN * 2, ORIGIN, ACCENT_COLOR, TERTIARY_COLOR)
        self.position_arrow.arrow.next_to(
            self.divisors.highlighted.submobjects[0], DOWN)

        self.position_arrow.create_tex_label(LEFT, r'2\text{x}')
        self.position_arrow.create_tex_label(DOWN, r'1\text{°}')

        self.play(GrowFromEdge(self.position_arrow.arrow, DOWN), run_time=2)
        self.play(FadeIn(self.position_arrow.labels), run_time=2)

        self.wait(2)

        def next(n):
            temp_position_arrow = self.position_arrow.copy()
            temp_position_arrow.arrow = Arrow(
                DOWN * 2, ORIGIN).set_color(TERTIARY_COLOR)
            temp_position_arrow.arrow.next_to(
                self.divisors.highlighted.submobjects[n - 1], DOWN)
            temp_position_arrow.replace_tex_label(
                1, DOWN, r'{n}\text{a}'.format(n=n, a='{°}'))
            temp_position_arrow.replace_tex_label(0, LEFT, r'2\text{x}')

            self.play(
                *self.position_arrow.replace(temp_position_arrow), run_time=2)

        next(2)

        self.wait(2)

        next(3)

        self.wait()

        next(4)

        self.wait()

        next(5)

        self.wait()

        next(6)

        self.wait()

        next(7)

        self.wait(2)

        self.play(FadeOut(self.position_arrow.group),
                  *self.divisors.unhighlight_line())

        self.wait(2)


class MultipleThreeSequence(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.divisors = DivisorsIlustration(ACCENT_COLOR, 0.5, 4/5)

        self.divisors.generate_lines(15)
        self.divisors.lines.move_to(ORIGIN)

        self.add(self.divisors.lines)

        self.wait()

        self.play(*self.divisors.highlight_line(3))

        self.wait(2)

        self.position_arrow = CustomArrow(
            DOWN * 2, ORIGIN, ACCENT_COLOR, TERTIARY_COLOR)
        self.position_arrow.arrow.next_to(
            self.divisors.highlighted.submobjects[0], DOWN)

        self.position_arrow.create_tex_label(LEFT, r'3\text{x}')
        self.position_arrow.create_tex_label(DOWN, r'1\text{°}')

        self.play(GrowFromEdge(self.position_arrow.arrow, DOWN), run_time=2)
        self.play(FadeIn(self.position_arrow.labels), run_time=2)

        self.wait(2)

        def next(n):
            temp_position_arrow = self.position_arrow.copy()
            temp_position_arrow.arrow = Arrow(
                DOWN * 2, ORIGIN).set_color(TERTIARY_COLOR)
            temp_position_arrow.arrow.next_to(
                self.divisors.highlighted.submobjects[n - 1], DOWN)
            temp_position_arrow.replace_tex_label(
                1, DOWN, r'{n}\text{a}'.format(n=n, a='{°}'))
            temp_position_arrow.replace_tex_label(0, LEFT, r'3\text{x}')

            self.play(
                *self.position_arrow.replace(temp_position_arrow), run_time=2)

        next(2)

        self.wait(2)

        next(3)

        self.wait()

        next(4)

        self.wait()

        next(5)

        self.wait(2)

        self.play(FadeOut(self.position_arrow.group),
                  *self.divisors.unhighlight_line())

        self.wait(2)


class NoticingPrimes(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.divisors = DivisorsIlustration(ACCENT_COLOR, 0.5, 4/5)

        self.divisors.generate_lines(15)
        self.divisors.lines.move_to(ORIGIN)

        self.add(self.divisors.lines)

        self.wait()

        self.divisors_of_2 = self.divisors.group_collumn_of(2)
        self.divisors_of_3 = self.divisors.group_collumn_of(3)
        self.divisors_of_5 = self.divisors.group_collumn_of(5)
        self.divisors_of_7 = self.divisors.group_collumn_of(7)
        self.divisors_of_11 = self.divisors.group_collumn_of(11)
        self.divisors_of_13 = self.divisors.group_collumn_of(13)

        self.play(SurroundingIndicate(self.divisors_of_2,
                  SECONDARY_COLOR, .15), run_time=2)
        self.wait()
        self.play(SurroundingIndicate(self.divisors_of_3,
                  SECONDARY_COLOR, .15), run_time=2)
        self.wait()
        self.play(SurroundingIndicate(self.divisors_of_5,
                  SECONDARY_COLOR, .15), run_time=2)
        self.wait()
        self.play(SurroundingIndicate(self.divisors_of_7,
                  SECONDARY_COLOR, .15), run_time=2)
        self.wait()
        self.play(SurroundingIndicate(self.divisors_of_11,
                  SECONDARY_COLOR, .15), run_time=2)
        self.wait()
        self.play(SurroundingIndicate(self.divisors_of_13,
                  SECONDARY_COLOR, .15), run_time=2)
        self.wait()

        self.play(Indicate(self.divisors_of_2), Indicate(self.divisors_of_3), Indicate(self.divisors_of_5), Indicate(
            self.divisors_of_7), Indicate(self.divisors_of_11), Indicate(self.divisors_of_13), run_time=2)
        self.wait()


class PrimesList(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.divisors = DivisorsIlustration(ACCENT_COLOR, 0.5, 4/5)

        self.divisors.generate_lines(15)
        self.divisors.lines.move_to(ORIGIN)

        self.add(self.divisors.lines)

        self.wait()

        self.primes_list = Tex('2', ',', '3', ',', '5',
                               ',', '7', ',', '11', ',', '13', ',', r'\dots')
        self.primes_list.set_color(ACCENT_COLOR)
        self.primes_list.set_color_by_tex_to_color_map({
            ',': TERTIARY_COLOR
        })

        self.play(ReplacementTransform(
            self.divisors.lines, self.primes_list), run_time=3.5)

        self.wait(2)

        temp_primes_list = Tex('2', ',', '3', ',', '5', ',',
                               '7', ',', '11', ',', '13', ',', r'\dots', r'\text{?}')
        temp_primes_list.set_color(ACCENT_COLOR)
        temp_primes_list.set_color_by_tex_to_color_map({
            ',': TERTIARY_COLOR
        })
        self.play(Transform(self.primes_list, temp_primes_list), run_time=2)

        self.wait()

        temp_primes_list = VGroup(
            Tex('2', ',', '3', ',', '5', ',', '7', ',', '11', ',', '13', ',', '17', ',', '19', ',', '23', ',', '29', ',',
                '31', ',', '37', ',', '41', ',', '43', ',', '47', ',', '53', ',', '59', ',', '61', ',', '67', ',', '71'),
            Tex('73', ',', '79', ',', '83', ',', '89', ',', '97', ',', '101', ',', '103', ',', '107',
                ',', '109', ',', '113', ',', '127', ',', '131', ',', '137', ',', '139', ',', '149'),
            Tex('151', ',', '157', ',', '163', ',', '167', ',', '173', ',', '179', ',', '181',
                ',', '191', ',', '193', ',', '197', ',', '199', ',', '211', ',', '223', ',', '239'),
            Tex('241', ',', '251', ',', '257', ',', '263', ',', '269', ',', '271', ',',
                '277', ',', '281', ',', '227', ',', '229', ',', '233', ',', '239', ',', '241')
        )
        for row in temp_primes_list:
            row.set_color(ACCENT_COLOR)
            row.set_color_by_tex_to_color_map({
                ',': TERTIARY_COLOR
            })
        align(temp_primes_list, DOWN)

        self.play(Transform(self.primes_list, temp_primes_list), run_time=3)

        self.wait(2)

        self.title = Text('NÚMEROS PRIMOS').set_color_by_gradient(
            ACCENT_COLOR, SECONDARY_COLOR).scale(3)
        self.title.to_edge(UP)
        self.play(Write(self.title), run_time=2)

        self.wait(2)

        self.play(Transform(self.title, self.title.copy().scale(
            3/4).to_edge(LEFT)), run_time=2)

        self.primo = ImageMobject('projects/eulers-number/primo.jpg')
        self.primo.scale(0.7)
        self.primo.to_corner(RIGHT + UP)

        self.wait()

        self.play(FadeIn(self.primo))

        self.wait(2)

        self.play(*(FadeOut(mobject) for mobject in self.mobjects))


class CountingPrimes(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()
        self.axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 4, 1],
            y_length=10,
            x_length=10,
            axis_config={
                "include_tip": False,
                "numbers_to_exclude": [0]
            }
        )
        self.axes.move_to(ORIGIN)
        self.axis_labels = self.axes.get_axis_labels(
            "", r"\text{primos até o número}")
        self.axes.add_coordinate_labels(range(11), range(5))
        self.graph = self.axes.get_graph(count_primes_to, x_range=[0, 10], color=[
                                         ACCENT_COLOR, ACCENT_COLOR, SECONDARY_COLOR])

        self.play(DrawBorderThenFill(self.axes), Write(self.axis_labels))
        self.play(ShowCreation(self.graph), run_time=4)

        self.wait(2)

        self.last = 10

        def increase_power_10():
            self.last *= 10
            primes_up_to_last = count_primes_to(self.last - 1)
            axes_temp = Axes(
                x_range=[0, self.last, int(self.last / 10)],
                y_range=[0, primes_up_to_last,
                         math.floor(primes_up_to_last/10)],
                y_length=10,
                x_length=10,
                axis_config={
                    "include_tip": False,
                    "numbers_to_exclude": [0]
                }
            )
            axes_temp.move_to(ORIGIN)
            axes_temp.add_coordinate_labels(range(0, self.last + 1, int(self.last / 10)), range(
                0, primes_up_to_last, math.floor(primes_up_to_last/10)))
            graph_temp = axes_temp.get_graph(lambda n: count_primes_to(n+1), x_range=[0, self.last], color=[
                                             ACCENT_COLOR, ACCENT_COLOR, SECONDARY_COLOR])
            self.play(
                Transform(self.axes, axes_temp),
                Transform(self.graph, graph_temp), run_time=4)

        increase_power_10()

        self.wait(2)

        increase_power_10()

        self.wait()

        increase_power_10()

        self.wait()

        increase_power_10()

        self.wait(.5)

        increase_power_10()

        self.wait(.5)

        primes_up_to_last = count_primes_to(self.last)
        axes_temp = Axes(
            x_range=[0, self.last, int(self.last / 10)],
            y_range=[0, primes_up_to_last, math.floor(primes_up_to_last/10)],
            y_length=10,
            x_length=10,
            axis_config={
                "include_tip": False,
                "numbers_to_exclude": [0]
            }
        )
        axes_temp.move_to(ORIGIN)
        axes_temp.add_coordinate_labels(range(0, self.last + 1, int(self.last / 10)), range(
            0, primes_up_to_last, math.floor(primes_up_to_last/10)))
        graph_temp = axes_temp.get_graph(lambda n: count_primes_to(n+1), x_range=[0, self.last], color=[
            ACCENT_COLOR, ACCENT_COLOR, SECONDARY_COLOR])
        self.log_graph = axes_temp.get_graph(count_primes_to_approx, x_range=[
                                             0, self.last], color=[SECONDARY_COLOR])
        self.axes.become(axes_temp)
        self.graph.become(graph_temp)
        self.play(ShowCreation(self.log_graph), run_time=4)

        self.wait(3)

        self.play(*(FadeOut(mobject) for mobject in self.mobjects))


class PrimeCountingFunction(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()
        self.pi_func = VGroup(
            Tex(r"\pi"),
            Tex(r"\pi", r"\left( \right)"),
            Tex(r"\pi", r"\left(10 \right)"),
            Tex(r"\pi", r"\left(10 \right)=4"),
            Tex(r"\pi", r"\left(20 \right)=8"),
            Tex(r"\pi", r"\left(30 \right)=10"),
            Tex(r"\pi", r"\left(40 \right)=12"),
            Tex(r"\pi", r"\left(50 \right)=15"),
            Tex(r"\pi", r"\left(60 \right)=17"),
            Tex(r"\pi", r"\left(70 \right)=19"),
            Tex(r"\pi", r"\left(80 \right)=22"),
            Tex(r"\pi", r"\left(90 \right)=24"),
            Tex(r"\pi", r"\left(100 \right)=25"),
        )
        self.currentTex = None
        for i, tex in enumerate(self.pi_func):
            tex.set_color(TERTIARY_COLOR)
            tex.set_color_by_tex_to_color_map({
                r"\pi": SECONDARY_COLOR
            })
            tex.scale(5)
            self.wait()
            self.currentTex = tex
            if i == 0:
                self.play(Write(self.currentTex))
            else:
                lastTex = self.pi_func.submobjects[i - 1]
                self.play(ReplacementTransform(lastTex, self.currentTex))
            self.wait(2)
        self.play(FadeOut(self.currentTex))
        self.wait()

        self.primes_up_to_milion = count_primes_to(10**6)
        self.axes = Axes(
            x_range=[0, 10**6, 10**5],
            y_range=[0, self.primes_up_to_milion,
                     math.floor(self.primes_up_to_milion/10)],
            y_length=10,
            x_length=10,
            axis_config={
                "include_tip": False,
                "numbers_to_exclude": [0]
            }
        )
        self.axes.move_to(ORIGIN)
        self.axis_labels = self.axes.get_axis_labels(
            "", r"\pi\left(\text{número}\right)")
        self.axes.add_coordinate_labels(range(0, 10**6+1, 10**5), range(
            0, self.primes_up_to_milion, math.floor(self.primes_up_to_milion/10)))
        self.graph = self.axes.get_graph(count_primes_to, x_range=[0, 10**6], color=[
                                         ACCENT_COLOR, ACCENT_COLOR, SECONDARY_COLOR])

        self.play(DrawBorderThenFill(self.axes), Write(self.axis_labels))
        self.play(ShowCreation(self.graph), run_time=4)
        self.wait()

        self.play(*(FadeOut(mobject) for mobject in self.mobjects))


class EulersNumber(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()
        self.e_lines = VGroup(
            Tex('2', '.', '71828182845904523536028747135266249775724709369995957'),
            Tex('4966967627724076630353547594571382178525166427427466391'),
            Tex('9320030599218174135966290435729003342952605956307381323'),
            Tex('2862794349076323382988075319525101901157383418793070215'),
            Tex('4089149934884167509244761460668082264800168477411853742'),
            Tex('3454424371075390777449920695517027618386062613313845830'),
            Tex('0075204493382656029760673711320070932870912744374704723'),
            Tex('0696977209310141692836819025515108657463772111252389784'),
            Tex('4250569536967707854499699679468644549059879316368892300'),
            Tex('9879312773617821542499922957635148220826989519366803318'),
            Tex('2528869398496465105820939239829488793320362509443117301'),
            Tex('2381970684161403970198376793206832823764648042953118023'),
            Tex('2878250981945581530175671736133206981125099618188159304')
        )

        align(self.e_lines, DOWN)
        self.e_lines.move_to(ORIGIN)

        for line in self.e_lines.submobjects:
            line.set_color(TERTIARY_COLOR)

        self.play(ShowCreation(self.e_lines), run_time=6)

        self.wait()

        self.play(SurroundingIndicate(
            self.e_lines.submobjects[0].get_part_by_tex('.')), run_time=2)

        self.wait(2)

        animations = []

        for i, line in enumerate(self.e_lines.submobjects):
            if i > 0:
                animations.append(FadeOut(line))

        self.first_line = self.e_lines.submobjects[0]
        self.play(*animations, self.first_line.animate.move_to(ORIGIN), run_time=2)

        self.wait()

        self.play(Transform(self.first_line, Tex('2.71828')), run_time=2)

        self.wait(3)

        self.play(self.first_line.animate.to_edge(UP))

        self.wait()

        self.year_line = NumberLine([1, 8, 7])

        self.year_brace = Brace(self.year_line, UP)
        self.year_brace_label = Text('1 Ano')
        self.year_brace_label.set_color(TERTIARY_COLOR)
        self.year_brace_label.next_to(self.year_brace, UP)

        self.step_money_range = TexNumberRange(TERTIARY_COLOR)
        self.step_money_range.nextList([1, 2])
        for i, tick in enumerate(self.year_line.get_tick_marks().submobjects):
            self.step_money_range.values_group.submobjects[i].next_to(tick, DOWN)
        # self.step_money_range.values_group.next_to(self.year_line, DOWN)

        self.step_percentage_growth_label = Text('+100%')
        self.step_percentage_growth_label.set_color(ACCENT_COLOR)
        self.step_percentage_growth_label.next_to(self.year_line, DOWN, 1)

        self.play(ShowCreation(self.year_line), run_time=2)
        self.play(GrowFromCenter(self.year_brace),
                  FadeIn(self.year_brace_label), run_time=2)
        self.play(FadeIn(self.step_percentage_growth_label))

        self.play(ShowCreation(self.step_money_range.values_group), run_time=3)

        self.wait(3)

        self.current_division = 1
        def next_division(run_time=3, number_scale=0.5):
            self.current_division += 1
            year_line_temp = NumberLine([1, 8, 7/self.current_division])

            step_percentage_growth_label_temp = Text('+{percentage}%'.format(percentage=math.floor(10000/self.current_division)/100))
            step_percentage_growth_label_temp.set_color(ACCENT_COLOR)
            step_percentage_growth_label_temp.next_to(year_line_temp, DOWN, 1)

            step_money_range_temp = TexNumberRange(TERTIARY_COLOR)
            step_money_range_temp.nextFunc(self.current_division + 1, lambda n: ((1+1/self.current_division)**n))
            step_money_range_temp.values_group.scale(number_scale)

            for i, tick in enumerate(year_line_temp.get_tick_marks().submobjects):
                if i + 1 > len(step_money_range_temp.values_group.submobjects):
                    year_line_temp.get_tick_marks().remove(tick)
            for i, number in enumerate(step_money_range_temp.values_group.submobjects):
                number.next_to(year_line_temp.get_tick_marks().submobjects[i], DOWN)

            self.play(Transform(self.year_line, year_line_temp), Transform(self.step_percentage_growth_label,
                    step_percentage_growth_label_temp), self.step_money_range.replace(step_money_range_temp), run_time=run_time)

        next_division()

        self.wait()

        next_division()

        self.wait()

        next_division()

        self.wait()

        next_division()

        self.wait()

        next_division(0.5)
        next_division(0.5)
        next_division(0.5)
        next_division(0.5)
        next_division(0.4)
        next_division(0.4, 0.4)
        next_division(0.4, 0.3)
        next_division(0.3, 0.3)
        next_division(0.3, 0.3)
        next_division(0.3, 0.3)
        next_division(0.3, 0.3)
        next_division(0.3, 0.3)
        next_division(0.3, 0.3)
        next_division(0.3, 0.3)
        next_division(0.3, 0.3)
        next_division(0.3, 0.3)
        next_division(0.2, 0.2)
        next_division(0.2, 0.2)
        next_division(0.2, 0.2)
        next_division(0.2, 0.2)
        next_division(0.2, 0.2)
        next_division(0.2, 0.2)
        next_division(0.2, 0.2)

        self.wait()

        self.play(Indicate(self.step_money_range.values_group.submobjects[-1]))

        self.wait()

        self.play(*(FadeOut(mobject) for mobject in self.mobjects))


class Ending(Scene):
    def set_background(self):
        self.background = FullScreenRectangle()
        self.background.set_fill(BACKGROUD_COLOR, 1)

    def construct(self):
        self.set_background()

        self.wait(2)
        self.eulers_number = Tex('2.71828')
        self.play(Write(self.eulers_number), run_time=2)

        self.wait(2)
        self.primes = Tex('2', ',', '3', ',', '5', ',', '7', ',', '11', ',', r'\dots')
        self.primes.set_color(ACCENT_COLOR)
        self.primes.set_color_by_tex_to_color_map({
            ',': TERTIARY_COLOR
        })

        self.relation_arrow = Arrow(LEFT, RIGHT)
        self.relation_arrow.set_color(TERTIARY_COLOR)

        self.play(self.eulers_number.animate.next_to(self.relation_arrow, LEFT), run_time=2)
        self.primes.next_to(self.relation_arrow, RIGHT)
        self.play(GrowFromEdge(self.relation_arrow, LEFT), FadeIn(self.primes), run_time=2)

        self.wait()

        self.question_mark = Text('?').set_color(ACCENT_COLOR).scale(2)
        self.question_mark.next_to(self.relation_arrow, DOWN)
        self.play(GrowFromCenter(self.question_mark), run_time=2)

        self.wait(3)