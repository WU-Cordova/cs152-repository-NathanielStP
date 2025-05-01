i used a deque to store a list of my orders. this way i don't need to worry about size because i can always enqueue
it's also FIFO, so orders have priority when they're put in first. however, sometimes easier orders from later on might be finished first
and i can't remove them until previous orders can be removed, which is one limit of my implementation
with more time i might add more customization, such as custom options to change the price, eg a size of a drink
i also should've added functionality to the day in review function to calcuate the total amount of money earned