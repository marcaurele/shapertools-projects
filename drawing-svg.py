import svg


class MightyWallet:

    def render(self) -> svg.SVG:
        canvas = svg.SVG(
            width="395mm",
            height="580mm",
            viewBox=svg.ViewBoxSpec(0, 0, 395, 580),
            elements=[
                svg.Rect(
                    width="100%",
                    height="100%",
                    fill="#ccc"),
                svg.Circle(
                    cx=50, cy=50, r=40, pathLength=30,
                    stroke="red",
                    fill="white",
                    stroke_width=3,
                ),
                svg.Path(
                    d=[
                        svg.M(200, 10),
                        self._draw_corner(10, 10),
                        svg.l(0, 200),
                        self._draw_corner(-10, 10),
                        svg.l(-30, 0),
                        self._draw_corner(-10, -10),
                        svg.l(0, -200),
                        self._draw_corner(10, -10),
                        svg.l(30, 0),
                    ],
                    fill="none",
                    stroke="blue",
                    stroke_width=0.5,
                ),
            ],
        )
        return canvas

    def _draw_corner(self, dx: int, dy: int) -> svg.ArcRel:
        return svg.ArcRel(
            rx=abs(dx),
            ry=abs(dy),
            angle=0,
            large_arc=False,
            sweep=True,
            dx=dx,
            dy=dy,
        )


def main():
    wallet = MightyWallet()
    print(wallet.render())


if __name__ == "__main__":
    main()
