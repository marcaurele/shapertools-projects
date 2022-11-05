from ast import Store
import svg


class MightyWallet:

    small_corner = 3
    start_x = 97
    start_y = 2

    def render(self) -> svg.SVG:
        canvas = svg.SVG(
            width="400mm",
            height="600mm",
            viewBox=svg.ViewBoxSpec(0, 0, 400, 600),
            elements=[
                # Main outer shape
                svg.Path(
                    d=[
                        svg.M(self.start_x, self.start_y),
                        svg.l(205, 0),
                        self._draw_corner(self.small_corner, self.small_corner, False),
                        self._draw_corner(90, 80),
                        self._draw_corner(-90, 80),
                        self._draw_corner(-self.small_corner, self.small_corner, False),
                        self._draw_corner(self.small_corner, self.small_corner, False),
                        self._draw_corner(90, 80),
                        self._draw_corner(-90, 80),
                        self._draw_corner(-self.small_corner, self.small_corner, False),
                        svg.l(0, 80),
                        svg.l(0, 80),
                        # self._draw_corner(self.small_corner, self.small_corner, False),
                        # svg.l(40, 0),
                        # self._draw_corner(self.small_corner, self.small_corner),
                        svg.l(0, 80),
                        self._draw_corner(-self.small_corner, self.small_corner),
                        # svg.l(-40, 0),
                        # svg.l(-self.small_corner, 0),

                        # svg.l(-205, 0),
                        svg.l(-205 + 2 * self.small_corner, 0),

                        # svg.l(-self.small_corner, 0),
                        # svg.l(-40, 0),
                        self._draw_corner(-self.small_corner, -self.small_corner),
                        svg.l(0, -80),
                        # self._draw_corner(self.small_corner, -self.small_corner),
                        # svg.l(40, 0),
                        # self._draw_corner(self.small_corner, -self.small_corner, False),
                        svg.l(0, -80),
                        svg.l(0, -80),
                        self._draw_corner(-self.small_corner, -self.small_corner, False),
                        self._draw_corner(-90, -80),
                        self._draw_corner(90, -80),
                        self._draw_corner(self.small_corner, -self.small_corner, False),
                        self._draw_corner(-self.small_corner, -self.small_corner, False),
                        self._draw_corner(-90, -80),
                        self._draw_corner(90, -80),
                        self._draw_corner(self.small_corner, -self.small_corner, False),
                    ],
                    fill="black",
                    stroke="black",
                    stroke_width=0.5,
                ),
                # Window to calibrate front image
                svg.Path(
                    d=[
                        svg.M(self.start_x + 102.5, self.start_y + self.small_corner + 80 + 80 - 10 - self.small_corner),
                        self._draw_corner(-self.small_corner, self.small_corner),
                        svg.l(-102 + self.small_corner, 0),
                        svg.l(0, -80 + 10),
                        svg.l(102 - self.small_corner, 0),
                        self._draw_corner(self.small_corner, self.small_corner),
                        self._draw_corner(self.small_corner, -self.small_corner),
                        svg.l(102 - self.small_corner, 0),
                        svg.l(0, 80 - 10),
                        svg.l(-102 + self.small_corner, 0),
                        self._draw_corner(-self.small_corner, -self.small_corner),
                    ],
                    fill="white",
                    stroke="black",
                    stroke_width=0.5,
                ),
                # Inside cards window
                svg.Path(
                    d=[
                        svg.M(self.start_x + 102.5, self.start_y + self.small_corner * 2 + 80 + 80 + 10),
                        svg.c(24,0, 20.7,0.2, 28,30),
                        svg.s(12,30,  -28,30),
                        svg.s(-35,0, -28,-30),
                        svg.s(4,-30, 28,-30),
                    ],
                    fill="white",
                    stroke="black",
                    stroke_width=0.5,
                ),
            ],
        )
        return canvas

    def _draw_corner(self, dx: int, dy: int, sweep=True) -> svg.ArcRel:
        return svg.ArcRel(
            rx=abs(dx),
            ry=abs(dy),
            angle=0,
            large_arc=False,
            sweep=sweep,
            dx=dx,
            dy=dy,
        )


def main():
    wallet = MightyWallet()
    with open("mighty-wallet.svg", "w") as f:
        f.write(f"{wallet.render()}")


if __name__ == "__main__":
    main()
