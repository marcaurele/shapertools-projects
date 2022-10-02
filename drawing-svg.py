import svg
canvas = svg.SVG(
    width="395mm",
    height="580mm",
    elements=[
        svg.Circle(
            cx=50, cy=50, r=40, pathLength=30,
            stroke="red",
            fill="white",
            stroke_width=5,
        ),
        svg.Path(
            d=[
                svg.M(100, 10),
                svg.Arc(10, 10, 45, 0, 1, 100, 110),
            ],
            fill="none",
            stroke="blue",
            stroke_width=5,
        ),

    ],
)
print(canvas)
