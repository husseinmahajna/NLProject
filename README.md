# NLProject

## Introduction

Our objective in this project is to compare the OpenCodeInterpreter with different modern code-generating LLM models. We used the HumanEval dataset to benchmark the models. To achieve this, we needed to:

1. Study the HumanEval dataset structure
2. Understand its components
3. Load the HumanEval dataset into a JSON object

This approach allows us to systematically evaluate and compare the performance of various language models in code generation tasks.

## Experimental Settings

Our experimental setup involved the following steps:

1. Connected with OpenCodeInterpreter and DeepSeek-coder-v2-Instruct using the Dspy package
2. Connected with Claude3.5 Sonnet and Claude3 Sonnet using the Anthropic package
3. Generated solutions for each query using each model and saved them into .jsonl files
   - This allows for multiple uses without regeneration, saving time
4. Imported the .jsonl solutions-files into JSON objects
5. Defined a benchmark function that creates a string for every code response, including:
   - Imports
   - Response code function
   - Check function
   - Call for the check function
6. Executed the string code using the `exec()` method

## Results

We defined two methods of calculating the accuracy of the model:

1. **acc_err_pass:** The accuracy if the samples that received errors were actually the right solutions and passed.
2. **acc_err_fail:** The accuracy if the samples that received errors were wrong solutions and didn't pass.

This dual approach was necessary because some runs returned errors caused by the models using elements not defined in the response code. These elements were defined in the prompt, leading the model to rely on functions or variables given in the prompt without including them in the response. Consequently, executing the code from the response alone could cause errors.

These are the results we got:
---
![image](https://github.com/husseinmahajna/NLProject/assets/70291425/a71ebbf8-a46d-4b15-86e1-f47cf8bc8371)

# Analysis of Model Performance: Claude3.5, Claude3, OCI, and DPV2I

## Overview
This stacked bar chart compares the performance of four AI models: Claude3.5, Claude3, OCI, and DPV2I. The chart categorizes results into three types:
- Passed (green)
- Didn't Pass (Excluding Errors) (red)
- Undefined Error (NameError) (orange)

## Model-by-Model Analysis

### Claude3.5
- **Highest pass rate**: Approximately 90% of tests passed
- **Minimal errors**: Very few undefined errors
- **Overall performance**: Strongest among the four models

### Claude3
- **Good pass rate**: About 65% of tests passed
- **Higher failure rate**: More "Didn't Pass" results compared to Claude3.5
- **Few errors**: Small number of undefined errors

### OCI
- **Moderate performance**: Pass rate around 70%
- **Notable error rate**: Highest proportion of undefined errors
- **Balance**: Fewer outright failures, but more NameErrors than other models

### DPV2I
- **Solid performance**: Pass rate approximately 80%
- **Low error rate**: Minimal undefined errors
- **Improvement area**: Higher "Didn't Pass" rate compared to Claude3.5

## Key Observations
1. **Claude3.5** demonstrates the best overall performance with the highest pass rate and lowest error rate.
2. **OCI** shows potential but is hindered by a high rate of undefined errors.
3. **DPV2I** performs well, ranking second in pass rates.
4. **Claude3** shows the lowest performance among the four models, with the lowest pass rate and a high rate of failures.

## Conclusion
> - The analysis reveals a clear performance hierarchy among the models, with Claude3.5 leading, followed by DPV2I, then OCI, and finally Claude3.
> - Each model shows distinct strengths and areas for potential improvement.

---
![image](https://github.com/husseinmahajna/NLProject/assets/70291425/c35f3486-f3ff-437c-93cc-99d6ce368c36)

## Model-by-Model Analysis

### Claude3.5
- **Highest accuracy**: Approximately 88%
- **Performance**: Clearly outperforms all other models

### DPV2I
- **Second-best accuracy**: Around 79-80%
- **Performance**: Strong showing, but notably behind Claude3.5

### OCI
- **Third place**: Accuracy of about 71%
- **Performance**: Decent performance, though below the top two models

### Claude3
- **Lowest accuracy**: Roughly 66%
- **Performance**: Underperforms compared to other models

## Key Observations

1. Claude3.5 demonstrates superior performance, with a substantial lead over the other models.
2. There's a clear hierarchy in accuracy: Claude3.5 > DPV2I > OCI > Claude3.
3. The gap between the best (Claude3.5) and worst (Claude3) performing models is significant, approximately 22 percentage points.
4. DPV2I shows strong performance, positioning itself as a runner-up to Claude3.5.
5. OCI demonstrates decent capabilities, holding a solid third position.

## Implications

- Claude3.5's superior performance suggests it might be the most reliable for complex tasks.
- The substantial performance gap between Claude3.5 and Claude3 indicates significant improvements in the newer version.
- OCI shows promise with its decent performance, though there's room for improvement to compete with the top models.
- Claude3 may require further refinement to match the performance of the other models in this comparison.

## Conclusion

This analysis reveals a clear performance hierarchy among the models. Claude3.5 stands out as the leader, with DPV2I showing strong potential. OCI demonstrates decent capabilities, securing a solid third position. Claude3 lags behind, suggesting areas for improvement in the future.

## Model Accuracy Ranges

| Model    | Accuracy Range |
|----------|----------------|
| Claude3.5| 0.86 - 0.92    |
| DSV2i    | 0.78 - 0.85    |
| OCI      | 0.66 - 0.77    |
| Claude3  | 0.63 - 0.73    |

> **Note:** Accuracy ranges represent the lower and upper bounds of model performance across different tests.


----

## Alternative Accuracy Measurement

We provide another method for measuring the accuracy of the models, ignoring NameErrors. This approach calculates the results without considering these errors:

### Calculation Method

Accuracy = passed_count / (passed_count + didnt_passed_count - error_count)

Or 

Accuracy = Number of Passed Samples / (Total Samples - Number of NameError Occurrences)

### Results

| Model    | Accuracy |
|----------|:-----------------:|
| Claude3.5| 0.882             |
| DPV2i    | 0.795             |
| OCI      | 0.697             |
| Claude3  | 0.650             |

This measurement offers an alternative perspective on model performance.

focusing on instances where the model produced a valid ( runnable ) output. It helps to highlight the models' capabilities when successfully generating code, regardless of NamErrors.


