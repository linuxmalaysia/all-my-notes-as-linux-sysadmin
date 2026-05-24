# What is DSPy?

DSPy is a framework from Stanford NLP that lets you program language models instead of prompting them. You write Python code describing what you want, and DSPy's optimizers automatically figure out how to make it happen.

## TL;DR

DSPy replaces manual prompt engineering with programmatic optimization. Instead of crafting prompts by trial and error, you define signatures and let DSPy's optimizers find the best approach.

GEPA is DSPy's newest optimizer (July 2025) that uses natural language reflection to improve prompts - beating reinforcement learning approaches while using 35x fewer resources.

## The Problem: Prompt Engineering is Broken

Here's what building with LLMs looks like today:

1. Write a prompt
2. Test it
3. It fails on edge cases
4. Add more instructions
5. Now it's too long and expensive
6. Simplify
7. It fails differently
8. Repeat forever

The core issues:

| Problem | Reality |
| :--- | :--- |
| Brittleness | Prompts break when you change models, add features, or scale up |
| No composability | You can't easily combine prompts like you combine functions |
| Manual optimization | Every improvement requires human intuition and trial-and-error |
| No portability | Prompts optimized for GPT-4 don't transfer to Claude or Llama |

## DSPy: Programming, Not Prompting

DSPy separates what you want from how to achieve it:

- You define: "Given a question and context, produce an answer"
- DSPy figures out: The exact prompt, examples, and structure to make it work

### A Simple Example

**Traditional prompting:**
```python
prompt = """You are a helpful assistant. Given the following context and question, 
provide a comprehensive answer. Be concise but thorough.

Context: {context}
Question: {question}

Answer:"""

response = llm.complete(prompt.format(context=ctx, question=q))
```

**DSPy:**
```python
import dspy

qa = dspy.ChainOfThought("context, question -> answer")
response = qa(context=ctx, question=q)
```
No prompt template. No manual engineering. DSPy handles the rest.

## How DSPy Works

DSPy has three core concepts: Signatures, Modules, and Optimizers.

### 1. Signatures: What You Want
Signatures declare input/output behavior:

```python
# Simple signature
"question -> answer"

# With types
"question: str -> answer: float"

# Multiple inputs and outputs
"context: list[str], question: str -> reasoning: str, answer: str"
```

### 2. Modules: How to Execute
Modules implement signatures with different strategies:

| Module | What It Does |
| :--- | :--- |
| `dspy.Predict` | Basic prediction |
| `dspy.ChainOfThought` | Adds step-by-step reasoning |
| `dspy.ProgramOfThought` | Generates code to solve problems |
| `dspy.ReAct` | Agent with tool use |

### 3. Optimizers: Automatic Improvement
Optimizers tune your program to maximize a metric:

```python
from dspy.teleprompt import MIPROv2

def metric(example, prediction):
    return prediction.answer.lower() == example.answer.lower()

optimizer = MIPROv2(metric=metric, auto="medium")
optimized_qa = optimizer.compile(qa, trainset=examples)
```

## Why GEPA Changes Everything

GEPA (Genetic-Pareto) is DSPy's breakthrough optimizer from July 2025.

### The Key Insight
Instead of treating optimization as an RL problem, GEPA treats it as a reflection problem:
- **Sample trajectories**: Run the program, collect traces
- **Reflect in language**: Ask the LLM to diagnose what went wrong
- **Propose improvements**: Generate new prompt variations
- **Test and combine**: Use Pareto optimization to find the best

### The Results

| Comparison | GEPA Improvement |
| :--- | :--- |
| vs GRPO (RL-based) | +10-20% better, 35x fewer rollouts |
| vs MIPROv2 | +10% across multiple LLMs |

## Real-World Impact

DSPy is in production at JetBlue, Replit, Databricks, Sephora, VMware, and Moody's.

**Benchmark Improvements**

| Task | Before | After | Gain |
| :--- | :--- | :--- | :--- |
| RAG (SemanticF1) | 42% | 61% | +19% |
| ReAct Agent | 24% | 51% | +27% |
| Multi-hop QA | 31% | 59% | +28% |

## Getting Started

**Installation**
```bash
pip install -U dspy
```

**Basic Setup**
```python
import dspy

# Configure your LM
lm = dspy.LM('anthropic/claude-sonnet-4-5-20250929', api_key='YOUR_KEY')
dspy.configure(lm=lm)

# Simple QA with reasoning
qa = dspy.ChainOfThought("question -> answer")
result = qa(question="What is 15% of 80?")
print(result.reasoning)  # Shows step-by-step math
print(result.answer)     # 12
```

## DSPy and Claude Skills

DSPy and Claude Skills solve different problems:

| Aspect | DSPy | Claude Skills |
| :--- | :--- | :--- |
| Focus | Optimizing LLM programs | Teaching workflows |
| When to use | Production systems, complex pipelines | Developer productivity, reusable instructions |
| Optimization | Automatic via algorithms | Manual via writing |

They're complementary. Use Skills for developer workflows and DSPy for production ML pipelines.

## Resources
- Documentation: dspy.ai
- GitHub: github.com/stanfordnlp/dspy (30k+ stars)
- Papers: DSPy (ICLR 2024), GEPA (July 2025)

## Conclusion

DSPy represents a paradigm shift from artisanal prompt crafting to systematic AI engineering. Combined with GEPA's efficient optimization, it's the foundation for building reliable LLM applications.

The teams still hand-crafting prompts in 2025 are competing against people with better tools.
