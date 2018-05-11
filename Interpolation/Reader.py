class Reader:
    x_list = []
    fx_list = []
    interpolation_order = 0
    operation = 0
    equation = ""
    initial_1 = None
    initial_2 = None
    tolerance = None
    max_iterations = None

    def read(self, file):
        file_object = open(file, "r")
        content = file_object.readlines()
        file_object.close()
        self.operation = int(content[0].rstrip().strip())
        self.equation = content[1].rstrip().strip()
        interval = content[2].rstrip().strip()
        if self.operation % 2 == 0:
            interval = interval.replace("[", "")
            interval = interval.replace("]", "")
            self.initial_1 = float(interval.strip().split(" ")[0])
            self.initial_2 = float(interval.strip().split(" ")[1])

        else:
            self.initial_1 = float(interval.strip())

        if (len(content) > 3):
            self.tolerance = float(content[3].rstrip().strip())
        if (len(content) > 4):
            self.max_iterations = int(content[4].rstrip().strip())
