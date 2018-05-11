class Reader:
    x_list = []
    fx_list = []
    interpolation_order = 0
    operation_interpolation = 0
    operation = 0
    query_points = []
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

        if len(content) > 3:
            self.tolerance = float(content[3].rstrip().strip())
        if len(content) > 4:
            self.max_iterations = int(content[4].rstrip().strip())

    def read_interpolation(self, file):
        file_object = open(file, "r")
        content = file_object.readlines()
        file_object.close()
        self.operation_interpolation = int(content[0].rstrip().strip())
        self.interpolation_order = int(content[1].rstrip().strip())
        interval = content[2].rstrip().strip()
        interval = interval.replace("[", "")
        interval = interval.replace("]", "")
        self.x_list = interval.split(" ")
        interval = content[3].rstrip().strip()
        interval = interval.replace("[", "")
        interval = interval.replace("]", "")
        self.fx_list = interval.split(" ")
        interval = content[4].rstrip().strip()
        interval = interval.replace("[", "")
        interval = interval.replace("]", "")
        self.query_points = interval.split(" ")
        for i in range(0 , len(self.x_list)):
            self.x_list[i] = float(self.x_list[i])
            self.fx_list[i] = float(self.fx_list[i])
        for i in range(0 , len(self.query_points)):
            self.query_points[i] = float(self.query_points[i])
