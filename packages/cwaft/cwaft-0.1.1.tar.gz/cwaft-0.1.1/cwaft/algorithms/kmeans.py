import numpy as np

def calculate_distance(x, y):

    return np.square(np.sum((x - y) ** 2))

class KMeans:

    def __init__(self, k: int = 2, n_iterations: int = 10, centeroids: np.array = None):

        self.k = k
        self.n_iterations = n_iterations

        self.centeroids = centeroids
        self.labels = None
        self.error = 0

    def initialize_centeroids(self, points):

        return np.array([np.random.uniform(points.min().min(), points.max().max(), points.shape[1]) for _ in range(self.k)])

    def assign_centeroid(self, point, centeroids):

        return np.argmin(np.array([calculate_distance(centeroid, point) for centeroid in centeroids]))

    def calculate_centeroids(self, points, labels):

        return np.array([np.mean(points[labels == index], axis=0) for index in range(self.k)])

    def total_error(self, centeroids, points, labels):

        total_error = 0
        for index, centeroid in enumerate(centeroids):
            total_error += np.sum([calculate_distance(point, centeroid) for point in points[labels == index]])

        return total_error

    def fit(self, X: np.array):

        self.centeroids = self.centeroids or kmeans.initialize_centeroids(X)
        self.labels = np.array([kmeans.assign_centeroid(point, self.centeroids) for point in X])
        self.error = kmeans.total_error(self.centeroids, X, self.labels)

        for epoch in range(self.n_iterations):
            self.labels = np.array([kmeans.assign_centeroid(point, self.centeroids) for point in X])
            self.centeroids = kmeans.calculate_centeroids(X, self.labels)

            error = kmeans.total_error(self.centeroids, X, self.labels)
            if error >= self.error:
                self.total_iterations = epoch
                self.error = error
                break
            else:
                self.error = error


if __name__ == "__main__":

    kmeans = KMeans()
    # points = np.array([(i, i)])
    points = np.random.uniform(low=[0,0], high=[100,100], size=(2,2))

    kmeans.fit(points)
    
    print(kmeans)

