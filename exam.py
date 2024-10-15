from MCTS.task import *
question = """
Garrett is popping popcorn for a snack. 
As the pan of kernels heats up, the kernels start popping faster. 
Twenty pop in the first 30 seconds of cooking, then three times that amount in the next 30 seconds. 
The kernels increase to four times the initial popping rate in the next thirty seconds, 
but in the final 30 seconds, the popping slows down to half the rate as the past 30 seconds. 
After Garrett takes the pan off the heat, 
a quarter of the number of kernels that popped in the final 30 seconds of cooking also pop from the residual heat. 
How many pieces of popcorn does Garrett have to eat.
"""
task = MCTS_Task(question, 'mistral', 'local', lang='en', iteration_limit=10)
output = task.run()
print(f"output:{output}")
# print(output['solution'])