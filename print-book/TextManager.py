class TextManager:
    text = ''
    width = 0
    height = 0
    end_line = ''
    debug = False

    def __init__(self, text, width, height):
        self.text = text
        self.width = int(width)
        self.height = int(height)
        for i in range(self.width - 1):
            self.end_line += '='

    def process_text(self):
        lines = self.split_lines()
        lines = self.trim_lines(lines)
        lines = self.break_lines(lines)
        lines = self.page(lines)
        return(lines)

    def split_lines(self):
        return (self.text.replace('\t', '    ').split('\n'))

    def trim_lines(self, lines):
        trimmed_lines = []
        for line in lines:
            trimmed_line = line.strip()
            if (trimmed_line != ''):
                trimmed_lines.append(trimmed_line)
        return trimmed_lines

    def break_lines(self, lines):
        broken_lines = []
        for line in lines:
            if (len(line) >= (self.width)):
                broken_lines += self.break_line(line)
            else:
                broken_lines.append(line)
        return broken_lines

    def break_line(self, input_line):
        res = []
        words = input_line.split(' ')
        line = ''
        for word in words:
            if word == '':
                line += ' '
            else:
                if (len(line + ' ' + word) < self.width):
                    if line == '':
                        line = word
                    else:
                        line += ' ' + word
                else:
                    res.append(line.strip())
                    line = word
        res.append(line.strip())
        return res

    def page(self, lines):
        paged_lines = []
        for i in range(len(lines)):
            if (i % (self.height -1) == 0 and i != 0):
                paged_lines.append(self.end_line)
            paged_lines.append(lines[i])
        return paged_lines
