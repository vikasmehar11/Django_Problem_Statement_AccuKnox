# Topic:Django Signals

"""Question 1:Are Django signals executed synchronously or asynchronously?

Answer:Django signals are executed synchronously."""
""""Synchronously because the signal handlers are called immediately after the signal is sent,
    so that the task depending on signal is completed before moving to the next step.
"""

# Code:-

# Import models, post_save and receiver in django
# Create a model (testModel) and use it in receiver
# Create a function for handling signal

@receiver(post_save, sender=testModel)
def handle_signal(sender, instance):
    print("Calling signal handler")

instance = testModel.objects.create(name="Sample")
print("Instance saved")

"""Question 2:Do Django signals run in the same thread as the caller?

Answer:Yes. """

# Code:-

# Import post_save, model, threading and receiver in django
# Create a model (testModel) and use it in receiver
# Create a function for handling signal

@receiver(post_save, sender=testModel)
def handle_signal(sender, instance):
    print(f"Signal thread: {threading.current_thread().name}")

# Create an instance 
print("Main thread:", threading.current_thread().name)
instance = testModel.objects.create(name="Sample")

# Both will print same thread.

"""Question 3:Do Django signals run in the same database transaction as the caller?

Answer:Yes. """

# Code:-

# Import post_save, receiver and transactionand model in django
# Create a function for handling signal

@receiver(post_save, sender=testModel)
def handle_signal(sender, instance):
    print(transaction.get_connection().in_atomic_block)

with transaction.atomic():
    testModel.objects.create(name="Test")

# Topic:Custom Classes in Python

# code:-

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Creating a rectangle

rec = Rectangle(10, 5)


