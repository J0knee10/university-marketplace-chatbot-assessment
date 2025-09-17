# Prompt Analysis

### 1. Structure and XML-like tags
I divided the prompt into `<system>`, `<behavior>`, `<conditional_logic>`, `<output_schema>`, and `<examples>`.  
This mirrors how we often organise configuration files: each block has a clear purpose and can be parsed or validated automatically.  
Using XML-style tags makes it obvious where one section ends and another begins, and lets future scripts target only the needed part (e.g., extract `<output_schema>` for testing).

### 2. Safety and escalation
Campus marketplaces involve potential scams, dangerous items, or threatening messages.  
By giving explicit rules in `<conditional_logic>` and a structured `output_schema`, the bot knows when to escalate to moderators and how to return a machine-readable summary.  
This prevents silent failures and allows automated tools to log or route serious issues.

### 3. Tone and usability
Under `<behavior>` I defined tone (“clear, friendly, max three paragraphs”) and safe practices (e.g., no direct payment info).  
The aim is to make responses approachable while keeping transactions secure.

### 4. Automation benefits
Because the prompt has consistent tags and an embedded JSON schema, an automation script can:
- Validate that all required tags exist.
- Check the JSON schema for correctness.
- Deploy only the `<system>` + `<behavior>` sections as the live prompt while leaving examples behind.  
This design supports CI/CD for prompt changes, just like infrastructure-as-code.
