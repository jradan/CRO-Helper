# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CRO-Helper is a conversion rate optimization (CRO) testing documentation system that helps manage A/B test hypotheses, briefs, and results. The repository uses a structured approach to evaluate and track CRO experiments with a scoring system.

## Key Commands

### Knowledge Base Generation
```bash
python build_cro_knowledge.py
```
Rebuilds the consolidated `cro-knowledge.md` file from all source materials. This script automatically combines:
- Scorecard definition
- Test documents from `tests/` directory  
- Brief documents from `briefs/` directory

### GitHub Actions
The repository has automated workflows that trigger knowledge rebuilds when markdown files change. The workflow runs on:
- Push events affecting any `.md` files
- Manual dispatch via `workflow_dispatch`

## Architecture & Structure

### Core Components

**Scorecard System**: Uses a 4-dimension scoring framework (Impact, Confidence, Effort, Clarity & User Trust) with 1-5 scale ratings. Total possible score is 20.

**Document Templates**: 
- `tests/test_template.md` - Full experiment documentation template
- `briefs/test_brief_template.md` - Condensed test brief template

**Knowledge Consolidation**: `build_cro_knowledge.py` creates a single reference file by combining all markdown content in a structured format with clear section delimiters.

### File Organization

```
├── scorecard_definition.md     # CRO scoring criteria
├── tests/                      # Detailed test documentation  
├── briefs/                     # Concise test briefs
├── build_cro_knowledge.py      # Knowledge base builder
└── cro-knowledge.md           # Generated consolidated reference
```

The system follows a template-driven approach where new tests and briefs should use the provided templates to maintain consistency in documentation structure and scoring methodology.

### Workflow Integration

GitHub Actions automatically rebuilds the knowledge base when documentation changes, ensuring the consolidated reference stays current. This enables a documentation-driven CRO process where all test materials are version controlled and automatically compiled.