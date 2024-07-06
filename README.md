# NLProject

## Introduction
Our objective in this project is to compare the OpenCodeInterpreter with different modern code-generating LLM models

We used the HumanEval dataset to benchmark the models

To achieve this we needed to study the HumanEval dataset structure and understand it 

We load the HumanEval dataset into a JSON object 

## Experimental Settings
We Connect with OpenCodeInterpreter and DeepSeek-coder-v2-Instruct using the Dspy package
We Connect with Claude3.5 sonnet and Claude3 sonnet using the anthropic package

We generate solutions for each query using each model and save them into .jsonl files, so we can use them multiple times if we want therefore saving time

We import the .jsonl solutions-files into JSON objects

We define a benchmark function that creates a string for every code response, including the imports, response code function, check function, and the call for the check function 

Then we execute the string code using the exec() method

## Results

*** We defined 2 methods of calculating the accuracy of the model :

**acc_err_pass:** the accuracy if the samples that received errors were actually the right solutions and passed.

**acc_err_fail:** the accuracy if the samples that received errors were wrong solutions and didn't pass.

And that was because some runs returned errors caused by the models using things that are not defined in the response code because they were defined in the prompt, so the model relies on the function or variable given from the prompt, but doesn't include them in the response, there for when executing the code coming from the response it can cause errors.

These are the results we got:

![image](https://github.com/husseinmahajna/NLProject/assets/70291425/ece83d5c-69c6-4daa-b311-c976161d4664)


![image](https://github.com/husseinmahajna/NLProject/assets/70291425/558b8785-9a27-47ed-bd28-ad5add11cef6)

**Claude3.5** : 0.86 - 0.92

**Claude3** : 0.63 - 0.73

**OCI** : 0.66 - 0.77

**DSV2i** : 0.78 - 0.85 




