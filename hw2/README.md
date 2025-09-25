# Observations

1. The agent is supposed to modify the prompt into Pirate English and then pass it on to Claude, which may then contact other agents on the NANDA registry. I observed this happening when I began the homework, but did not see it in the log I am uploading. 

2. I observed the agent has no memory in the same conversation. 

3. The agent did seem to be able to answer basic questions (e.g. I asked it to make a python program that calculated a Fibonacci number.)

# Feedback

1. Although I was able to query the agent using curl commands that hit API endpoints (e.g. the `send` endpoint), my agent was not able to register on the NANDA registry. I believe this is because of an error on the NANDA registry side, as two of my classmates (including one who was able to previously register his agent with the same EC2 instance setup) were also unable to register their agents to the NANDA registry at the time I was facing issues. 

2. I was unable to access the NANDA registry through the website at: https://chat.nanda-registry.com/ . I believe many of my classmates faced the same issues.

3. Where does the NANDA adapeter fit within the larger NANDA project? I'm a bit confused about how to navigate the projnanda github. It would be great to have a technical breakdown of where the entire project is today.