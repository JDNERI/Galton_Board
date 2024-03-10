import random
import matplotlib.pyplot as plt

# Define the galton function that simulates the passage of balls through the Galton board
def galton(num_steps, num_balls):
    slots = [0] * (num_steps + 1)  # Initialize the slots on the Galton board
    order = []  # Store the order of the balls

    # For each ball
    for ball in range(1, num_balls):

        position = 0  # Initialize the position of the ball

        # For each step on the Galton board
        for step in range(1, num_steps + 1):
            # The ball moves left or right randomly
            if random.choice(["left", "right"]) == "left":
                position -= 1
            else:
                position += 1

        # Adjust the position of the ball if it goes out of bounds
        if position <= -7:
            position = 6 - abs(position) + 6
        elif position < 0:
            position = (6) - abs(position)
        elif position >= 7:
            position = 6 + position - 6
        else:
            position = 6 + position

        # Store the final position of the ball and update the count in the slots
        order.append(position)
        slots[position] += 1
    print(slots)

    # Return the order of the balls
    return order


# Define the histogram function that displays the distribution of the balls
def histogram():
    intervals = range(min(order), max(order) + 2)  # Define the intervals of the histogram
    plt.hist(x=order, bins=intervals, color='#F2AB6D')  # Create the histogram
    plt.title('Galton Board')  # Set the title of the plot
    plt.xlabel('Distribution of balls')  # Set the label of the x-axis
    plt.ylabel('Number of balls')  # Set the label of the y-axis
    plt.xticks(intervals)  # Set the ticks of the x-axis

    plt.show()  # Display the plot


# If the script is run as the main program
if __name__ == "__main__":
    order = galton(12, 3000)  # Run the Galton board simulation
    histogram()  # Display the histogram of the distribution of the balls