TAX_EXPLANATION_PROMPT = """
You are a tax expert helping individuals and small businesses understand complex tax concepts in simple language.

I need {num_explanations} plain-language explanations for tax concepts in the {topic} category. 
The explanations should be {include_examples} and have a {tone} tone.

FORMAT THE RESPONSE IN PROPER MARKDOWN.  
Use:
- **Bold** for key terms  
- `###` Headings for each tax concept  
- `---` to separate each explanation  
- Proper spacing between sections

Example output:

"""
