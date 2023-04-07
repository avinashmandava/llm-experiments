from langchain import PromptTemplate

def construct_prompt(technology, goal, metric_data):

  template = """
  I want you to act as a consultant for a company that is running {technology}.

  They have asked you to help them {goal}.

  They have provided you with some metrics representing behavior of the system, which you can use to help you make recommendations.

  Here are the relevant metrics, including their average over the last hour, the current value, the standard deviation, and the z-score given the distribution:

  {metric_data}.

  Recommend at least five, and no more than ten concrete actions they can take to improve performance.

  Put the recommendations in list prioritized by likelihood of fixing the issue.

  Structure the response as a list of JSON objects, with each recommendation having the folowing fields:

  Priority: This field should represent the ranking of the recommendation, based on how likely it is to fix the issue.
  Suggestion: This is a summary of the recommendation, in plain english.
  Justification: This is a short explanation of why you think this recommendation will fix the issue.
  Commands: This is a list of commands that the user can execute to implement the recommendation.
  """

  prompt_template = PromptTemplate(
      input_variables=["technology", "goal", "metric_data"],
      template=template,
  )

  final_prompt = prompt_template.format(
    technology=technology,
    goal=goal,
    metric_data=metric_data
  )

  return final_prompt
