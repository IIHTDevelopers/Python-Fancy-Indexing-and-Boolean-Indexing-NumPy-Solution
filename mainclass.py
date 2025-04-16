import numpy as np

class TestScoreAnalysis:
    def __init__(self, student_ids, test_scores):
        """Initialize NumPy arrays for student data analysis"""
        self.student_ids = np.array(student_ids, dtype=np.int32)
        self.test_scores = np.array(test_scores, dtype=np.float32)

    def fancy_indexing(self):
        """Select elements at even indices"""
        return self.test_scores[::2]

    def boolean_indexing(self):
        """Select elements greater than 50"""
        return self.test_scores[self.test_scores > 50]

    def mean_score(self):
        """Calculate the mean of the test scores"""
        return np.mean(self.test_scores)

    def median_score(self):
        """Calculate the median of the test scores"""
        return np.median(self.test_scores)

    def standard_deviation(self):
        """Calculate the standard deviation of the test scores"""
        return np.std(self.test_scores)
