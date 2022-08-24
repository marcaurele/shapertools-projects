import svgwrite

def main():
  dwg = svgwrite.Drawing('test.svg', size=("170mm", "130mm"), viewBox=("0 0 170 130"))
  dwg.add(dwg.line((0, 0), (300, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
  dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
  dwg.save()

if __name__ == '__main__':
    main()
