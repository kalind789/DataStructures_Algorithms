from utils import swap

class SortingAlgorithm:
    def __init__(self, app):
        self.app = app

    def bubble_sort_step(self, i, j):
        if i < len(self.app.data) - 1:
            if j < len(self.app.data) - 1 - i:
                if self.app.data[j] > self.app.data[j + 1]:
                    # Swap elements
                    swap(self.app.data, j, j+1)
                # Update the visualization
                self.app.draw_array(["red" if x == j else "yellow" if  x == j+1 else "blue" for x in range(len(self.app.data))])
                # Schedule the next step
                self.app.root.after(self.app.speed_slider.get(), lambda: self.bubble_sort_step(i, j + 1))
            else:
                # Move to the next pass through the array
                self.app.root.after(self.app.speed_slider.get(), lambda: self.bubble_sort_step(i + 1, 0))
    
    def quick_sort_step(self, i, j):
        pass
