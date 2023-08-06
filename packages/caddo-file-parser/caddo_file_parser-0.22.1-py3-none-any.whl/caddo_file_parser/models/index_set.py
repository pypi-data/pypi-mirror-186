class IndexSet:
    def __init__(self, number: int, train_indexes: [int], test_indexes: [int], seed: int):
        self.number = number
        self.train_indexes = train_indexes
        self.test_indexes = test_indexes
        self.seed = seed

    def __init__(self, index_set_yaml_file):
            self.number = index_set_yaml_file["number"]
            self.train_indexes = index_set_yaml_file["train_indexes"]
            self.test_indexes = index_set_yaml_file["test_indexes"]
            self.seed = index_set_yaml_file["seed"]
